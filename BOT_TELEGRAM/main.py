#
# from aiogram import types, executor, Dispatcher, Bot
# from bs4 import BeautifulSoup
# import requests
#
#
# bot = Bot("5671827929:AAG4LQR9-tPnrrv2Qw2dJNd0j1rG9SJNKmE")
#
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands = ['start']) #команда start
# async def start(message: types.message):
#     await bot.send_message(message.chat.id, """Привет, я бот, который может показать тебе,
#     какие сегодня акции есть в торговых сетях Минска таких как
#     <b><a href = "https://korona.by/hypermarkets/promotions">Корона, Соседи, Виталюр, Грин</a></b>
#     Введи название сети""",
#     parse_mode = "html",
#     disable_web_page_preview=1)
#
#
# #парсер
# @dp.message_handler(content_types=['text'])
# async def parser(message: types.message):
#     url = "https://korona.by/hypermarkets/promotions" + message.text
#     requests = requests.get(url)
#     soup = BeautifulSoup(requests.text, "html.parser")
#
#
#
#
#
#
#
# executor.start_polling(dp) #бот будет бесконечно обрабатывать поиск

