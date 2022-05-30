import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Почтовый индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
            '[Прокси]': response.get('proxy'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')



    except requests.exceprions as ConnectionError:
        print('[!] Пожалуйста проверьте подключение!')



preview_text = Figlet(font='slant')
print(preview_text.renderText('IP INFO byStax'))
ip = input('Пожалуйста,введите IP адресс: ')

get_info_by_ip(ip=ip)


