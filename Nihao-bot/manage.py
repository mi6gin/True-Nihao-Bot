import logging
from settings import nihao, bot
from aiogram import types
from handlers.user import dedinside, listochek, Start, Help, wikipedia_reader, stf, ShtirlicStf, Asked
from UserInterface import BotCommands
from DB import Database
logging.basicConfig(level=logging.INFO)

Start.register_handlers_start(nihao)
Help.register_handlers_help(nihao)
dedinside.register_handlers_dedinside(nihao)
Asked.register_handlers_gopota(nihao)
wikipedia_reader.register_handlers_wiki(nihao)
stf.register_handlers_stf(nihao)
ShtirlicStf.register_handlers_anekdots(nihao)
async def main():
    await BotCommands.set_commands(bot)
    await Database.create_database()
    await nihao.start_polling(bot)
