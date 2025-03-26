import json
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth


class Credentials:
    consumer_key = "xNeRioGer58j1EQHkxJ2oZLDJ1v5HqqAoXt8Si1gH1tQpJXv"
    consumer_secret = "WsZ4Vl2g0J7aWmDc4gkfewOl9ZlyUm2ke2fQtONGOROMUFIR6FAVdhZv1wcGyxiS"
    # passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url ="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"




class AccessToken:
    request = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(request.text)['access_token']


class Password:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    shortcode = "174379"
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    # passkey = Credentials.passkey
    to_encode = shortcode + passkey +timestamp
    encoded_password = base64.b64encode(to_encode.encode())
    encode_str = shortcode + passkey +timestamp
    decoded_password = encoded_password.decode('utf-8')

    # encoded = base64.b64encode(encode_str.encode())
