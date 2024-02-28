from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from core.keyboards.inline import keyboard_admin, keyboard_back
from core.utils.callbackdata import KeyboardAdmin
from core.utils.states import ContentMenuState
from core.utils.dbconnect import Request
from core.utils.edit_message import edit_message

router = Router()


@router.callback_query(KeyboardAdmin.filter(F.name == 'admin_menu'))
async def admin_menu(call: CallbackQuery, bot: Bot):
    await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption='Выберите действие',
                                   reply_markup=keyboard_admin())


@router.callback_query(KeyboardAdmin.filter(F.name == 'new_button'))
async def new_button(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(ContentMenuState.status)
    await state.update_data(status='add_button')
    await state.set_state(ContentMenuState.name_button)
    await bot.edit_message_caption(call.from_user.id, call.message.message_id,
                                   caption='Напишите название нового раздела:', reply_markup=keyboard_back())


@router.callback_query(KeyboardAdmin.filter(F.name == 'start_menu'))
async def add_button(call: CallbackQuery, bot: Bot, request: Request, state: FSMContext):
    await state.set_state(ContentMenuState.status)
    await state.update_data(status='start_menu')
    await state.set_state(ContentMenuState.name_button)
    buttons = await request.get_buttons()
    buttons_list = [f"- {x['name_button']}" for x in buttons if x['start_button'] is True]
    if buttons_list:
        buttons_list = '\n'.join(buttons_list)
    else:
        buttons_list = 'Список пуст'
    await bot.edit_message_caption(call.from_user.id, call.message.message_id,
                                   caption=f'Список разделов:\n{buttons_list}\n\nНапишите название раздела:',
                                   reply_markup=keyboard_back())


@router.message(ContentMenuState.name_button)
async def add_button_name(message: Message, bot: Bot, state: FSMContext, request: Request):
    context = await state.get_data()
    status = context.get('status')
    file = await request.get_file(1)
    if status == 'add_button':
        button_id = context.get('id_button')
        button_id_to = await request.add_button(message.text)
        await request.add_new_button_to_button(button_id, button_id_to)
    if status == 'start_menu':
        await request.add_button_start(message.text)
    await state.clear()
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_message(bot, message.message_id, keyboard_back(), 'Раздел добавлен', message.chat.id, file)
