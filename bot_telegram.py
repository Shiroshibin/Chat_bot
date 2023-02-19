from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token, all_commands
from aiogram.dispatcher.filters import Text
from parser import information_about_innopolis, postgraduate_studies, magistr, bakalavr
from time import localtime

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Функция для защиты от флуда
async def anti_flood(message: types.Message, *args, **kwargs):
    await message.delete()


# Это первоначальный опрос пользователя, чтобы узнать какую он информацию хочет получить
@dp.message_handler(Text(equals=['/start', 'Назад', 'Вернуться к выбору информации']))
@dp.throttled(anti_flood, rate=2)
async def start(message: types.Message):
    select_buttons = ['Учебные программы', 'Общая информация об Иннополисе']
    keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_start.add(*select_buttons)

    await message.answer("Добро пожаловать в нашего телеграм бота!\n"
                         "С помощью этого бота вы сможете узнать всю нужную информацию для поступления в Иннополис!\n"
                         "По различным учебным программам, а также немного информации об обучении в иннополисе",
                         reply_markup=keyboard_start)


# Эта функция создана для того, чтобы пользователь мог выбрать по какой учебной программе он получит информацию
@dp.message_handler(Text(equals=['Учебные программы', 'Вернуться назад']))
@dp.throttled(anti_flood, rate=2)
async def choice_study_programs(message: types.Message):
    select_buttons = ['Бакалавриат', 'Магистратура', 'Аспирантура', 'Назад']
    keyboard_study_programs = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_study_programs.add(*select_buttons)

    await message.answer(
        'Выберите одну из предложенных учебных программ, чтобы узнать о ней подробней или нажмите кнопку назад',
        reply_markup=keyboard_study_programs)

    # Эта функция выдаёт информацию об Бакалавриате в иннополисе


@dp.message_handler(Text(equals='Бакалавриат'))
@dp.throttled(anti_flood, rate=2)
async def undergraduate(message: types.Message):
    select_buttons = {'Cтруктура обучения в Бакалавриате', 'Направление подготовки в Бакалавриате',
                      'Учебные программы в Бакалавриате', 'Вернуться назад'}
    keyboard_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_select.add(*select_buttons)
    await message.answer('Выберите информацию которую хотите узнать', reply_markup=keyboard_select)


@dp.message_handler(Text(equals="Cтруктура обучения в Бакалавриате"))
@dp.throttled(anti_flood, rate=2)
async def education_schema(message: types.Message):
    with open('bakalavr/education_schema.txt', 'r', encoding="utf-8") as file_education_schema:
        await message.answer(file_education_schema.read())


@dp.message_handler(Text(equals="Направление подготовки в Бакалавриате"))
@dp.throttled(anti_flood, rate=2)
async def direction_preparation(message: types.Message):
    with open('bakalavr/direction_preparation.txt', 'r', encoding="utf-8") as file_direction_preparation:
        await message.answer(file_direction_preparation.read())


@dp.message_handler(Text(equals="Учебные программы в Бакалавриате"))
@dp.throttled(anti_flood, rate=2)
async def learning_programs(message: types.Message):
    with open('bakalavr/learning_programs.txt', 'r', encoding="utf-8") as file_learning_programs:
        await message.answer(file_learning_programs.read())


# Эта функция выдаёт информацию об Магистратуре в иннополисе
@dp.message_handler(Text(equals="Магистратура"))
@dp.throttled(anti_flood, rate=2)
async def magistracy(message: types.Message):
    select_buttons = {'Cтруктура обучения в Магистратуре', 'Направление подготовки в Магистратуре',
                      'Учебные программы в Магистратуре', 'Вернуться назад'}
    keyboard_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_select.add(*select_buttons)
    await message.answer('Выберите информацию которую хотите узнать', reply_markup=keyboard_select)


@dp.message_handler(Text(equals="Cтруктура обучения в Магистратуре"))
@dp.throttled(anti_flood, rate=2)
async def education_schema(message: types.Message):
    with open('magistr/education_schema.txt', 'r', encoding="utf-8") as file_education_schema:
        await message.answer(file_education_schema.read())


@dp.message_handler(Text(equals="Направление подготовки в Магистратуре"))
@dp.throttled(anti_flood, rate=2)
async def direction_preparation(message: types.Message):
    with open('magistr/direction_preparation.txt', 'r', encoding="utf-8") as file_direction_preparation:
        await message.answer(file_direction_preparation.read())


@dp.message_handler(Text(equals="Учебные программы в Магистратуре"))
@dp.throttled(anti_flood, rate=2)
async def learning_programs(message: types.Message):
    with open('magistr/learning_programs.txt', 'r', encoding="utf-8") as file_learning_programs:
        await message.answer(file_learning_programs.read())


