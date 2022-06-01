from telebot import types
from base import *


def get_text_markup(markup):
    return [i[0]['text'] for i in markup.keyboard]


def default():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Регистрация"))
    markup.add(types.KeyboardButton("Помощь❓"))

    return markup