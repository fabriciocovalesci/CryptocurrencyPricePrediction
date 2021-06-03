from flask import Flask, url_for, render_template, request
import requests
from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
from datetime import datetime
import os

endpoint = 'https://min-api.cryptocompare.com/data/histoday'


app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    dict_crypto = {
        'BTC': 'bitcoin',
        'ETH': 'ethereum',
        'ADA': 'cardano',
        'DOGE': 'dogecoin',
        'XRP': 'xrp',
        'DOT': 'polkadot',
        'UNI': 'uniswap',
        'ICP': 'internet-computer',
        'LINK': 'chainlink',
        'BNB': 'binance-coin'
    }

    crypto = dict_crypto.get(request.form['cripto'])
    query = f"?fsym={request.form['cripto']}&tsym=USD&limit=1"
    res = requests.get(endpoint + query)
    print(res.content)

    api_gecko = CoinGeckoAPI()
    price = api_gecko.get_price(ids=crypto, vs_currencies='usd', include_24hr_vol='true')
    chart_data = api_gecko.get_coin_ohlc_by_id(id=crypto, vs_currency='usd', days=1)

    return render_template('index.html', data=res.content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5500))
    app.run(host='0.0.0.0', port=port)
