class User:
    def __init__(self, spotify_username: str, lastfm_username: str, new_releases_ignore_remixes: bool):
        self.spotify_username = spotify_username
        self.lastfm_username = lastfm_username
        self.new_releases_ignore_remixes = new_releases_ignore_remixes