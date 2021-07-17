from flask import Flask, url_for, render_template, request
import requests
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

    query = f"?fsym={request.form['cripto']}&tsym=USD&limit=1"
    res = requests.get(endpoint + query)

    resp = json.loads(res.content)

    print(resp['Data'])

    return render_template('index.html', data=resp['Data'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5500))
    app.run(host='0.0.0.0', port=port)