# Эта функция выдаёт информацию об Аспирантуре в иннополисе
@dp.message_handler(Text(equals="Аспирантура"))
@dp.throttled(anti_flood, rate=2)
async def graduate_school(message: types.Message):
    select_buttons = {'Cтруктура обучения в Аспирантуре', 'Направление подготовки в Аспирантуре',
                      'Учебные программы в Аспирантуре', 'Вернуться назад'}
    keyboard_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_select.add(*select_buttons)
    await message.answer('Выберите информацию которую хотите узнать', reply_markup=keyboard_select)


@dp.message_handler(Text(equals='Cтруктура обучения в Аспирантуре'))
@dp.throttled(anti_flood, rate=2)
async def education_schema(message: types.Message):
    with open('postgraduate_studies/education_schema.txt', 'r', encoding="utf-8") as file_education_schema:
        await message.answer(file_education_schema.read())


@dp.message_handler(Text(equals="Направление подготовки в Аспирантуре"))
@dp.throttled(anti_flood, rate=2)
async def direction_preparation(message: types.Message):
    with open('postgraduate_studies/direction_preparation.txt', 'r', encoding="utf-8") as file_direction_preparation:
        await message.answer(file_direction_preparation.read())


@dp.message_handler(Text(equals="Учебные программы в Аспирантуре"))
@dp.throttled(anti_flood, rate=2)
async def learning_programs(message: types.Message):
    with open('postgraduate_studies/learning_programs.txt', 'r', encoding="utf-8") as file_learning_programs:
        await message.answer(file_learning_programs.read())


# Эта функция создана для выбора информации об иннополисе
@dp.message_handler(Text(equals="Общая информация об Иннополисе"))
@dp.throttled(anti_flood, rate=2)
async def study_information(message: types.Message):
    select_buttons = ["Об учебе в Иннополисе", "О городе Иннополис", "О кампусе", "О студенческой жизни",
                      "Как поступить?", "Назад"]
    keyboard_study_information = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_study_information.add(*select_buttons)
    await message.answer('Выберите информацию которую хотели бы узнать', reply_markup=keyboard_study_information)


@dp.message_handler(Text(equals="Об учебе в Иннополисе"))
@dp.throttled(anti_flood, rate=2)
async def about_study(message: types.Message):
    with open('some_info_about_inun/about_study_parser.txt', 'r', encoding="utf-8") as file_about_study_parser:
        await message.answer(file_about_study_parser.read())


@dp.message_handler(Text(equals="О городе Иннополис"))
@dp.throttled(anti_flood, rate=2)
async def about_the_city_of_innopolis(message: types.Message):
    with open('some_info_about_inun/about_the_city_of_innopolis.txt', 'r', encoding="utf-8") as file_about_the_city_of_innopolis:
        await message.answer(file_about_the_city_of_innopolis.read())


@dp.message_handler(Text(equals="О кампусе"))
@dp.throttled(anti_flood, rate=2)
async def about_campus(message: types.Message):
    with open('some_info_about_inun/about_campus.txt', 'r', encoding="utf-8") as file_about_campus:
        await message.answer(file_about_campus.read())


@dp.message_handler(Text(equals="О студенческой жизни"))
@dp.throttled(anti_flood, rate=2)
async def about_student_life(message: types.Message):
    with open('some_info_about_inun/student_life.txt', 'r', encoding="utf-8") as file_student_life:
        await message.answer(file_student_life.read())


@dp.message_handler(Text(equals='Как поступить?'))
@dp.throttled(anti_flood, rate=2)
async def how_to_go(message: types.Message):
    with open('some_info_about_inun/how_to_go.txt', 'r', encoding="utf-8") as file_how_to_go:
        await message.answer(file_how_to_go.read())


# Проверка сообщения, на то является ли оно командой или пользователь написал что-то странное
@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood, rate=2)
async def message_authentication(message: types.Message):
    if message.text in all_commands:
        pass
    else:
        select_buttons = ['Вернуться к выбору информации']
        keyboard_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_select.add(*select_buttons)
        await message.answer('Привет! Я бот для поиска информации, для поступающих в иннополис, и я понимаю только '
                             'лишь определённые команды, которые появляются у вас в виде кнопок',
                             reply_markup=keyboard_select)


if __name__ == '__main__':
    with open('state.txt', 'w') as state:
        now_time = localtime()

        state.write('Bot start in \n')
        state.write(f'Time: {str(now_time.tm_hour).rjust(2, "0")}.{str(now_time.tm_min).rjust(2, "0")}.{str(now_time.tm_sec).rjust(2, "0")}\n')
        state.write(f'Date: {str(now_time.tm_mday).rjust(2, "0")}.{str(now_time.tm_mon).rjust(2, "0")}.{now_time.tm_year}\n\n')

    executor.start_polling(dp)