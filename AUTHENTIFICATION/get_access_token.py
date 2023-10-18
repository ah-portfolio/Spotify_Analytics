import base64
import requests

client_id = xxx

client_secret = xx

code= xx

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:8080/"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)


token = r.json()["refresh_token"]

print(token)
