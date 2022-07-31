import telebot

bot = telebot.TeleBot('5475668858:AAHvpNVS2_iyN7d9Ljk-3j2GQ-D3-n2YHQc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name}, your ip: {message.from_user.last_name}'
    bot.send_message(-1001524218927, mess)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'adelina':
        photo = open('adelina.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, message, parse_mode='html')

bot.polling(none_stop=True)