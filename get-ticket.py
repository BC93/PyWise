# coding: utf-8
# get ticket status by id.

import requests
import json
import auth
import bcolors


tid = input('Enter Ticket ID: ')
url = "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets/%s" % tid


# request the url, with the method, url, and headers as json
response = requests.request(method="GET", url=url, headers=auth.headers()).json()

# dump the response into a list format for parsing
data = json.dumps(response)

# get ticket summary
suma = json.loads(data)['summary']
# get ticket status
# First, we need to load the key 'status'
status = json.loads(data)['status']
# then we need to call the subkey 'name'
pstatus = status['name']
# get ticket company
com = json.loads(data)['company']
pcom = com['identifier']
# get ticket description
desc = json.loads(data)['initialDescription']


print bcolors.bcolors.OKGREEN, "\tSummary: ", suma, bcolors.bcolors.ENDC, "\n"

print bcolors.bcolors.OKBLUE, "\tCompany: ", pcom, bcolors.bcolors.ENDC, "\n"

if pstatus == ">Closed":
    print bcolors.bcolors.WARNING,  "\tStatus: ", pstatus, bcolors.bcolors.ENDC, "\n"
elif pstatus == "Open":
    print bcolors.bcolors.OKGREEN,  "\tstatus: ", pstatus, bcolors.bcolors.ENDC, "\n"

print bcolors.bcolors.OKGREEN, "\tDescription: ", desc, bcolors.bcolors.ENDC, "\n"
print "\n\n"
