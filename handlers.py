from loader import dp, bot
from aiogram import types

from utils.namefinder import findnames


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nПо команде /names я отправлю тебе сегодняшние именины!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/names - отправляет список сегодняшних именин")


@dp.message_handler(commands=['names'])
async def process_help_command(message: types.Message):
    names = await findnames()
    text = "Сегодняшние именины:\n"
    for name in names:
        text += name + "\n"
    await message.answer(text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)