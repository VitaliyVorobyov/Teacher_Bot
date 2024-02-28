from aiogram.filters.callback_data import CallbackData


class KeyboardAdmin(CallbackData, prefix='start'):
    name: str


class Back(CallbackData, prefix='back'):
    name: str


class UserData(CallbackData, prefix='user'):
    id: int
    name: str
    add_name: str


class Register(CallbackData, prefix='register'):
    id: int
    name: str
