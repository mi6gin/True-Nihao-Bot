from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Dispatcher
import manage
import wikipedia
import logging
from aiogram.filters import Command, StateFilter

logger = logging.getLogger(__name__)


class FSM(StatesGroup):
    search = State()
    get_data = State()
    finish = State()


async def search(message: Message, state: FSMContext):
    await message.reply(
        'Привет товарищ, вы включили режим википедии\nОтправьте мне название статьи информацию о которой вы хотели бы узнать')
    await state.set_state(FSM.get_data)


async def get_data(message: Message, state: FSMContext):
    await state.set_state(FSM.finish)
    wikipedia.set_lang("ru")
    try:
        quote = wikipedia.summary(message.text, sentences=4)
        await message.answer(quote)
    except Exception as e:
        logger.info(e)
        await message.answer('Извините товарищ, но такой статьи не существует')


def register_handlers_wiki(nihao: Dispatcher):
    nihao.message.register(search, StateFilter(FSM.search))
    nihao.message.register(get_data, StateFilter(FSM.get_data))
    nihao.message.register(search, Command(commands=['wiki']))
