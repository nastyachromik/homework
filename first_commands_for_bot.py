import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

API_URL = 'https://api.telegram.org/bot'
token = '6870654449:AAH5VSfXmALYnVDbFWayDNux6iP6QhbXk8E'
MAX_COUNTER = 100
counter = 0
offset = -2


while counter < MAX_COUNTER:
    response = requests.get(url=f'{API_URL}{token}/getUpdates?offset={offset + 1}').json()

    if response['result']:
        req = response['result'][0]['message']['text']
        name = response['result'][0]['message']['from']['first_name']
        chat_id = response['result'][0]['message']['chat']['id']
        offset = response['result']['update_id']

        if 'привет' in req.lower().strip():
            requests.get(url=f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Привет, {name}!')

        elif 'как дела' in req.lower().strip():
            requests.get(url=f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=У меня все отлично! Спасибо, что '
                             f'интересуешься, {name} <3')

        elif 'пока' in req.lower().strip():
            requests.get(
                url=f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Уже уходишь! Обращайся ко мне еще, '
                    f'до встречи, {name}!')

        elif req.strip().isdigit():
            new_request = requests.get(url=f'http://numbersapi.com/#{req.strip()}')
            answer = new_request.json()
            requests.get(url=f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Интересный факт о числе '
                             f'{req.strip()}:\n{answer}')

        elif 'мои координаты' in req.strip():
            new_request = requests.get(url=f'http://api.open-notify.org/iss-now.json').json()
            latitude = new_request['iss_position']['latitude']
            longitude = new_request['iss_position']['longitude']
            requests.get(
                f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Ваши координаты:\nШирота: {latitude}\nДолгота: {longitude}')

        elif 'погода' in req.strip():
            requests.get(
                f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=В каком городе вы находитесь?')
            while True:
                response = requests.get(url=f'{API_URL}{token}/getUpdates?offset={offset + 1}').json()
                if response['result']:
                    offset = response['result']['update_id']
                    city = response['result'][0]['message']['text']
                    break
            driver = webdriver.Chrome()
            driver.get(url='https://www.gismeteo.ru/')
            button = driver.find_element(By.CLASS_NAME('input js-input'))
            try:
                button.send_keys(f'{city.strip()}')
                weather = driver.find_element(By.CLASS_NAME, 'weather-value').text
                requests.get(
                    f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Погода в городе {city} сейчас: {weather}')
            except:
                requests.get(
                    f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text=Вероятно, такого города не существует(')
        else:
            message = 'Вы ввели некорректную команду. Список доступных команд:\n1) Привет\n2) Пока\n3) Как дела?\n4)Мои координаты\n5) Погода'
            requests.get(
                f'{API_URL}{token}/sendMessage?chat_id={chat_id}&text={message}')

    counter += 1
    time.sleep(1)