from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token
from aiogram.dispatcher.filters import Text

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# Это первоначальный опрос пользователя, чтобы узнать какую он информацию хочет получить
@dp.message_handler(Text(equals=['/start', 'Назад', 'Вернуться к выбору информации']))
async def start(message: types.Message):
    select_buttons = ['Учебные программы', 'Немного информации об иннополисе']
    keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_start.add(*select_buttons)

    await message.answer("Добро пожаловать в нашего телеграм бота!\n"
                         "С помощью этого бота вы сможете узнать всю нужную информацию для поступления в Иннополис!\n"
                         "По различным учебным программам, а также немного информации об обучении в иннополисе",
                         reply_markup=keyboard_start)


# Эта функция создана для того, чтобы пользователь мог выбрать по какой учебной программе он получит информацию
@dp.message_handler(Text(equals=['Учебные программы', 'Вернуться к учебным программам']))
async def choice_study_programs(message: types.Message):
    select_buttons = ['Бакалавриат', 'Магистратура', 'Аспирантура', 'Назад']
    keyboard_study_programs = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_study_programs.add(*select_buttons)

    await message.answer(
        'Выберите одну из предложенных учебных программ, чтобы узнать о ней подробней или нажмите кнопку назад',
        reply_markup=keyboard_study_programs)

    # Эта функция выдаёт информацию об Бакалавриате в иннополисе
    @dp.message_handler(Text(equals="Бакалавриат"))
    async def undergraduate(message: types.Message):
        select_buttons = ['Вернуться к учебным программам', 'Вернуться к выбору информации']
        keyboard_buttons_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_buttons_back.add(*select_buttons)
        await message.answer('Здесь будет информация о Бакалавриате', reply_markup=keyboard_buttons_back)

    # Эта функция выдаёт информацию об Магистратуре в иннополисе
    @dp.message_handler(Text(equals="Магистратура"))
    async def magistracy(message: types.Message):
        select_buttons = ['Вернуться к учебным программам', 'Вернуться к выбору информации']
        keyboard_buttons_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_buttons_back.add(*select_buttons)
        await message.answer('Здесь будет информация о Магистратуре', reply_markup=keyboard_buttons_back)

    # Эта функция выдаёт информацию об Аспирантуре в иннополисе
    @dp.message_handler(Text(equals="Аспирантура"))
    async def graduate_school(message: types.Message):
        select_buttons = ['Вернуться к учебным программам', 'Вернуться к выбору информации']
        keyboard_buttons_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_buttons_back.add(*select_buttons)
        await message.answer('Здесь будет информация о Аспирантуре', reply_markup=keyboard_buttons_back)


# Эта функция создана для выбора информации об иннополисе
@dp.message_handler(Text(equals="Немного информации об иннополисе"))
async def study_information(message: types.Message):
    select_buttons = ["Об учебе в иннополисе", "Об платном обучении", "Олимпиадные бонусы", "Часто задаваемые вопросы",
                      "Отбор в университет", "Назад"]
    keyboard_study_information = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_study_information.add(*select_buttons)
    await message.answer('Выберите информацию которую хотели бы узнать', reply_markup=keyboard_study_information)

    @dp.message_handler(Text(equals="Об учебе в иннополисе"))
    async def about_study(message: types.Message):
        await message.answer('что-то про иннополис')

    @dp.message_handler(Text(equals="Об платном обучении"))
    async def about_study(message: types.Message):
        await message.answer('Об платном обучении')

    @dp.message_handler(Text(equals="Олимпиадные бонусы"))
    async def about_study(message: types.Message):
        await message.answer('Олимпиадные бонусы')

    @dp.message_handler(Text(equals="Часто задаваемые вопросы"))
    async def about_study(message: types.Message):
        await message.answer('Часто задаваемые вопросы')

    @dp.message_handler(Text(equals="Отбор в университет"))
    async def about_study(message: types.Message):
        await message.answer("Отбор в университет")


if __name__ == '__main__':
    executor.start_polling(dp)
