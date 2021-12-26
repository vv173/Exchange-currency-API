#!/usr/bin/env python3

# File name: python_api.py
# Description: Exchange-currency-API
# Author: Viktor Vodnev
# Date: 05-06-2021

import requests
import datetime
import logging
import json
import csv

def json_response(URL, parameters):
    logging.info("Starting json response")
    try:
        response = requests.get(URL, params=parameters)
        json_response = response.json()
    except:
        logging.exception("Failed to make api request")
    finally:
        logging.debug("Successful api request ")
    return json_response

def data_cp(parameters, json_response):
    logging.info("Getting information from a jason file")
    try:
        #converting a string of currencies into a list
        currencies = parameters['symbols'].split(',')

        data = [[],[]]
        for currency in currencies:  
            data[0].append(currency)
            data[1].append(json_response['rates'][currency])
    except:
        logging.exception("Error getting information from a json file")

    return data

#converting a Unix timestamp to the default date
def time_convert(json_response):
    timestamp = json_response['timestamp']                
    creation_time = datetime.datetime.fromtimestamp(
        int(timestamp)
        ).strftime('%d-%m-%Y_%H_%M_%S')
    return creation_time

#sets the name of the CSV file in the format "name - date - time" 
def file_name(creation_time):
    file_name = 'euro_exchange_rate_' + str(creation_time) + '.csv'
    return file_name

def convert_to_json(filename, data):
    try:
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
            logging.debug("Successful writing to file ")
    except:
        logging.exception("Errors during file creation")
    finally:
        logging.debug("The file is completely filled with data")

def main():
    
    API_KEY = 'c168447546cedb690c58f867c4dbc434'
    URL = 'http://api.exchangeratesapi.io/v1/latest'
    BASE_CURRENCY = 'EUR'
    SYMBOLS = 'USD,PLN,GBP,CNY,RUB'

    logging.basicConfig(level=logging.DEBUG, filename='exchange.log',
     format='%(asctime)s %(levelname)s:%(message)s')

    #parameters for API get request
    parameters = {
        'access_key': API_KEY,
        'base': BASE_CURRENCY, 
        'symbols': SYMBOLS
    }
    json_r = json_response(URL, parameters)
    time = time_convert(json_r)
    data = data_cp(parameters, json_r)
    convert_to_json(file_name(time), data)

if __name__ == '__main__':
    main()
