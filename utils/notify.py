from aiogram import Dispatcher

from data.config import admin_id


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(admin_id, "Бот Запущен")


async def pavels_day(dp: Dispatcher):
    await dp.bot.send_message(admin_id, "Сегодня день Павла")