from settings.SETTINGS import *
from parse.Parse import Parse
from parse.dataPy import Data

@BOT.message_handler(commands=['start'])
def start_message(message):
    BOT.send_message(message.chat.id, 'Выбери интересующую тебя валюту', reply_markup=KEYBOARD_START)

@BOT.message_handler(commands=['help'])
def help_message(message):
    BOT.send_message(message.chat.id, 'Напиши пожалуйста /start и выбери валюту, которая тебя интересует!', reply_markup=create_keyboard().row(BUTTON_START))

# получения сообщений
@BOT.message_handler(content_types=['text'])
def get_text_message(message):

    global site, values

    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_RUB:
        site = Parse(URL_RUB).get_content()
        values = Data(site)
        BOT.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_ALL_LIST:
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        BOT.send_message(message.chat.id, values.get_best_buy_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_SELL_VALUE:
        BOT.send_message(message.chat.id, values.get_best_sell_value(), reply_markup=KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)

    elif message.text == BUTTON_HELP:
        help_message(message)

    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю! Напиши пожалуйста /help', reply_markup=create_keyboard().row(BUTTON_HELP))

BOT.polling()

