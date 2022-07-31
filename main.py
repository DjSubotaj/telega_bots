import telebot
from telebot import types

bot = telebot.TeleBot('5475668858:AAHvpNVS2_iyN7d9Ljk-3j2GQ-D3-n2YHQc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name}, your ip: {message.from_user.last_name}'
    bot.send_message(-1001524218927, mess)

#@bot.message_handler()
#def get_user_text(message):
#    if message.text == 'adelina':
#        photo = open('adelina.jpg', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    elif message.text == 'alina':
#        bot.send_message(message.chat.id,'Samaya krasivaya na svete')
#    else:
#        bot.send_message(message.chat.id, message, parse_mode='html')

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, 'Что за хуйня?')

@bot.message_handler(commands=['web'])
def web(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Best page in instagram', url='https://www.instagram.com/alina_gioeva/?igshid=YmMyMTA2M2Y%3D'))
    bot.send_message(message.chat.id, 'Perejdite na sait', reply_markup=markup)

@bot.message_handler(commands=['help'])
def web(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website = types.KeyboardButton('TopModel')
    start = types.KeyboardButton('start')
    markup.add(website,start)
    bot.send_message(message.chat.id, 'Perejdite na sait', reply_markup=markup)
bot.polling(none_stop=True)