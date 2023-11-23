from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.user.STF import SettingsStf, PlayExitStf


async def process_callback_ok(callback: types.CallbackQuery, state: FSMContext):
    callback.__dict__['data'] = "none"
    data = await state.get_data()
    message_to_delete = data.get('message_to_delete')
    await message_to_delete.delete()
    await PlayExitStf.stfPlay(callback.message, state)


async def process_callback_setting(callback: types.CallbackQuery, state: FSMContext):
    callback.__dict__['data'] = "none"
    data = await state.get_data()
    message_to_delete = data.get('message_to_delete')
    await message_to_delete.delete()
    await SettingsStf.stfSettingPart1(callback.message, state)

async def process_callback_canel(callback: types.CallbackQuery, state: FSMContext):
    callback.__dict__['data'] = "none"
    data = await state.get_data()
    message_to_delete = data.get('message_to_delete')
    await message_to_delete.delete()
    await PlayExitStf.stfExit(callback.message, state)