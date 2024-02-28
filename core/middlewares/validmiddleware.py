from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from core.utils.settings import settings
from core.keyboards.inline import keyboard_register


class ValidationMiddleware(BaseMiddleware):
    def __init__(self, users: list[int], admin_id: int = settings.bots.admin_id):
        super().__init__()
        self.users = users
        self.admin_id = admin_id

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data["event_from_user"]
        if user.id == self.admin_id:
            data['users'] = self.admin_id
            return await handler(event, data)
        if user.id not in self.users:
            await event.answer(f"Вы не авторизованы для использования этого бота, дождитесь авторизации")
            await event.bot.send_message(settings.bots.admin_id,
                                         f"Пользователь {user.full_name} пытался использовать бота",
                                         reply_markup=keyboard_register(user.id))
        else:
            data['users'] = self.users
            return await handler(event, data)
