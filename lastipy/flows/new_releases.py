import os
from prefect import flow, get_run_logger, task
from lastipy.user import User
from spotipy import Spotify
import lastipy.spotify

@flow(retries=3)
def save_new_releases():
    # TODO fetch users from database?
    users = [User(spotify_username="sonofjack3", lastfm_username="sonofjack3")]

    for user in users:
        save_new_releases_for_user(user)

@task()
async def save_new_releases_for_user(user: User):
    logging = get_run_logger()
    logging.info("Saving new releases for user %s", user.spotify_username)
    spotify_client = Spotify(lastipy.spotify.token.get_token(user.spotify_username, os.environ["SPOTIFY_CLIENT_ID"], os.environ["SPOTIFY_CLIENT_SECRET"]))
    # TODO fetch and save new releases

if __name__ == "__main__":
    save_new_releases.serve(
        name="new_releases_deployment", 
        cron="* * * * *"
    )
