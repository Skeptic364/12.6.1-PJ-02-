import requests
import json
from config import keys, headers



class ConvertionException(Exception):
    pass

class ConventerV:
    @staticmethod
    def convertCon(quote: str, base: str, amount: str):




        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')


        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')


        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')


        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.request("GET", f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from=\
{quote_ticker}&amount={amount}", headers=headers)
        total_base = json.loads(r.content).get('result')

        return total_base
