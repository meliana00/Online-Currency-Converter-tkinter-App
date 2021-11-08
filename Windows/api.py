import requests
import json

response = requests.get(f"https://open.er-api.com/v6/latest/USD").text
data_json = json.loads(response)
data_rates = data_json["rates"]

def brain():

    key_values = []
    for key, value in data_rates.items():
        #print(key, '->', value)
        key_values.append(key)

    return key_values