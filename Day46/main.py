import os
import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
songs_uris = []
result = sp.search(q=f"track:{song_names[2]} year:{date.split('-')[0]}", type='track')
for song in song_names:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type='track')
    try:
        songs_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.........")

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)['id']

sp.playlist_add_items(playlist_id=playlist_id, items=songs_uris)
