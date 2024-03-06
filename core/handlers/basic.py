from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from core.keyboards.inline import keyboard_user, keyboard_edit_content
from core.utils.callbackdata import Back, UserData, Register
from core.utils.dbconnect import Request
from core.utils.states import ContentMenuState
from core.utils.create_scrolling import scrolling


router = Router()


@router.message(Command(commands=['start']))
@router.callback_query(Register.filter(F.name == 'start'))
async def start(message: Message, bot: Bot, state: FSMContext, request: Request):
    await state.clear()
    photo = await request.get_file(1)
    get_keyword = await request.get_buttons()
    keywords_dict = {x['button_id']: x['name_button'] for x in get_keyword if x['start_button'] is True}
    try:
        await message.answer_photo(photo, f'Привет, {message.from_user.full_name}!',
                                   reply_markup=keyboard_user(keywords_dict, admin=True, back=False))
    except AttributeError:
        await bot.send_photo(message.from_user.id, photo, caption=f'Привет, {message.from_user.full_name}!',
                             reply_markup=keyboard_user(keywords_dict, admin=True, back=False))


@router.callback_query(UserData.filter(F.add_name == 'user_menu'))
async def navigate_to_menu(call: CallbackQuery, bot: Bot, callback_data: UserData, state: FSMContext,
                           request: Request):
    await state.set_state(ContentMenuState.id_button)
    await state.update_data(id_button=callback_data.id)
    get_keyword = await request.get_buttons_for_menu(callback_data.id)
    keywords_dict = {x['button_id_to']: x['name_button'] for x in get_keyword}
    if len(keywords_dict) == 0:
        await state.set_state(ContentMenuState.id_button)
        await state.update_data(id_button=callback_data.id)
        content = await request.get_content_for_button(callback_data.id)
        if content:
            scroll_data, file, description, content_id = await scrolling(content, 1, request)
            await bot.edit_message_media(InputMediaPhoto(media=file, caption=description),
                                         call.from_user.id, call.message.message_id,
                                         reply_markup=keyboard_edit_content(scroll_data=scroll_data, admin=True,
                                                                            content_id=content_id))
        else:
            await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption='Раздел пуст',
                                           reply_markup=keyboard_edit_content(admin=True, new_dir=True, content_id=0))
    else:
        await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption=f'Выберите раздел',
                                       reply_markup=keyboard_user(keywords_dict, new_dir=True))


@router.callback_query(UserData.filter(F.add_name == 'next_page'))
async def next_page(call: CallbackQuery, bot: Bot, callback_data: UserData, state: FSMContext, request: Request):
    context = await state.get_data()
    button_id = context.get('id_button')
    content = await request.get_content_for_button(button_id)
    scroll_data, file, description, content_id = await scrolling(content, callback_data.id+1, request)
    await bot.edit_message_media(InputMediaPhoto(media=file, caption=description),
                                 call.from_user.id, call.message.message_id,
                                 reply_markup=keyboard_edit_content(scroll_data=scroll_data, admin=True,
                                                                    content_id=content_id))


@router.callback_query(UserData.filter(F.add_name == 'last_page'))
async def next_page(call: CallbackQuery, bot: Bot, callback_data: UserData, state: FSMContext, request: Request):
    context = await state.get_data()
    button_id = context.get('id_button')
    content = await request.get_content_for_button(button_id)
    scroll_data, file, description, content_id = await scrolling(content, callback_data.id-1, request)
    await bot.edit_message_media(InputMediaPhoto(media=file, caption=description),
                                 call.from_user.id, call.message.message_id,
                                 reply_markup=keyboard_edit_content(scroll_data=scroll_data, admin=True,
                                                                    content_id=content_id))


@router.callback_query(Back.filter(F.name == 'back'))
async def back(call: CallbackQuery, bot: Bot, state: FSMContext, request: Request):
    await state.clear()
    get_keyword = await request.get_buttons()
    file = await request.get_file(1)
    keywords_dict = {x['button_id']: x['name_button'] for x in get_keyword if x['start_button'] is True}
    await bot.edit_message_media(InputMediaPhoto(media=file, caption='Выберите действие'),
                                 call.from_user.id, call.message.message_id,
                                 reply_markup=keyboard_user(keywords_dict, admin=True, back=False))
