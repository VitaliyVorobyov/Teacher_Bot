from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery

from core.utils.callbackdata import Register
from core.utils.dbconnect import Request
from core.utils.edit_message import edit_message
from core.keyboards.inline import keyboard_back, keyboard_start


router = Router()


@router.callback_query(Register.filter(F.name == 'confirm'))
async def register(call: CallbackQuery, bot: Bot, callback_data: Register, request: Request):
    file = await request.get_file(1)
    await request.add_user(callback_data.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(callback_data.id, 'Ваш аккаунт подтвержден', reply_markup=keyboard_start())
    await edit_message(bot, call.message.message_id, keyboard_back(), 'Пользователь зарегистрирован',
                       call.from_user.id, file)
