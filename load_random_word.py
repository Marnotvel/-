import random
import requests
from requests import get

from BasicWord import BasicWord


def load_random_word():
    data = get('https://api.npoint.io/f7d4d7be481bd574d10f').json()
    random_word = random.choice(data)
    return BasicWord(random_word['word'], random_word['subwords'])
