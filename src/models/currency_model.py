# import os
import requests
from dotenv import load_dotenv
from flask import jsonify


load_dotenv()


def get_conversion_rate(from_currency, to_currency, amount):
    # api_key = os.getenv('API_KEY')
    currency_mapping = {
        'USD': 'usd',
        'BRL': 'brl',
        'EUR': 'eur',
        'BTC': 'bitcoin',
        'ETH': 'ethereum'
    }

    from_currency_id = currency_mapping.get(from_currency.upper())
    to_currency_id = currency_mapping.get(to_currency.upper())

    if not from_currency_id or not to_currency_id:
        raise ValueError(
            f'Invalid currency code:'
            f'{from_currency if not from_currency_id else to_currency}'
        )

    url = (
        f'https://api.coingecko.com/api/v3/simple/price'
        f'?ids={from_currency}&vs_currencies={to_currency}'
        )

    response = requests.get(url)
    data = response.json()

    # Verifique se a resposta contém dados válidos
    if from_currency not in data:
        raise ValueError(f'Invalid currency code: {from_currency}')

    if to_currency not in data[from_currency]:
        raise ValueError(f'Conversion rate not available for {to_currency}')

    # Obtenha a taxa de conversão
    rate = data[from_currency][to_currency]
    converted_amount = amount * rate
    # Retorne o valor convertido
    return round(converted_amount, 2)


def convert_currency():  # Convertendo para maiúsculas

    from_currency = requests.args.get('from', '').upper()
    # Convertendo para maiúsculas
    to_currency = requests.args.get('to', '').upper()
    amount = float(requests.args.get('amount', 1))

    supported_currencies = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']
    if (from_currency not in supported_currencies or
       to_currency not in supported_currencies):
        return jsonify({'error': 'Invalid currency specified.'}), 400

    try:
        converted_amount = get_conversion_rate(
            from_currency, to_currency, amount)
        return jsonify({'converted_amount': converted_amount}
                       )
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    # if 'error' in data:
    #     raise ValueError('Invalid currency code')

    # rates = data.get('conversion_rates')
    # if to_currency not in rates:
    #     raise ValueError('Conversion rate not available')

    # return amount * rates[to_currency]
