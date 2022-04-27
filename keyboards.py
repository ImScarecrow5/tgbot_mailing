from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_hi = KeyboardButton('Привет! 👋')
button_ym = KeyboardButton('Что ты умеешь? 🤔')
button_keyboardss = KeyboardButton('Клавиатура (только для админов)')
button_back = KeyboardButton('Назад')

button_info = KeyboardButton('Информация о командах')


greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(button_ym).add(button_info).add(button_hi)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_ym).add(button_info).add(button_hi)
