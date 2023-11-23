import random

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


async def send_anecdote(message: Message):
    with open("Files/Txt/anekdots.txt", "r", encoding="utf-8") as file:
        anekdots = file.read().split('\n\n')  # Разделение анекдотов между собой двойным переводом строки

    if anekdots:
        random_anecdote = random.choice(anekdots)
        await message.answer(random_anecdote)
    else:
        await message.answer("К сожалению, анекдоты не найдены.")

def register_handlers_anekdots(nihao: Dispatcher):
    nihao.message.register(send_anecdote, Command('anecdote'))
