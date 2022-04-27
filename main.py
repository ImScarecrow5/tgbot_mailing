from aiogram import Bot, Dispatcher, executor, types
from config import Token, admin_ip
from db import Database
import keyboards as kb


bot = Bot(Token)
dp = Dispatcher(bot)
db = Database('dbras.db')

admin1 = -1


@dp.message_handler(commands=['addadmin'])
async def start(message: types.Message):
    global admin1
    if message.chat.type == 'private':
        if message.from_user.id == admin_ip:
            text1 = message.text[10:]
            if admin_ip == text1:
                await bot.send_message(message.from_user.id, 'Извинте, но этот человек уже админ!')
            else:
                if admin1 == -1:
                    admin1 = int(text1)
                    await bot.send_message(message.from_user.id, text1 + ' теперь админ')
                    await bot.send_message(text1, 'Вы теперь админ')


@dp.message_handler(commands=['info'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Я телеграмм бот, рассылающий сообщения :)')


@dp.message_handler(commands=['whoadmin'])
async def start(message: types.Message):
    global admin1
    if message.chat.type == 'private':
        if admin1 > -1:
            admins = str(admin_ip) + ' - Главный админ, ' + str(admin1) + ' - обычный админ'
            await bot.send_message(message.from_user.id, admins)
        else:
            admins = str(admin_ip) + ' - Главный админ'
            await bot.send_message(message.from_user.id, admins)


@dp.message_handler(commands=['keyboard'])
async def ras(message: types.Message):
    global admin1
    if message.chat.type == 'private':
        if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
            await message.reply("admin panel", reply_markup=kb.markup3)
        else:
            await message.reply("клавиатура", reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['sendall'])
async def ras(message: types.Message):
    global admin1
    if message.chat.type == 'private':
        if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
            text1 = message.text[9:]
            users = db.get_users()
            for row in users:
                user_ras = False
                try:
                    await bot.send_message(row[0], text1)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, "Успешная рассылка")
            print('ID Пользователя: ' + str(message.from_user.id) + ', разослал сообщение: ' + str(text1))



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            print(str(message.from_user.id) + ' подключился к боту')
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("Добро пожаловать!", reply_markup=kb.markup3)
            else:
                await message.reply("Добро пожаловать!", reply_markup=kb.greet_kb)
        else:
            await bot.send_message(message.from_user.id, 'Мы уже вас зарегистрировали, не нужно жмать сюда')
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("Добро пожаловать!", reply_markup=kb.markup3)
            else:
                await message.reply("Добро пожаловать!", reply_markup=kb.greet_kb)


@dp.message_handler(content_types=['text'])
async def que(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Назад':
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("Хорошо", reply_markup=kb.markup3)
            else:
                await message.reply("Хорошо", reply_markup=kb.greet_kb1)
        if message.text == 'Привет! 👋':
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("И тебе привет", reply_markup=kb.markup3)
            else:
                await message.reply("И тебе привет", reply_markup=kb.greet_kb1)
        if message.text == 'Информация о командах':
            if message.from_user.id == admin_ip:
                await message.reply("Сейчас предоставлю", reply_markup=kb.markup3)
                await bot.send_message(message.from_user.id, '/sendall - разослать сообщение (команда + сообщение)')
                await bot.send_message(message.from_user.id, '/whoadmin - узнать кто админ')
                await bot.send_message(message.from_user.id, '/addadmin - добавить админа (макс. 1, команда + id)')
                await bot.send_message(message.from_user.id, '/deleteadmin - добавить админа (команда + id)')
                await bot.send_message(message.from_user.id, '/info - информация о боте')
                await bot.send_message(message.from_user.id, '/keyboard - клавиатура')
            elif message.from_user.id == admin1:
                await message.reply("Сейчас предоставлю", reply_markup=kb.markup3)
                await bot.send_message(message.from_user.id, '/sendall - разослать сообщение (команда + сообщение)')
                await bot.send_message(message.from_user.id, '/whoadmin - узнать кто админ')
                await bot.send_message(message.from_user.id, '/info - информация о боте')
                await bot.send_message(message.from_user.id, '/keyboard - клавиатура')
            else:
                await message.reply("Сейчас предоставлю", reply_markup=kb.greet_kb1)
                await bot.send_message(message.from_user.id, '/whoadmin - узнать кто админ')
                await bot.send_message(message.from_user.id, '/info - информация о боте')
                await bot.send_message(message.from_user.id, '/keyboard - клавиатура')
        if message.text == 'Что ты умеешь? 🤔':
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("Я телеграмм бот, рассылающий сообщения :)", reply_markup=kb.markup3)
            else:
                await message.reply("Я телеграмм бот, рассылающий сообщения :)", reply_markup=kb.greet_kb1)
        if message.text == 'Клавиатура (только для админов)':
            if message.from_user.id == admin_ip or admin1 > -1 and message.from_user.id == admin1:
                await message.reply("Чем займемся сегодня?", reply_markup=kb.markup3)
            else:
                await message.reply("Вы не админ", reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['deleteadmin'])
async def start(message: types.Message):
    global admin1
    if message.chat.type == 'private':
        if message.from_user.id == admin_ip:
            text1 = message.text[13:]
            if int(admin1) == text1:
                await bot.send_message(message.from_user.id, text1 + ' Вы успешно удалили из админов')
                await bot.send_message(text1, 'Вы теперь не админ :(')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
