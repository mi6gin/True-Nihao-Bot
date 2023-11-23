import os
from handlers.user.STF import SettingsStf, PlayExitStf, CallbackStf
from dataclasses import dataclass
import aiosqlite
from aiogram import types
from aiogram.filters import Command
from handlers.user import stf
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

async def stfStart(message: Message, state: FSMContext):
    await state.set_state(stf.FSM.stfStart)
    stf.create_user_data_from_message(message)
    photo_id = 'https://sun9-35.userapi.com/impg/d3F87txM3NsX4b6fg-_iICq-bmCwx4vmNvw9pQ/sc4faeaM5aU.jpg?size=1024x1024&quality=95&sign=122617b191efba153ec5591d477f43f0&type=album'
    message_to_delete = await message.answer_photo(photo_id,
          caption='Привет товарищ, ты запустил особый режим\r\nРежим ПРОГУЛКИ подразумевает концентрацию и усидчевость\r\nПо умолчанию стоит 15 минут на работу и на отдых, но вы можете настроить их под себя\r\nКак будешь готов дай мне знать',
          reply_markup=stf.get_keyboard()
    )
    await state.update_data(message_to_delete=message_to_delete)
    database_path = os.path.join('DB', 'sqlite', 'user_data.db')

    async with aiosqlite.connect(database_path) as db:
        cursor = await db.execute('SELECT user_id FROM user_data WHERE user_id = ?',
                                  (stf.UserData.user_id,))
        existing_user = await cursor.fetchone()

        if not existing_user:
            # Если записи с данным user_id нет, создаем новую запись
            insert_query = '''
                    INSERT INTO user_data (user_id, work_time, rest_time)
                    VALUES (?, ?, ?)
                '''
            await db.execute(insert_query,
                             (
                              stf.UserData.user_id,
                              stf.UserData.work_time,
                              stf.UserData.rest_time))
            await db.commit()
        else:
            pass