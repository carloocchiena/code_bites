#two very simple example of python API connectors for any further reference


#this is one
import requests
from requests.auth import HTTPDigestAuth

ID = "123456"
TOKEN = "abcdef"

url = "https:\\www.pizza.com\apiconnect"
result = requests.get(url, auth=HTTPDigestAuth('ID', 'TOKEN'))
result


#this is two
import requests

url = "https:\\www.pizza.com\apiconnect"

headers = {'User-Agent': '123456',
           'X-Auth-Token': 'abcdef'
           }
r = requests.get(url, headers=headers)
r

