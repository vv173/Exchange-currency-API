import requests
import datetime
import json
import csv

API_KEY = 'c168447546cedb690c58f867c4dbc434'
URL = 'http://api.exchangeratesapi.io/v1/latest'
BASE_CURRENCY = 'EUR'
SYMBOLS = 'USD,PLN,GBP,CNY,RUB'

#parametry dla api get request 
parameters = {
    'access_key': API_KEY,
    'base': BASE_CURRENCY, 
    'symbols': SYMBOLS
}

response = requests.get(URL, params=parameters)
json_response = response.json()

#zamiana ciągu walut na listę
currencies = SYMBOLS.split(',')

data = [[],[]]
for currency in currencies:
    data[0].append(currency)
    data[1].append(json_response['rates'][currency])

#konwertowanie uniksowego znacznika czasu na domyślną datę 
timestamp = json_response['timestamp']                
creation_time = datetime.datetime.fromtimestamp(
    int(timestamp)
    ).strftime('%d-%m-%Y_%H_%M_%S')

#ustawiam nazwę pliku csv w formacie "nazwa - data - godzina"
file_name = 'euro_exchange_rate_' + str(creation_time) + '.csv'

with open(file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)