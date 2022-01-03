#!/usr/bin/env python3

# File name: python_api.py
# Description: Exchange-currency-API
# Author: Viktor Vodnev
# Date: 03-01-2021

import requests
import datetime
import logging
import json
import csv
import argparse

def arguments():
    logging.info("Start parsing arguments ")
    try:
        parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
        parser.add_argument("-a", type=str, default=None, required=True, help="Enter the link to the API")
        parser.add_argument("-k", type=str, default=None, required=True, help="Enter the key for the API")
        args = parser.parse_args()
    except:
        logging.exception("Error reading arguments ")
    finally:
        logging.debug("Argument reading completed successfully")
    return args

def json_response(URL, parameters):
    logging.info("Starting json response")
    try:
        response = requests.get(URL, params=parameters)
    except:
        logging.exception("Failed to make api request")
    finally:
        logging.debug("Successful api request ")
    return response.json()

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
    file_name = './exchange/' + 'euro_exchange_rate_' + str(creation_time) + '.csv'
    return file_name

def convert_to_csv(filename, data):
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
    args = arguments()
    API_KEY = args.k
    URL = args.a
    BASE_CURRENCY = 'EUR'
    CURRENCIES = 'USD,PLN,GBP,CNY,RUB'

    logging.basicConfig(level=logging.DEBUG, filename='exchange.log',
     format='%(asctime)s %(levelname)s:%(message)s')

    #parameters for API request
    parameters = {
        'access_key': API_KEY,
        'base': BASE_CURRENCY, 
        'symbols': CURRENCIES
    }

    time = time_convert(json_response(URL, parameters))
    data = data_cp(parameters, json_response(URL, parameters))
    convert_to_csv(file_name(time), data)

if __name__ == '__main__':
    main()