# coding: utf-8


# Get list of configurations from ConnectWise through the API.

from requests import request
import requests
import json

# I keep the Headers for Authentication in a separate file and import them. If anyone needs / wants to see an example shoot me a message.
import auth

url = "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/company/configurations/"
config_response = requests.request(method="GET", url=url, headers=auth.headers()).json()

# I don't really know what this does but it makes it work.
config_data = json.dumps(config_response)
# This too. It makes it so I can parse out the values of each index value
config_load = json.loads(config_data)

# Enumerate # of configs.
# This actually doesn't seem to work the way I want, it seems to only grab some configurations - not all.
for x,i in enumerate(config_load):
    try:
        config_status =  config_load[x]['status']['name']
        config_id = config_load[x]['id']
        config_serial = config_load[x]['serialNumber']
        config_tag = config_load[x]['tagNumber']
    except: IndexError

    print config_id , " "  , config_serial , " "  , config_tag , " "  , config_status, "\n"
