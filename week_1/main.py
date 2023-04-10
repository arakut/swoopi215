import requests


locations = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']
for place in locations:
    url = f'https://wttr.in/{place}?nqmT&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
    print('-'*75)
