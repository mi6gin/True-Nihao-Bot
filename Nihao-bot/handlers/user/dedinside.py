import asyncio
from aiogram.filters import Command
from aiogram.filters.state import State, StateFilter, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class FSM(StatesGroup):
    start = State()
    spam = State()
    finish = State()


async def start(message: Message, state: FSMContext):
    await state.set_state(FSM.spam)
    text = 'Здравия желаю господа-коммунисты-бояре\r\nКто нас интересует?'
    await message.answer(text)


async def spam(message: Message, state: FSMContext):
    await state.set_state(FSM.finish)
    text = message.text
    if text.startswith('@'):
        for i in range(10):
            msg = await message.answer(text)
            await asyncio.sleep(5)
            await msg.delete()
    else:
        await state.set_state(FSM.spam)
        await message.answer('Нет-нет-нет, товарищ...\nВы делаете всё не так, надо указывать перед ником \"@\"\nНапример [@githab_parasha]")')


def register_handlers_dedinside(nihao):
    nihao.message.register(start, StateFilter(FSM.start))
    nihao.message.register(spam, StateFilter(FSM.spam))
    nihao.message.register(start, Command(commands='dedinside'))