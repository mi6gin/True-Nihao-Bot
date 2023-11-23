import os
from handlers.user import stf
import aiosqlite
from aiogram import types
from aiogram.fsm.context import FSMContext
import re


async def stfSettingPart1(message: types.Message, state: FSMContext):
    await state.set_state(stf.FSM.stfSettingP2)
    # Отправьте пользователю инструкции о том, как отправить сообщение с необходимым форматом
    await message.answer(
        "Пожалуйста читайте внимательно!!!\nОтправьте мне сообщение в таком стиле:\n Работа: [число минут в цифрах], Отдых: [число минут в цифрах]")

async def stfSettingPart2(message: types.Message, state: FSMContext):
    await state.set_state(stf.FSM.finish)
    text = message.text
    # Проверяем, соответствует ли текст сообщения формату
    pattern = r'^Работа: (\d+), Отдых: (\d+)$'
    match = re.match(pattern, text)
    if match:
        # Если сообщение соответствует формату, извлекаем числа для работы и отдыха
        work_time = int(match.group(1))
        rest_time = int(match.group(2))

        # Получаем ID пользователя
        user_id = stf.UserData.user_id
        print(user_id)

        # Обновляем данные пользователя в базе данных
        database_path = os.path.join('DB', 'sqlite', 'user_data.db')
        async with aiosqlite.connect(database_path) as db:
            cursor = await db.execute('''
                    UPDATE user_data
                    SET work_time = ?, rest_time = ?
                    WHERE user_id = ?
                ''', (work_time, rest_time, user_id))
            await db.commit()

        await message.reply('Данные успешно обновлены!')

    else:
        await message.answer(
            'Нет-нет-нет, товарищ...\nВы делаете всё не так, надо указывать перед ником \"@\"\nНапример [@githab_parasha]')

