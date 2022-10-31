#5671827929:AAG4LQR9-tPnrrv2Qw2dJNd0j1rG9SJNKmE

#https://korona.by/hypermarkets/promotions
#https://sosedi.by/sales/
#https://www.green-market.by/shares?ysclid=l9t0j9yfan643904217
#https://vitalur.by/actions/?ysclid=l9t0kpcdth308409329


import telebot
from telebot import types
token = '5671827929:AAG4LQR9-tPnrrv2Qw2dJNd0j1rG9SJNKmE'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    korona_btn = types.InlineKeyboardButton(text = "Акции Корона", callback_data='1')
    sosedi_btn = types.InlineKeyboardButton(text="Акции Соседи", callback_data='2')
    green_btn = types.InlineKeyboardButton(text="Акции Green", callback_data='3')
    vitalur_btn = types.InlineKeyboardButton(text="Акции Виталюр", callback_data='4')
    keyboard.add(korona_btn)
    keyboard.add(sosedi_btn)
    keyboard.add(green_btn)
    keyboard.add(vitalur_btn)
    return keyboard


#создадим декоратор
@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день, выберите торговую сеть!",
        reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open("11.jpg", "rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://korona.by/hypermarkets/promotions",
                reply_markup=keyboard)
            img.close()
        if call.data=="2":
            img = open("22.jpg", "rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://sosedi.by/sales/",
                reply_markup=keyboard)
            img.close()
        if call.data=="3":
            img = open("33.png", "rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://www.green-market.by/shares?ysclid=l9t0j9yfan643904217",
                reply_markup=keyboard)
            img.close()
        if call.data=="4":
            img = open("44.png", "rb")
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://vitalur.by/actions/?ysclid=l9t0kpcdth308409329",
                reply_markup=keyboard)
            img.close()


if __name__=="__main__":
    bot.polling(none_stop=True)

