import requests

BASE_URL = "https://ohmanda.com/api/horoscope/"

signs = [
    "aquarius",
    "pisces",
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
]

response = requests.get(BASE_URL + "scorpio")

print(response.json())
