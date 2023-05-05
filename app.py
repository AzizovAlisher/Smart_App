import pandas as pd 
import numpy as np
import json
import requests
import sys
import database_manager

def get_exchange_rate(from_currency,to_currency):

    token = 'DIUF8PP4X3TKH776'
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
    url += '&from_currency='+from_currency
    url += '&to_currency='+to_currency
    url += '&apikey='+token

    data = requests.get(url).json()
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return exchange_rate

def eur_to_rub():

    rub = (get_exchange_rate("EUR","RUB"))
    rub = round(float(rub), 2)
    return rub

def extract_data(file):

    df = pd.read_excel(file)
