from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from alef_bot.create_bot import bot
from alef_bot.app import start_operation, put_locality, get_list_locality


async def command_start(message: Message):
    aaa = start_operation()
    xxx = aaa[0]
    yyy = aaa[1]
    zzz = aaa[2]
    put_locality(xxx, yyy, zzz)
    await bot.send_message(
        message.from_user.id, "БД заполнена") 

# Для варианта с инлайн кнопками

# async def command_get_list(message: Message):
#     x = get_list_locality(message.text)
#     sps = []
#     for i in range(len(x)):
#         url_batton = InlineKeyboardButton(text=x[i][0], url=x[i][1])
#         sps.append(url_batton)
#     url_kb = InlineKeyboardMarkup()
#     url_kb.add(*sps)
#     await message.answer('Варианты:', reply_markup=url_kb)

async def command_get_list(message: Message):
    
    if message.text.startswith('/'):
        st = message.text[1::]
        x = get_list_locality(st)
        sps = []
        for i in range(len(x)):
            sps.append(x[i][0])
        await bot.send_message(
            message.from_user.id, sps)

    else:
        x = get_list_locality(message.text)
        if x[0][0] ==  message.text:
            sps_1 = []
            for i in range(len(x)):
                sps_1.append(x[i][1])
                sps_1.append(x[i][2])
            await bot.send_message(
                message.from_user.id, sps_1)
        else:
            await bot.send_message(message.from_user.id, "Укажите точное название населенного пункта")
        

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(command_get_list)