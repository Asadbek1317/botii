from aiogram.dispatcher.filters.state import StatesGroup, State


class PersanalData(StatesGroup):
    name = State()
    phone = State()

