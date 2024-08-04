from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

BOT = Bot('5928793004:AAFJIdCONY9xVLMuVjhkVUIzJzSVo43epZQ')
dp = Dispatcher()
users = {}
stages = ['''
     --------
     |      |
     |      0
     |     \\|/
     |      |
     |     / \\
     -
     ''',
     '''
     --------
     |      |
     |      0
     |     \\|/
     |      |
     |     /
     -
     ''',
     '''
     --------
     |      |
     |      0
     |     \\|/
     |      |
     |     
     -
     ''',
     '''
     --------
     |      |
     |      0
     |     \\|
     |      |
     |
     -
     ''',
     '''
     --------
     |      |
     |      0
     |      |
     |      |
     |
     -
     ''',
     '''
     --------
     |      |
     |      0
     |     
     |      
     |     
     -
     ''',
     '''  
     --------
     |      |
     |      
     |     
     |      
     |     
     -
     '''
     ]
def random_word():
    with open('words_for_viselica.txt', 'r') as file:
        words_lst = [i.strip() for i in file.readlines()]
        word = random.choice(words_lst)
        return word

button_agree = KeyboardButton(text='Да✅')
button_disagree = KeyboardButton(text='Нет❌')
keyword1 = ReplyKeyboardMarkup(keyboard=[[button_agree], [button_disagree]])

