import base64
import requests

client_id = '9f03a121933946b697c1a34194df6440'

client_secret = '83b47bf1e8ab4dbaab75ab20efacbe3d'

code='AQBN1a8d6p-DbTuuk1rAw11EH_4_9MhDpnXVCDr619XequiLZzJSQyLMke-3DLfwDfqWxrIVffPZJHgIal-E0SEWjQfthLNMhCQg4mkE0lQJrd8OR6NK9tId7cwmeR_UtnitJmwNFHLOtgHiPNORDK9eSxnEhpe_KuRajyQxDP8UfsabsgPgqtodhsif'

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