import requests
from urllib.parse import urlencode
import base64
import webbrowser


client_id = "9f03a121933946b697c1a34194df6440"
client_secret = "83b47bf1e8ab4dbaab75ab20efacbe3d"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:8080/",
    "scope": "user-read-recently-played"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))