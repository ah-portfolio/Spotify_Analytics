import requests
import json
import base64
import pandas as pd
from datetime import datetime, timedelta


########################################################
####### FIRST STEP #####################################
####### GET THE ACCESS TOKEN WITH THE REFRESH TOKEN ############

client_id = 'xx'
client_secret = 'xx'

refresh_token = 'xx'

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "refresh_token",
    'refresh_token' : refresh_token,
    "redirect_uri": "http://localhost:8080/"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)


access_token = r.json()['access_token']




########################################################
####### SECOND STEP #####################################
####### GET THE DATA############


limitation = 3 #Nombre de titres a extraire (max 50)

user_headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": limitation
}


user_tracks_response = requests.get("https://api.spotify.com/v1/me/player/recently-played", params=user_params, headers=user_headers)



items = user_tracks_response.json()['items']


TRACK_NAME = []
ALBUM = []
ALBUM_IMAGE = []
ARTIST = []
PLAYED_AT_GMT = []
PLAYED_AT_FR = []
POPULARITY = []

#INSERT DATA IN LISTS
for i in range (0,len(items)):
    ARTIST.append(items[i]['track']['artists'][0]['name']) #On prend le 1er artiste du featuring
    TRACK_NAME.append(items[i]['track']['name'])
    ALBUM.append(items[i]['track']['album']['name'])
    ALBUM_IMAGE.append(items[i]['track']['album']['images'][1]['url'])
    PLAYED_AT_GMT.append(items[i]['played_at'])
    POPULARITY.append(items[i]['track']['popularity'])
 
 
 
#CONVERT GMT DATETIME TO FR DATETIME
for el in PLAYED_AT_GMT :
    str_gmt = el[0:19].replace('T',' ')
    datetime_gmt = datetime.strptime(str_gmt, '%Y-%m-%d %H:%M:%S')
    datetime_fr = datetime_gmt + timedelta(hours=2)
    PLAYED_AT_FR.append(str(datetime_fr))
    

df = pd.DataFrame()

df['PLAYED_AT_GMT)']  = PLAYED_AT_GMT
df['PLAYED_AT_FR']  = PLAYED_AT_FR
df['TRACK_NAME']  = TRACK_NAME
df['ARTIST']  = ARTIST
df['ALBUM']  = ALBUM
df['ALBUM_IMAGE']  = ALBUM_IMAGE
df['POPULARITY']  = POPULARITY

print(df)


