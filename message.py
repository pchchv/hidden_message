import telebot
import string
import random


key = open('key.txt').read()
bot = telebot.TeleBot(key)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Получить сообщение', 'Отправить сообщение')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "С помощью этого бота можно отправит анонимное сообщение которое самоуничтожится после прочтения.\
                                       \nВ ответ на сообщение бот вернёт пароль для получения сообщения",\
                                        reply_markup = keyboard1)

@bot.message_handler(content_types=['text'])
def passwordgeneration(message):
    if message.text.lower() == 'получить сообщение':
        bot.send_message(message.chat.id, 'Для получения сообщения необходим пароль')
    elif message.text.lower() == 'отправить сообщение':
        symbols = string.ascii_letters + string.digits
        password = ''.join(random.sample(symbols, random.randint(15,40)))
        bot.send_message(message.chat.id, password)

bot.polling()
