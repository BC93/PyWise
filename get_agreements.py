# coding: utf-8


import requests
import json
import auth



url = "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/finance/agreements/"

response = requests.request(method="GET", url=url, headers=auth.headers()).json()

dump = json.dumps(response)

load = json.loads(dump)

for i,v in enumerate(load):
    print "Start Date: ", load[i]['startDate']
    print "End Date: ", load[i]['endDate']
    print "SLA ID: ", load[i]['slaId']
    print "Agreement ID: ", load[i]['id']
    print load[i]['company']['id']
    print load[i]['company']['identifier']
    print "\n"
    print "-------------------------------------------"


