import g4f
import asyncio

from aiogram.filters import Command
from aiogram.filters.state import State, StateFilter, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

class FSM(StatesGroup):
    begin = State()
    text = State()
    Gop = State()
    finish = State()

async def start(message: Message, state: FSMContext):
    await state.set_state(FSM.text)
    text = 'Внимательно слушаю товарищ!'
    await message.answer(text)

async def text_handler(message: Message, state: FSMContext):
    await state.set_state(FSM.finish)
    text = message.text
    await Gopota(text, message)

async def Gopota(text: str, message: Message):
    txt = f'{text}'
    response = await g4f.ChatCompletion.create_async(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Ответь на русском{txt}"}],
    )  # Alternative model setting
    await message.answer(response)


def register_handlers_gopota(nihao):
    nihao.message.register(start, StateFilter(FSM.begin))
    nihao.message.register(text_handler, StateFilter(FSM.text))
    nihao.message.register(start, Command(commands='Say'))
