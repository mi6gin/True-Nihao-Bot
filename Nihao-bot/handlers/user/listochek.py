from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Dispatcher
import manage
from aiogram.filters import Command

class FSM(StatesGroup):
    list_def = State()
    list = State()
    finish = State()


async def list_def(message: Message, state: FSMContext):
    await message.reply(
        'Ваш список:\n1)Остальгия;\n2)Кризис в кремле;\n3)Политический симулятор.\nДля того чтобы получить доступ к файлам вышлите мне их номер в списке.')
    manage.nihao.message.register(list, state=FSM.list)
    await state.set_state(FSM.list)


async def list(message: Message, state: FSMContext):
    await state.set_state(FSM.finish)
    text = message.text
    if text == "1":
        await message.reply(
            "Остальгия: берлинская стена - https://drive.google.com/drive/folders/1-kagrWnuxGG5ZAu4OW3R_WO0nISELn6m?usp=sharing")
    elif text == "2":
        await message.reply(
            "Кризис в кремле - https://drive.google.com/drive/folders/1nniufJ29QuEzGLAVqcAOAIWUxNBL7u2O?usp=sharing")
    elif text == "3":
        await message.reply(
            "Collapse: A Political Simulator - https://drive.google.com/drive/folders/1MTpE7ejIknPiWGG6CcdVWGVu03nkzUPL?usp=sharing")
    else:
        await message.reply("К сожалению то, что вы простие меня сделать...Мягко говоря неосуществимо")
        await state.set_state(FSM.list)


def register_handlers_list(nihao: Dispatcher):
    nihao.message.register(list_def, Command(commands=['list']))
