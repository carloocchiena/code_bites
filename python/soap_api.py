# Import the needed modules
from zeep import Client
from zeep.transports import Transport
from requests import Session

# Set the endpoint URL
url = 'url.com'

# Create the SOAP client
client = Client(url)

# Set the credentials
username = 'username'
password = 'password'

# Make the SOAP request
token_response = client.service.getToken(USERNAME=username, PASSWORD=password)

# Process the response
token = token_response.getTokenResult
print(token_response)

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
