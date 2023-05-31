# python script to get authorization token from a web app that uses Auth0 authentication methods

import requests

# store app data
class MyAppData:
  client_id = 'CLIENT_ID' # don't put secrets in production code, in that case use .env
  redirect_uri = 'https://www.example.com/get_token'
  client_secret = 'CLIENT_SECRET' # don't put secrets in production code, in that case use .env
  token = 'TOKEN' # don't put secrets in production code, in that case use .env
  
# get the authorization link and generate auth token
def redirect():
    query = {
        'client_id': MyAppData.client_id,  
        'redirect_uri': MyAppData.redirect_uri,
        'response_type': 'code',
        'scope': '',
        'state': 'done',
    }
    redirect_url = 'https://target-website.com/oauth/authorize?' + requests.compat.urlencode(query)
    
    print(redirect_url)
    return redirect_url

# navigate to redirect_url and grab the token, storing it in the MyAppData.token variable

# generate the authorization token consequently
def generate_token(code):
    token_url = 'https://target-website.com/oauth/token'
    
    # Set the token request parameters
    data = {
        'grant_type': 'authorization_code',  # The type of token being requested
        'client_id': MyAppData.client_id,
        'client_secret': MyAppData.client_secret,
        'redirect_uri': MyAppData.redirect_uri,
        'code': MyAppData.token,
    }

    # Send the POST request
    response = requests.post(token_url, data=data)

    # Parse the JSON response
    token_data = response.json()
    print(token_data)

    # Access the token from the response
    if 'access_token' in token_data:
        access_token = token_data['access_token']
        print('Access Token is:', access_token)
    else:
        print('Error: Failed to obtain access token')

# Call the functions
redirect_url = redirect()
print('Redirect URL:', redirect_url)

generate_token(token)  
 
# you should see the authorization token printed out
# at this point you can grab this and use for making API calls to the web application
