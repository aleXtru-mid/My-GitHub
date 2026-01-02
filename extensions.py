import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert (quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException("Вы ввели одинаковую валюту, повторите запрос:")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Вы неправильно ввели название валюты {quote}, повторите запрос:")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Вы неправильно ввели название валюты {base}, повторите запрос:")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Вы неправильно ввели количество валюты {amount}, повторите запрос:")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
