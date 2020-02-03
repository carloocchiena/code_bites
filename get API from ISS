#import the lib we need: requests for api, json to read the javascript output, datetime to convert the time format 

import requests as req
import json
from datetime import datetime


#for simplicity's sake, let's assign to r the req.get() in the format reg.get("url") to retrieve the data from the api

r= req.get("http://api.open-notify.org/astros.json")


#r.status_code allows us to  check the connection status (with typical server response: 200, 404, 301..)
print(r.status_code)

#r.headers allows us to check the overall header of the website (as well as CMS used and other info)
print(r.headers)

#r.json allows us to get the api data via a json file
print (r.json())

#we need to be able to read in python the json format, so far we created a function (using .dumps python native function)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print (text)

#ora possiamo stampare comodamente con la funzione jprint
jprint (r.json())


#un'altra api ci chiede dei parametri fissi di input (lo scopriamo nella documentazione), quindi creaimo un dizionario per storarli 
#più agevolmente, e li richiamiamo con il comando params

parameters={"lat":44.4037, "lon":8.6756 }


r= req.get("http://api.open-notify.org/iss-pass.json", params=parameters)
   
jprint (r.json())

#ora che abbiamo ottenuto un sacco di data, meglio focalizzarsi solo su quella che ci serve, andiamo quindi a prenderla all'interno del 
#json e poi storiamola in una lista 

pass_time=r.json()["response"]
jprint(pass_time)

risetimes= []

for d in pass_time:
    time = d["risetime"]
    risetimes.append(time)
    
print (risetimes)


#otteniamo dei dati espressi in epoche e convertiamoli in date comprensibili mediante la libreria date time:

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print (time)
    
print (time)


#in case a login is needed:

requests.get('https://api.github.com/user', auth=('user', 'pass'))
