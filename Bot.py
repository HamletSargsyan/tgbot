import telebot
from telebot import types

bot = telebot.TeleBot('5583191944:AAF_S4fszlCHqy7CzvfoJd5oZNXwjPhmdQo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="www.exemple.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "id":
                bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('pic.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебе не понимаю", parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="www.exemple.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)



bot.polling(non_stop=True)