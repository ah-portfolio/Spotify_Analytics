import requests
from urllib.parse import urlencode
import base64
import webbrowser


client_id = "xx"
client_secret = "xx"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:8080/",
    "scope": "user-read-recently-played"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
