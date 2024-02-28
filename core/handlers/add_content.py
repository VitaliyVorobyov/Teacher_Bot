from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from core.keyboards.inline import keyboard_go_to_bot, keyboard_back, keyboard_edit_content
from core.utils.settings import settings
from core.utils.callbackdata import KeyboardAdmin
from core.utils.states import ContentMenuState
from core.utils.dbconnect import Request
from core.utils.edit_message import edit_message


router = Router()


@router.callback_query(KeyboardAdmin.filter(F.name == 'image'))
async def add_image(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(ContentMenuState.file_id)
    await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption='Отправьте изображение',
                                   reply_markup=keyboard_back())


@router.callback_query(KeyboardAdmin.filter(F.name == 'description'))
async def add_image(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(ContentMenuState.description)
    await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption='Отправьте описание',
                                   reply_markup=keyboard_back())


@router.message(F.photo, ContentMenuState.file_id)
async def save_image(message: Message, bot: Bot, state: FSMContext, request: Request):
    file_id = message.photo[-1].file_id
    row_id = await request.add_file_id(file_id)
    file = await request.get_file(1)
    await state.update_data(file_id=file_id)
    await state.set_state(ContentMenuState.row_id)
    await state.update_data(row_id=row_id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_message(bot, message.message_id, keyboard_edit_content(admin=True, publish=True),
                       'Изображение Сохранено', message.from_user.id, file)


@router.message(F.text, ContentMenuState.description)
async def save_description(message: Message, bot: Bot, state: FSMContext, request: Request):
    description = message.text
    description_id = await request.add_description(description)
    file = await request.get_file(1)
    await state.update_data(description=description)
    await state.set_state(ContentMenuState.description_id)
    await state.update_data(description_id=description_id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_message(bot, message.message_id, keyboard_edit_content(admin=True, publish=True),
                       'Описание Сохранено', message.chat.id, file)


@router.callback_query(KeyboardAdmin.filter(F.name == 'publish'))
async def publish(call: CallbackQuery, bot: Bot, state: FSMContext, request: Request):
    context = await state.get_data()
    button_id = context.get('id_button')
    file_id = context.get('file_id')
    row_id = context.get('row_id')
    description_id = context.get('description_id')
    description = context.get('description')
    file = await request.get_file(1)
    if file_id and description:
        file_to_description = await request.add_file_to_description(row_id, description_id)
        await request.add_content_to_button(button_id, file_to_description)
        await bot.send_photo(settings.bots.channel_id, photo=file_id, caption=description,
                             reply_markup=keyboard_go_to_bot())
    if file_id and not description:
        file_to_description = await request.add_file_to_description(1, description_id)
        await request.add_content_to_button(button_id, file_to_description)
        await bot.send_photo(settings.bots.channel_id, file_id, reply_markup=keyboard_go_to_bot())
    if description and not file_id:
        file_to_description = await request.add_file_to_description(1, description_id)
        await request.add_content_to_button(button_id, file_to_description)
        await bot.send_message(settings.bots.channel_id, description, reply_markup=keyboard_go_to_bot())
    await state.clear()
    await edit_message(bot, call.message.message_id, keyboard_back(), 'Сообщение опубликовано!',
                       call.from_user.id, file)
