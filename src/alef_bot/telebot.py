from aiogram.utils import executor

from alef_bot.create_bot import dp
from alef_bot.handlers import client


async def on_startup(dp):
    print("Бот онлайн")


client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)