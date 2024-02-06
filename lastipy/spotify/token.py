import spotipy.oauth2 as oauth2
import os
from lastipy import definitions

def get_token(username, client_id_key, client_secret_key):
    # These are the only scopes required by this app so no need to parameterize this
    scope = (
        "playlist-modify-public user-library-read user-library-modify user-follow-read"
    )

    sp_oauth = oauth2.SpotifyOAuth(
        client_id_key,
        client_secret_key,
        scope=scope,
        cache_path=os.path.join(definitions.ROOT_DIR, 'spotipy_cache/', ".cache-" + username),
    )

    token_info = sp_oauth.get_cached_token()
    return token_info["access_token"]
