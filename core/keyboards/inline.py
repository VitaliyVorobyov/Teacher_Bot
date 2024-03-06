from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.callbackdata import Back, KeyboardAdmin, UserData, Register


def keyboard_admin():
    kb = InlineKeyboardBuilder()
    kb.button(text='Создать стартовое меню', callback_data=KeyboardAdmin(name='start_menu'))
    kb.button(text='Создать тест', callback_data=KeyboardAdmin(name='create_test'))
    kb.button(text='Статистика', callback_data=KeyboardAdmin(name='statistics'))
    kb.button(text='Помощь', callback_data=KeyboardAdmin(name='help'))
    kb.button(text='Назад', callback_data=Back(name='back'))
    kb.adjust(1)
    return kb.as_markup()


def keyboard_back():
    kb = InlineKeyboardBuilder()
    kb.button(text='Назад', callback_data=Back(name='back'))
    kb.adjust(1)
    return kb.as_markup()


def keyboard_go_to_bot():
    kb = InlineKeyboardBuilder()
    kb.button(text='Перейти к боту', url='https://t.me/TeacherAdmBot')
    kb.adjust(1)
    return kb.as_markup()


def keyboard_user(keyboard: dict, back: bool = True, admin: bool = False, new_dir: bool = False):
    kb = InlineKeyboardBuilder()
    for key, values in keyboard.items():
        kb.button(text=values, callback_data=UserData(id=key, name=values, add_name='user_menu'))
    if new_dir:
        kb.button(text='Новый раздел', callback_data=KeyboardAdmin(name='new_button'))
    if admin:
        kb.button(text='Админ меню', callback_data=KeyboardAdmin(name='admin_menu'))
    if back:
        kb.button(text='Назад', callback_data=Back(name='back'))
    kb.adjust(1)
    return kb.as_markup()


def keyboard_edit_content(scroll_data: list = None, admin: bool = False, publish: bool = False, new_dir: bool = False,
                          content_id: int = None):
    kb = InlineKeyboardBuilder()
    if scroll_data:
        kb.button(text='<<<', callback_data=UserData(id=scroll_data[0], name='scroll', add_name='last_page'))
        kb.button(text=f'{scroll_data[0]}-{scroll_data[1]}', callback_data=UserData(id=scroll_data[0], name='scroll',
                                                                                    add_name='count_page'))
        kb.button(text='>>>', callback_data=UserData(id=scroll_data[0], name='scroll', add_name='next_page'))
    if admin:
        kb.button(text="+ Картинка", callback_data=KeyboardAdmin(name="image"))
        kb.button(text="+ Описание", callback_data=KeyboardAdmin(name="description"))
        if publish:
            kb.button(text="Сохранить и Опубликовать", callback_data=KeyboardAdmin(name="publish"))
        if new_dir:
            kb.button(text='+ Новый раздел', callback_data=KeyboardAdmin(name='new_button'))
    kb.button(text="Удалить", callback_data=Register(id=content_id, name="delete"))
    kb.button(text='Назад', callback_data=Back(name='back'))
    if scroll_data and admin:
        if publish:
            kb.adjust(3, 2, 1, 1, 1)
        else:
            kb.adjust(3, 2, 1, 1)
    if admin and not scroll_data:
        if new_dir and publish:
            kb.adjust(2, 1, 1, 1, 1)
        else:
            kb.adjust(2, 1, 1, 1)
    return kb.as_markup()


def keyboard_register(user_id: int):
    kb = InlineKeyboardBuilder()
    kb.button(text='Подтвердить', callback_data=Register(id=user_id, name='confirm'))
    kb.adjust(1)
    return kb.as_markup()


def keyboard_start():
    kb = InlineKeyboardBuilder()
    kb.button(text='Начать', callback_data=Register(id=0, name='start'))
    kb.adjust(1)
    return kb.as_markup()
