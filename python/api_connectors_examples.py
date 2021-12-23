#some very simple example of python API connectors for any further reference


# this is one
import requests
from requests.auth import HTTPDigestAuth

ID = "123456"
TOKEN = "abcdef"

url = "https:\\www.pizza.com\apiconnect"
result = requests.get(url, auth=HTTPDigestAuth('ID', 'TOKEN'))
result


# this is two
import requests

url = "https:\\www.pizza.com\apiconnect"

headers = {'User-Agent': '123456',
           'X-Auth-Token': 'abcdef'
           }
r = requests.get(url, headers=headers)
r

# this is three
import requests

user = "test@yopmail.com"
token = "eyJraWQiOiJFbFQ5UG9WM25jN2VpVlwv"
headers = {"Authorization": "Bearer" + f" {token}"}

url = "https://api.example.com/v1/products"
requests.get(url, headers=headers)
