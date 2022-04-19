import requests


def fact():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    response.raise_for_status()

    result = response.json().get('value', 'Error')
    return result
