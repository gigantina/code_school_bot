#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
                     f'''Привет! Я Парламент.Бот от Школьного Самоуправления. В следующем году у меня появится много интересных функций. Сейчас, с моей помощью можно пройти Ученическую Оценку Преподавания. Ученическая Оценка Преподавания — это новый проект Школьного Самоуправления, созданный для анализа удовлетворённости учеников образованием. 
Вам предстоит пройти опрос, который займёт примерно 20 минут. Участие в нем абсолютно анонимно, ответы будут переданы в обобщённом виде только администрации и непосредственно учителям, которых вы будете оценивать. Поэтому можете не беспокоиться и отвечать абсолютно честно и непредвзято. Для прохождения  УОПа нажмите кнопку «Регистрация»''',
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
            bot.send_message(chat, 'Напишите ФИО')
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
                         '''Ученическая Оценка Преподавания — это новый проект Школьного Самоуправления, созданный для анализа удовлетворённости учеников образованием. 
Вам предстоит пройти опрос, который займёт примерно 20 минут. Участие в нем абсолютно анонимно, ответы будут переданы в обобщённом виде только администрации и непосредственно учителям, которых вы будете оценивать. Поэтому можете не беспокоиться и отвечать абсолютно честно и непредвзято. Для прохождения  УОПа нажмите кнопку «Регистрация». Исходный код бота можно посмотреть по ссылке: https://github.com/gigantina/code_school+bot''',
                         reply_markup=default())


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
