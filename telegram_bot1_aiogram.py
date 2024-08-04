from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import requests

BOT = Bot('6870654449:AAH5VSfXmALYnVDbFWayDNux6iP6QhbXk8E')
dp = Dispatcher()

@dp.message(F.text.lower().strip().in_(['привет']))
async def hello_func(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text.lower().strip().in_(['как дела']))
async def how_are_you_func(message: Message):
    await message.answer(f'У меня все отлично! Спасибо, что '
                             f'интересуешься, {message.from_user.first_name} <3')

@dp.message(F.text.lower().strip().in_(['пока']))
async def bye_func(message: Message):
    await message.answer(f'Уже уходишь! Обращайся ко мне еще, '
                    f'до встречи, {message.from_user.first_name}!')

@dp.message(F.text.lower().strip().isdigit())
async def numbers_func(message: Message):
    num = message.text.strip()
    request = requests.get(url=f'http://numbersapi.com/#{num}')
    answer = request.text
    await message.answer('Интересный факт о числе '
                             f'{num}:\n{answer}')

@dp.message(F.text.lower().strip().in_(['погода']))
async def weather_func(message: Message):
    key = '540b568316e707775ca72fdc3a35dc28'
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=11.8696&lon=80.3610&appid={key}').json()
    temperature = request['main']['temp']
    feels_like = request['main']['feels_like']
    weather = request['weather']['main']
    await message.answer(f'Температура: {temperature}\nОщущается как: {feels_like}\nПогода: {weather}')
@dp.message(F.text.lower().strip().in_(['мои координаты']))
async def coordinates_func(message: Message):
    request = requests.get('http://api.open-notify.org/iss-now.json').json()
    latitude = request['iss_position']['latitude']
    longitude = request['iss_position']['longitude']
    await message.answer(f'Ваши координаты:\nШирота: {latitude}\nДолгота: {longitude}')

@dp.message(F.text.lower().strip().in_(['картинки']))
async def pictures_func(message: Message):
    await message.answer('Картинку с каким животным вы хотите?(собака/лиса/кошка)')

@dp.message(F.text.lower().strip().in_(['лиса', 'собака', 'кошка']))
async def type_animal(message1: Message):
    if message1 == 'лиса':
        request = requests.get('https://randomfox.ca/floof/').json()
        url = request['image']
        await message1.answer_photo(url)
    elif message1 == 'собака':
        request = requests.get('https://random.dog/woof.json').json()
        url = request['url']
        await message1.answer_photo(url)
    elif message1 == 'кошка':
        request = requests.get('https://api.thecatapi.com/v1/images/search').json()
        url = request['url']
        await message1.answer_photo(url)

if __name__ == '__main__':
    dp.run_polling(BOT)




