import aiosqlite
import os

async def create_database():
    database_path = os.path.join('DB', 'sqlite', 'user_data.db')

    async with aiosqlite.connect(database_path) as db:
        cursor = await db.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id int,
                work_time int,
                rest_time int
            )
        ''')
        await cursor.close()