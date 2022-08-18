#  respect memory, import only what you need
from requests import get
from json import loads

ValueError_TEXT = "Please enter a sensible value."
TEXT_4 = "Checking the cache..."
TEXT_5 = "Oh! It is in the cache!"
TEXT_6 = "Sorry, but it is not in the cache!"
TEXT_7 = "You received"


def currency_converter_v6():
    exchange_data = {}
    owned_currency = get_input(out_type=str).lower()
    for currency in ["usd", "eur"]:
        if currency == owned_currency:
            pass
        else:
            exchange_data[currency] = get_exchange_data(owned_currency, currency)

    while True:
        target_currency = get_input(out_type=str).lower()
        if not target_currency:
            break
        currency_amount = get_input()
        print(TEXT_4)

        if target_currency in exchange_data.keys():
            print(TEXT_5)
        else:
            print(TEXT_6)
            exchange_data[target_currency] = get_exchange_data(owned_currency, target_currency)
        
        final_amount = round(currency_amount * exchange_data[target_currency]['rate'], 2)
        print(TEXT_7, final_amount, f'{target_currency.upper()}.')


def get_exchange_data(owned_currency, target_currency):
    """Returns exchange_data dictionary for selected target_currency on basis of the owned_currency"""
    url = f"http://www.floatrates.com/daily/{owned_currency}.json"
    response = loads(get(url).content)
    return response[target_currency]


def get_input(input_text="", out_type=float):
    """Returns requested type from user input (using the input_text for input query).
    Uses a simple loop to avoid ValueErrors."""
    input_as_type = None
    while True:
        try:
            input_as_type = out_type(input(input_text))
        except ValueError:
            print(ValueError_TEXT)
            pass
        return input_as_type


currency_converter_v6()
