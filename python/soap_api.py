# ---- FIRST VERSION WITHOUT EXPORT ---

# Import the needed modules
import os

from zeep import Client
from zeep.transports import Transport
from requests import Session
import time

# Set the endpoint URL
wsdl = os.environ['WSDL']

# Create the SOAP client
client = Client(wsdl)

# Set the credentials
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

# Make the SOAP request
token_response = client.service.getToken(USERNAME=username, PASSWORD=password)

# Process the response
token = token_response.getTokenResult
print(token_response)

# wait for the process to grab the token
time.sleep(5)

# Set the custom headers
headers = {
    'Authorization': 'Bearer ' + token,
}

# Create a session and set the headers
session = Session()
session.headers.update(headers)

# Create the custom transport with the session
transport = Transport(session=session)

# Set the transport on the client
client.transport = transport

# Make the SOAP requests accordingly to documentation
get_identita = client.service.GetDDNItem(TokenCode=token, Riferimento='TipologiaDocumentoIdentita')

get_fornitore = client.service.GetDDNItem(TokenCode=token, Riferimento='Fornitore')

get_pagamento = client.service.GetDDNItem(TokenCode=token, Riferimento='ModalitaPagamento')

get_pagamento_web = client.service.GetDDNItem(TokenCode=token, Riferimento='ModalitaPagamentoWeb')

get_categoria_uso_gas = client.service.GetDDNItem(TokenCode=token, Riferimento='CategoriaUsoGas')

print(f'ID: {get_identita}')
print(f'FORNITORE: {get_fornitore}')
print(f'PAGAMENTO: {get_pagamento}')
print(f'PAGAMENTO WEB: {get_pagamento_web}')
print(f'CAT_USO_GAS: {get_categoria_uso_gas}')

# --- SECOND VERSION WITH EXPORT OF ALL THE DATA TO TXT ---

import os
import sys
from requests import Session
import time

from zeep import Client
from zeep.transports import Transport

# Create the container for the JSON data
output_file= 'output.txt'

# Set the endpoint URL
wsdl = os.environ['WSDL']

# Create the SOAP client
client = Client(wsdl)

# Set the credentials
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

# Make the SOAP request
token_response = client.service.getToken(USERNAME=username, PASSWORD=password)

# Process the response
token = token_response.getTokenResult
print(token_response)

# wait for the process to grab the token
time.sleep(5)

# Set the custom headers
headers = {
    'Authorization': 'Bearer ' + token,
}

# Create a session and set the headers
session = Session()
session.headers.update(headers)

# Create the custom transport with the session
transport = Transport(session=session)

# Set the transport on the client
client.transport = transport

# Make the SOAP requests accordingly to documentation
get_identita = client.service.GetDDNItem(TokenCode=token, Riferimento='TipologiaDocumentoIdentita')

get_fornitore = client.service.GetDDNItem(TokenCode=token, Riferimento='Fornitore')

get_pagamento = client.service.GetDDNItem(TokenCode=token, Riferimento='ModalitaPagamento')

get_pagamento_web = client.service.GetDDNItem(TokenCode=token, Riferimento='ModalitaPagamentoWeb')

get_categoria_uso_gas = client.service.GetDDNItem(TokenCode=token, Riferimento='CategoriaUsoGas')

get_offerta = client.service.getOffertaAkyra(TokenCode=token, CodiceOfferta='022326ESVFL01XX00SECPUNAWPL30001')

# Testing the new GET method required by SENTRA
get_campagna = client.service.GetOfferteCampagna(TokenCode=token, Campagna='FUNNELTEST')

# Print everything to "output.txt"
with open(output_file, 'w') as f:
  # Overwrite original Print method
  original_stdout = sys.stdout
  sys.stdout = f

  print(f'ID: {get_identita}')
  print(f'FORNITORE: {get_fornitore}')
  print(f'PAGAMENTO: {get_pagamento}')
  print(f'PAGAMENTO WEB: {get_pagamento_web}')
  print(f'CAT_USO_GAS: {get_categoria_uso_gas}')
  print(f'OFFERTA: {get_offerta}')
  print(f'CAMPAGNA: {get_campagna}')

  # Recover the original Print method
  sys.stdout = original_stdout

# Print the results
print(f'ID: {get_identita}')
print(f'FORNITORE: {get_fornitore}')
print(f'PAGAMENTO: {get_pagamento}')
print(f'PAGAMENTO WEB: {get_pagamento_web}')
print(f'CAT_USO_GAS: {get_categoria_uso_gas}')
print(f'OFFERTA: {get_offerta}')
print(f'CAMPAGNA: {get_campagna}')

