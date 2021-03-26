
async def startup(dp):
    from utils.notify import on_startup_notify
    await on_startup_notify(dp)
    print("Бот запущен")


if __name__ == '__main__':
    from aiogram import executor
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    
    from handlers import dp
    from utils.namefinder import findnames
    from utils.notify import pavels_day

    async def pavels_day_test():
        names = await findnames()
        if "Павел" in names:
            await pavels_day(dp)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(pavels_day_test, 'cron', hour=16, minute=49)
    scheduler.start()
    
    executor.start_polling(dp,on_startup=startup)