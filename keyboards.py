from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Привет! 👋')
button_ym = KeyboardButton('Что ты умеешь? 🤔')
button_keyboardss = KeyboardButton('Клавиатура (только для админов)')
button_back = KeyboardButton('Назад')


button_info = KeyboardButton('Информация о командах')

button_ras = KeyboardButton('Рассылка')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(button_hi)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(button_ym).add(button_info).add(button_hi)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_ym).add(button_keyboardss).add(button_hi)
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).add(button_ras).add(button_info)





inline_btn_1 = InlineKeyboardButton('Что ты умеешь? 🤔', callback_data='button1')

inline_btn_2 = InlineKeyboardButton('Рассылка(/sendall)', callback_data='button2')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)


