import requests
import json
import pfauth
import cwauth
import time

# Note: Notice I'm import pfauth and cwauth. 
# These are python files I created for my headers so I don't have to type them out everytime.
# I will post an example auth file for each later.


# datastore to log each unique event id.
def datastore(event_id):

        with open('datastore.txt', 'a') as f: f.write(event_id)
        with open('datastore.txt', 'a') as f: f.write("\n")

def pf_tickets():
    pfheaders = pfauth.headers()
    # You'll need to change this for whatever your url and group ids are.
    pf_url = "http://pfe3trial.printfleet.com:80/restapi/3.6.5/alerts/events?groupid=32323aa3-85dd-4f59-aa80-5aa0825cc455"
    # Get response for PrintFleet API

    pf_response = requests.request(method="GET", url=pf_url, headers=pfheaders).json()

    dump = json.dumps(pf_response)
    data = json.loads(dump)
    for k,v in enumerate(data):
        name = data[k]['description']['description']
        event_id = data[k]['alertEventId']
        with open('datastore.txt', 'r') as f:
            # Check if we already created a ticket for each event.
            if not any(str(event_id) == x.rstrip('\n\n') for x in f):
                # qeue the event for processing
                qeue(event_id, name)
                # write the event to the log file so we don't create duplicate tickets
                datastore(event_id)
            else:
                print("A ticket has already been created for event %s, skipping." %event_id)
                pass


def qeue(event_id, name):

    # You'll need to change this for your url
    cw_url = "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets"
    print("Creating Ticket in Connectwise.")
    
    # For this section you can really add whatever info you want displayed in the ticket. 
    # Just set the data you want from printfleet as a variable and put the variable whereever you want in the service ticket.
    
    ticket = {
        "id": 0,
        "summary": name,

        "recordType": "ServiceTicket",
        "company": {
            "id": 250,
            "identifier": "250",
            "_info": {}
                },
        "site": {
            "id": 0,
            "name": "string",
            "_info": {}
                },
        "initialDescription": event_id
        }

    cw_response = requests.request(method="POST", url=cw_url, headers=cwauth.headers(), data=json.dumps(ticket)).json()
# I set this file so it checks PrintFleet on an interval, you can change this or remove it to run whenever you want manually.
while True:
    pf_tickets()
    time.sleep(10)
