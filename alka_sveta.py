import random, os
import telebot
from random import randrange

bot = telebot.TeleBot('5475668858:AAHvpNVS2_iyN7d9Ljk-3j2GQ-D3-n2YHQc')

bad = ['Дура', 'Скотина', 'Тварь', 'Центнер', 'Свиноматка', 'Корыто', 'Вафля', 'Пончик', 'Корова', 'Кабан', 'Сопля', 'Горбатая Гора']
good = ['Умница', 'Золото', 'Самородок', 'Брилиант', 'Добрая', 'Заботливая', 'Люблю ее']

sveta = ['Света', 'Светуля', 'Светланка', 'Светуня', 'Светуся', 'Светуха', 'Светуша', 'Вета', 'Лана', 'Светланочка', 'Светик', 'Светачка', 'Светка', 'Светочка', 'Светусик']
alla = ['Алка', 'Ала', 'Аля', 'Алюня', 'Алюся', 'Аллочка', 'Алла', 'Алло']

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, f'Welcome, {message.from_user.first_name}')
    bot.send_message(-1001524218927, f'New subcribe!!!\nName: {message.from_user.first_name}\nID: @{message.from_user.username}')

@bot.message_handler(commands=['photo'])
def photo(message):
    photo = open('Art/' + random.choice(os.listdir('Art')), 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def svet_alka(message):
    if message.text in sveta:
        bot.send_message(message.chat.id, f'{bad[randrange(len(bad))]}')
    if message.text in alla:
        bot.send_message(message.chat.id, f'{good[randrange(len(good))]}')


bot.polling(none_stop=True)