@dp.message(Command(commands=['start']))
async def start_func(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {'wins': 0,
                                       'fails': 0,
                                       'total': 0,
                                       'status': False,
                                       'word': '',
                                       'tries': 0,
                                       'letters': []}
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в игру "Угадайка слов"! Вы хотите начать игру?', reply_markup=keyword1)

@dp.message(Command(commands=['stat']))
async def stat_func(message: Message):
    await message.answer(f'Всего сыграно игр: {users[message.from_user.id]["total"]}\n'
                         f'Кол-во поражений: {users[message.from_user.id]["fails"]}\n'
                         f'Кол-во побед: {users[message.from_user.id]["wins"]}\n'
                         f'Хотите начать новую игру?')


@dp.message(Command(commands=['info']))
async def info_func(message: Message):
    await message.answer(f'------------ПРАВИЛА-------------\n'
                         f'Угадайка слов - игра, в которой вам нужно угадывать различные слова.\n'
                         f'Ход игры:\n'
                         f' 1) Вы получаете количество букв в загаданном слове.\n'
                         f' 2) Угадываете слово по буквам.\n '
                         f' 3) Если ошибётесь 7 раз - проиграете.\n'
                         f'----------ВСЕ КОМАНДЫ---------\n'
                         f'/stat - для просмотра статистики игрока.\n'
                         f'/cancel - для выхода из игры.\n'
                         f'/info - для просмотра информации об игре.\n'
                         f'/start - для запуска бота.\n'
                         f'"нет", "не хочу", "не хочу играть" - для отклонения запроса на игру.\n'
                         f'"да", "хочу", "хочу играть", "играть", "игра" - для начала игры.\n'
                         f'-----------Удачной игры!---------.')

@dp.message(Command(commands=['cancel']))
async def cancel_func(message: Message):
    if users[message.from_user.id]['status']:
        users[message.from_user.id]['status'] = False
        users[message.from_user.id]['total'] += 1
        await message.answer(f'Вы вышли из игры! Загаданное слово было: {users[message.from_user.id]["word"]}\n'
                             f'Если захотите сыграть еще раз, то напишите мне "играть"')
    else:
        await message.answer('Ошибка, вы еще не в игре! Хотите начать игру?')

@dp.message(F.text.strip().lower().in_(['нет', 'не хочу', 'не хочу играть', 'Нет❌']))
async def decline_game_func(message: Message):
    if not users[message.from_user.id]['status']:
        await message.answer('Очень жаль! Если захотите поиграть, то напишите мне "играть"', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Вы уже находитесь в игре! Если хотите выйти из игры, то используйте команду /cancel', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text.strip().lower().in_(['да', 'хочу', 'хочу играть', 'играть', 'игра', 'да✅']))
async def accept_game_func(message: Message):
    if not users[message.from_user.id]['status']:
        users[message.from_user.id]['status'] = True
        users[message.from_user.id]['tries'] = 7
        users[message.from_user.id]['word'] = random_word().lower()
        users[message.from_user.id]['letters'] = ['_' for i in range(len(users[message.from_user.id]['word']))]
        await message.answer(f'Игра началась! У вас есть 7 попыток чтобы отгадать слово.\n'
                             f'Текущее состояние человечка: \n'
                             f'{stages[users[message.from_user.id]["tries"]-1]}\n'
                             f'Загаданное слово: {" ".join(users[message.from_user.id]["letters"])}', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text.strip().lower().isalpha())
async def guessing_game_func(message: Message):
    if len(message.text) > 1:

        if message.text.lower() == users[message.from_user.id]['word']:
            users[message.from_user.id]["wins"] += 1
            users[message.from_user.id]['total'] += 1
            users[message.from_user.id]['status'] = False
            await message.answer(f'Поздравляем, Вы выиграли!\n'
                                 f'Ваше загаданное слово было: {users[message.from_user.id]["word"]}\n'
                                 f'Финальное состояние человечка:\n {stages[users[message.from_user.id]["tries"]-1]}\n'
                                 f'Хотите сыграть еще?')
        else:
            users[message.from_user.id]['tries'] -= 1
            if users[message.from_user.id]['tries'] == 0:
                users[message.from_user.id]['total'] += 1
                users[message.from_user.id]['fails'] += 1
                users[message.from_user.id]['status'] = False
                await message.answer(f'К сожалению, вы проиграли!\n'
                                     f'Ваше загаданное слово было: {users[message.from_user.id]["word"]}\n'
                                     f'Финальное состояние человечка: {stages[users[message.from_user.id]["tries"]-1]}\n'
                                     f'Хотите сыграть еще?')
            else:
                await message.answer(f'Вы не угадали слово! Может стоит попробовать по буквам?\n'
                                     f'{"".join(users[message.from_user.id]["letters"])}\n'
                                     f'Текущее состояние человечка:\n'
                                     f'{stages[users[message.from_user.id]["tries"]-1]}')
    else:

        if message.text.lower() in users[message.from_user.id]['letters']:
            await message.answer(f'Вы уже угадали эту букву, попробуйте угадать другие.\n'
                                 f'{" ".join(users[message.from_user.id]["letters"])}\n'
                                 f'Текущее состояние человечка:\n'
                                 f'{stages[users[message.from_user.id]["tries"]-1]}')

        elif message.text.lower() not in users[message.from_user.id]['letters'] and message.text.lower() in users[message.from_user.id]['word']:
            for let in range(len(users[message.from_user.id]['word'])):
                if users[message.from_user.id]['word'][let] == message.text.lower():
                    users[message.from_user.id]['letters'][let] = message.text.lower()
            if "".join(users[message.from_user.id]["letters"]) == users[message.from_user.id]['word']:
                users[message.from_user.id]['total'] += 1
                users[message.from_user.id]['wins'] += 1
                users[message.from_user.id]['status'] = False
                await message.answer(f'Поздравляем, Вы выиграли!\n'
                 f'Ваше загаданное слово было: {users[message.from_user.id]["word"]}\n'
                 f'Финальное состояние человечка:\n {stages[users[message.from_user.id]["tries"] - 1]}\n'
                 f'Хотите сыграть еще?')
            else:
                await message.answer(f'Вы угадали букву!\n'
                                 f'{" ".join(users[message.from_user.id]["letters"])}\n'
                                 f'Текущее состояние человечка:\n'
                                 f'{stages[users[message.from_user.id]["tries"]-1]}')

        else:
            users[message.from_user.id]['tries'] -= 1
            if users[message.from_user.id]['tries'] == 0:
                users[message.from_user.id]['total'] += 1
                users[message.from_user.id]['fails'] += 1
                users[message.from_user.id]['status'] = False
                await message.answer(f'К сожалению, вы проиграли!\n'
                                     f'Ваше загаданное слово было: {users[message.from_user.id]["word"]}\n'
                                     f'Финальное состояние человечка: {stages[users[message.from_user.id]["tries"]-1]}\n'
                                     f'Хотите сыграть еще?')
            else:
                await message.answer(f'Вы не угадали букву! Попробуйте еще раз.\n'
                                     f'{" ".join(users[message.from_user.id]["letters"])}\n'
                                     f'Текущее состояние человечка:\n'
                                     f'{stages[users[message.from_user.id]["tries"]-1]}')

@dp.message()
async def others_func(message: Message):
    await message.answer(f'Я не понимаю ваше сообщение. Для просмотра доступных команд используйте /info')

if __name__ == '__main__':
    dp.run_polling(BOT)