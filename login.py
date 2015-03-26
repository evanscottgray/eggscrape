import requests
from bs4 import BeautifulSoup

USER = ''
PASS = ''


def get_requests_client():
    client = requests.session()
    LOGIN_URL = 'https://egghead.io/users/sign_in'
    login_page = client.get(LOGIN_URL)
    html = login_page.text
    input_tag = BeautifulSoup(html).find('input',
                                         attrs={'name': 'authenticity_token'})
    csrftoken = input_tag['value']
    data = {'user[email]': USER,
            'user[password]': PASS,
            'authenticity_token': csrftoken,
            'commit': 'Sign in'}
    headers = {'Referrer': 'https://egghead.io/users/sign_in',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'text/html',
               'Origin': 'https://egghead.io'}
    client.post(LOGIN_URL,
                data=data,
                headers=headers,
                cookies=login_page.cookies)
    return client
