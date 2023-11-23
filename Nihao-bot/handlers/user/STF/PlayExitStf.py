import asyncio
import os

from aiogram.filters import StateFilter

from handlers.user import stf
import aiosqlite
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile


async def stfPlay(message: types.Message, state: FSMContext):
    await state.set_state(stf.FSM.finish)
    database_path = os.path.join('DB', 'sqlite', 'user_data.db')
    async with aiosqlite.connect(database_path) as db:
        cursor = await db.execute('SELECT work_time, rest_time FROM user_data WHERE user_id = ?', (stf.UserData.user_id,))
        row = await cursor.fetchone()
        if row:
            work_time_minutes = row[0] * 60  # Преобразуем минуты в секунды для work_time
            rest_time_minutes = row[1] * 60  # Преобразуем минуты в секунды для rest_time
        else:
            print(row)
            work_time_minutes = 18 * 60
            rest_time_minutes = 18 * 60
    min = 0
    sec = 0
    text = f"Впахивай как стахановец следующие: {min:02d}:{sec:02d}"
    sent_message = await message.answer(text)
    total_seconds_for_work = work_time_minutes
    total_seconds_for_rest = rest_time_minutes
    for second in range(total_seconds_for_work-1, 0, -1):
        minutes = second // 60
        seconds_remaining = second % 60

        text = f"Впахивай как стахановец следующие: {minutes:02d}:{seconds_remaining:02d}"

        await sent_message.edit_text(text, parse_mode="HTML")
        await asyncio.sleep(1)
    for second in range(total_seconds_for_rest - 1, 0, -1):
        minutes = second // 60
        seconds_remaining = second % 60

        text = f"Отдыхай пролетарий следующие: {minutes:02d}:{seconds_remaining:02d}"

        await sent_message.edit_text(text, parse_mode="HTML")
        await asyncio.sleep(1)
    await sent_message.delete()
    await stf.stfStart(message, state)

async def stfExit(message: Message, state: FSMContext):
    await state.set_state(stf.FSM.finish)
    await message.reply(
        "Очень жаль!!!")
    image_path = FSInputFile("Files/Images/Png/sad_smiley_sticker.webp")
    await message.answer_document(image_path)

