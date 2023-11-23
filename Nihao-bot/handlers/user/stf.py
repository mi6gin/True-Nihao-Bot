import os
from handlers.user.STF import SettingsStf, PlayExitStf, CallbackStf, StartStf
from dataclasses import dataclass
import aiosqlite
from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import State, StateFilter, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
class FSM(StatesGroup):
    stfStart = State()
    stfPlay = State()
    stfExit = State()
    stfSettingP1 = State()
    stfSettingP2 = State()
    finish = State()
@dataclass
class UserData:
    user_id: int
    work_time: int = 15
    rest_time: int = 15
def create_user_data_from_message(message):
    UserData.user_id = message.from_user.id
def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Запуск", callback_data="ok"),
            types.InlineKeyboardButton(text="Настройки", callback_data="setting"),
            types.InlineKeyboardButton(text="Отмена", callback_data="canel")
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def register_handlers_stf(nihao):
    nihao.message.register(StartStf.stfStart, StateFilter(FSM.stfStart))
    nihao.callback_query.register(CallbackStf.process_callback_ok, lambda c: c.data == 'ok')
    nihao.callback_query.register(CallbackStf.process_callback_canel, lambda c: c.data == 'canel')
    nihao.callback_query.register(CallbackStf.process_callback_setting, lambda c: c.data == 'setting')
    nihao.message.register(PlayExitStf.stfPlay, StateFilter(FSM.stfPlay))
    nihao.message.register(SettingsStf.stfSettingPart1, StateFilter(FSM.stfSettingP1))
    nihao.message.register(SettingsStf.stfSettingPart2, StateFilter(FSM.stfSettingP2))
    nihao.message.register(PlayExitStf.stfExit, StateFilter(FSM.stfExit))
    nihao.message.register(StartStf.stfStart, Command(commands='stf'))