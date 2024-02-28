from aiogram.fsm.state import State, StatesGroup


class ContentMenuState(StatesGroup):
    status = State()
    id_button = State()
    name_button = State()
    description = State()
    row_id = State()
    file_id = State()
    description_id = State()
