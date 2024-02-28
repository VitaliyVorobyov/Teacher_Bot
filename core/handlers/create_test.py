from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery

from core.keyboards.inline import keyboard_back
from core.utils.callbackdata import KeyboardAdmin


router = Router()


@router.callback_query(KeyboardAdmin.filter(F.name == 'create_test'))
async def help_(call: CallbackQuery, bot: Bot):
    await bot.edit_message_caption(call.from_user.id, call.message.message_id, caption=f'Раздел в разработке',
                                   reply_markup=keyboard_back())