import telebot
from config import TOKEN
from markups import *
from base import *
import os, sys
import random

# level, order, new = start_values()
levels = dict()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message, res=False):
    global levels
    bot.send_message(message.chat.id,
                     f'Я на связи, {message.from_user.username}. Бот создан для получения кода для прохождения ученической оценки образования. Следуйте меню. Чтобы получить дополнительную информацию, перейдите в "Помощь"',
                     reply_markup=default())
    levels[message.from_user.id] = 0


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global levels

    m = message.text.strip()
    user = message.from_user

    chat = message.chat.id
    print(m)
    commands = ['Регистрация']

    if m == 'Регистрация':
        if isReg(user.id):
            bot.send_message(chat, 'Вы уже зарегестрированы. Ваш уникальный код находится где-то выше')

        else:
            bot.send_message(chat, 'Напишите ФИО', reply_markup=classes())
            levels[user.id] = 1

    if levels[user.id] == 1 and m not in commands:
        if isUserExists(m):
            add_user(m, user.id)
            key = random.randint(1000, 9999)
            while isKeyExists(key):
                key = random.randint(1000, 9999)
            add_key(key, m)
            link = get_link_from_name(m)

            bot.send_message(chat, 'Вы успешно зарегестрированы!')
            bot.send_message(chat, f'Поучавствуйте в оценке образования - заполните форму {link} \nВаш код - {key}')
        else:
            bot.send_message(chat, 'Ученик с таким ФИО не найден')

    if m == 'Помощь❓':
        bot.send_message(chat,
                         f'Бот создан для получения кода для прохождения ученической оценки образования. Опрос анонимен, ваше ФИО необходимо для того, чтобы мы исключили повторяющиеся прохождения. Вы можете убедиться в этом, перейдя на страницу https://github.com/gigantina/code_school_bot: \nВ файле Readme.md объясняются принципы работы бота, в том числе анонимность', reply_markup=default())


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
