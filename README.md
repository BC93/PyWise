# Pywise (Work in Progress)

  Pywise is a Command Line Utility for interacting with ConnectWise through the API. ConnectWise can often be a painfully slow and clunky software to deal with, and offers no native Command Line Interface (CLI). Additionally, ConnectWise does not natively support any Linux Distributions, except through the webapp. 
  
## Features:
* List all tickets
* List open tickets (Coming soon)
* List all open or closed tickets for a particular resource (Coming soon)
* List all Agreements (W.I.P. - Including: Company Name, Agreement start and end date, client contact details, SLA, and configuration list.
* List all Configurations (SLA's, Company, Expiration Date, Contact details, Serial #'s)
* Serial Number Search - (Coming soon) - search serial number, return coverage details, past tickets, clients, etc.
* Ticket Creation 
* Ticket Updating
* Time Keeping.


# Moving Forward:
  Please note this is a large project that started as something small from a requirement by my employer to create tickets from another software automatically. I have a lot on my plate so I can't give an estimated completion date at this time. 
  I welcome all contributors and collaborators.

# Getting Started:
## Headers
* You're going to need to create an API member in ConnectWise, then create a new API key.
* type out companyname+apipublickey:privatekey
  /ex fakecompany+asdfsadfpubafdgad:asfprivadfg
* base64 encode that string
  - let's say the output of that was asdfoajo23429sd==
* after cloning this repo create a new cwauth.py file with the following contents.

    headers = {
      'Authorization': 'basic asdfoajo23429sd==',
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Cache-Control': 'no-cache'
      }
## More Coming Soon

# Contributors / Collaborators:
* **Lead Developer**: Brian Coffey (bcoffey218)
* Aaron (CodeCity)

# Questions, Concerns, Contact:
  If you have questions or  concerns, or would like to contribute feel free to reach me at: bcoffey218@gmail.com.


