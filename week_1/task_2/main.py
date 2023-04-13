import requests

TOKEN = ''


def shorten_link(token, url):
    main_url = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        'long_url': f'{url}',
    }

    response = requests.post(main_url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json().get("id")
    return f'{bitlink}'


def count_clicks(token, user_url):
    main_url = f'https://api-ssl.bitly.com/v4/bitlinks/{user_url}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        'long_url': f'{user_url}',
    }

    response = requests.get(main_url, headers=headers)
    response.raise_for_status()
    clicks = response.json().get('total_clicks')
    return f'All amounts of clicks: {clicks}'


def is_bitlink(url):
    if 'bit.ly' in url:
        return count_clicks(TOKEN, url)
    return shorten_link(TOKEN, url)


if __name__ == '__main__':
    try:
        print(shorten_link(TOKEN, input('Enter your link: ')))
    except requests.exceptions.HTTPError:
        print('Something went wrong with your link.')

    try:
        print(count_clicks(TOKEN, input('Enter your bitlink: ')))
    except requests.exceptions.HTTPError:
        print('Something went wrong with your bitlink.')

    try:
        print(is_bitlink(input('Enter your url: ')))
    except requests.exceptions.HTTPError:
        print('Your link is incorrect.')
