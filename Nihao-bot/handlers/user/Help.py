from aiogram import Dispatcher, types
from aiogram.filters import Command


async def help(message: types.Message):
    photo_id = 'https://sun9-1.userapi.com/impg/dnvKms_lz49AsprMp7u2WORn8iBtyAShpRcQKg/WincNLcilWA.jpg?size=1170x1170&quality=95&sign=c5ebdc06d298cdd8d3812611b1f8ae56&type=album'
    await message.answer_photo(photo_id,
                               caption='Ну что товарищ, вам нужна моя помощь? Не волнуйтесь, сейчас я вам всё объясню и расскажу😉 Среди доступных мне функций есть:\n/anecdote- я могу рассказать вам шутку про нашего любимого разведчика;\n/dedinside- это функция агрессивного зова товарища, просто отправьте мне его никнейм и сообщение к нему(если конечно вы хотите ему что-то передать);\n/stf- это функция которая которая распределяет ваше время, нужна для тех у кого нет силы воли;\nНу вроде это всё, про /help и /start я рассказывать не стала, потому что вы уже и так знаете, что они делают😅',
                               )


def register_handlers_help(nihao: Dispatcher):
    nihao.message.register(help, Command('help'))
