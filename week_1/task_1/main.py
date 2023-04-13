import requests


def main(*locations):
    for place in locations:
        payload = {'nqmT': '', 'lang': 'ru'}
        url = f'https://wttr.in/{place}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main('Лондон', 'Аэропорт Шереметьево', 'Череповец')
