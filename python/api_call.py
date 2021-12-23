import requests

user = "test@yopmail.com"
token = "eyJraWQiOiJFbFQ5UG9WM25jN2VpVlwv"
headers = {"Authorization": "Bearer" + f" {token}"}

url = "https://api.example.com/v1/products"
requests.get(url, headers=headers)
