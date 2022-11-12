import requests

class Session:
    _base_url = "https://ohmanda.com/api/horoscope/"

    @classmethod
    def begin(cls):
        print("\n** Welcome to Daily Scope! **\n")
        while True:
            user_input = input("""Enter your sign to read today's horoscope.
You can also enter 'done' to exit or 'zodiac' to see available signs.

I'm waiting: """)
            if user_input in Zodiac.get_signs():
                horoscope = cls.get_horoscope(user_input)
                print("\n** " + horoscope["sign"] + " - " + horoscope["date"] + " **")
                print("\n" + horoscope["horoscope"] + "\n")

            elif user_input == "done":
                break
            elif user_input == "zodiac":
                print("\n================")
                for sign in Zodiac.get_signs():
                    print("- " +sign)
                print("================\n")
    
    @classmethod
    def get_horoscope(cls, sign):
        response = requests.get(cls._base_url + sign)
        return response.json()


class Zodiac:
    _signs = [
        "aries",
        "taurus",
        "gemini",
        "cancer",
        "leo",
        "virgo",
        "libra",
        "scorpio",
        "sagittarius",
        "capricornus",
        "aquarius",
        "pisces"
    ]

    @classmethod
    def get_signs(cls):
        return cls._signs
    
Session.begin()