#SETTINGS BOT
import telebot
TOKEN = '1437076021:AAF3lM6wpqZnqHWqkv6V9Ns7DUCjX8Euvak'
BOT = telebot.TeleBot(TOKEN)

#URLS
URL_USD = 'https://banki24.by/minsk/kurs/usd'
URL_EUR = 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
URL_UAH = 'https://banki24.by/minsk/kurs/uah'

#BUTTONS
BUTTON_START = 'В начало'
BUTTON_HELP = 'Помощь'
BUTTON_GET_ALL_LIST = 'Курсы валют всех банков'
BUTTON_BEST_BUY_VALUE = 'Вывести лучший курс для покупки'
BUTTON_BEST_SELL_VALUE = 'Вывести лучший курс для продажи'
BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'
BUTTON_UAH = 'UAH'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
    return keyboard

#Кнопки для выбора валюты
KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD,BUTTON_EUR,BUTTON_RUB)

#Кнопки для выбора курсов валют
KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST)
KEYBOARD_CHOICE.row(BUTTON_BEST_BUY_VALUE,BUTTON_BEST_SELL_VALUE)
KEYBOARD_CHOICE.row(BUTTON_START)
