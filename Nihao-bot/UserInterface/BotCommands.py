from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot):
    commands = [
        BotCommand(
            command='start',
            description='Поздороваться с Нихао'
        ),
        BotCommand(
            command='help',
            description='Позвать Нихао'
        ),
        BotCommand(
            command='dedinside',
            description='Позвать собутыльника'
        ),
        BotCommand(
            command='stf',
            description='Таймер-Отсчет'
        ),
        BotCommand(
            command='list',
            description='Игры на диске'
        ),
        BotCommand(
            command='wiki',
            description='Воспользоватся западным ресурсом'
        ),
        BotCommand(
            command='anecdote',
            description='Позвать собутыльника'
        ),
        BotCommand(
            command='anecdote',
            description='Спросить Нихао'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())