import os
from spotipy import Spotify
from lastipy.spotify.token import get_token

def build_client(username: str):
    return Spotify(get_token(username, os.environ["SPOTIFY_CLIENT_ID"], os.environ["SPOTIFY_CLIENT_SECRET"]))