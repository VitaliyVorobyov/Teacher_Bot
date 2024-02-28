from aiogram.exceptions import TelegramBadRequest


async def edit_message(bot, message_id, keyboard, caption, user_id, photo):
    for i in range(100):
        try:
            await bot.edit_message_caption(user_id, message_id - i,
                                           caption=caption, reply_markup=keyboard)
            break
        except TelegramBadRequest:
            pass
        if i == 99:
            await bot.answer_photo(photo, caption, reply_markup=keyboard)
            break
