from aiogram import Dispatcher, types
from aiogram.filters import Command


async def start(message: types.Message):
    await message.reply(
        "Здравствуйте товарищ ✌️, меня зовут Нихао, я ассистент мистера Романова! Если вам что-нибудь понадобится, то просто воспользуйтесь командой /help, и я сразу же прийду к вам на помощь!")


def register_handlers_start(nihao: Dispatcher):
    nihao.message.register(start, Command('start'))
