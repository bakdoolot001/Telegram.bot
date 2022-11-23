# SECONDBOT
import telebot

bot = telebot.TeleBot("5805505422:AAFupvy59POJ2h10anm69TIPBJ425kk-hlk")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет давай поиграем, задавай мне вопросы!", parse_mode='html')


@bot.message_handler()
def name(message):
    if message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "Меня зовут BakuSecondBot", parse_mode='html')
    elif message.text == "Сколько тебе лет?":
        bot.send_message(message.chat.id, "Меня создали вчера", parse_mode='html')
    elif message.text == "Откуда ты?":
        bot.send_message(message.chat.id, "Я из Телеграмма", parse_mode='html')
    elif message.text == "photo":
        photo = open('index.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Где ты?":
        bot.send_message(message.chat.id, "Я в Телеграмме", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)