import os
from prefect import flow, get_run_logger, task
from lastipy.user import User
from lastipy.spotify.client import build_client
from spotipy import Spotify
from lastipy.spotify import new_releases
from datetime import date, timedelta
from lastipy.spotify import album
from lastipy.spotify import library

@flow(retries=3)
def save_new_releases():
    # TODO fetch users from database?
    users = [User(spotify_username="sonofjack3", lastfm_username="sonofjack3", new_releases_ignore_remixes=True)]
    for user in users:
        save_new_releases_for_user(user)

@task()
async def save_new_releases_for_user(user: User):
    logging = get_run_logger()
    logging.info("Saving new releases for user %s", user.spotify_username)
    spotify_client = build_client(user.spotify_username)

    yesterday = date.today() - timedelta(days=1)

    logging.info("Fetching new releases...")
    new_tracks = new_releases.fetch_new_tracks(
        spotify_client,
        ignore_remixes=user.new_releases_ignore_remixes,
        album_types=[album.SINGLE_ALBUM_TYPE, album.ALBUM_ALBUM_TYPE],
        as_of_date=yesterday,
    )
    logging.info("Fetched %s new tracks", str(len(new_tracks)))

    # TODO Last.fm integration
    # if ignore_scrobbled_songs:
    #     logging.info("Filtering out scrobbled tracks from new releases")
    #     # TODO this is pretty inefficient but it appears to be the only way to tell if a user has scrobbled a track
    #     recent_tracks = fetch_recent_tracks(user=lastfm_user, api_key=lastfm_api_key)
    #     new_tracks = filter_out_tracks_in_second_list(new_tracks, recent_tracks)

    if len(new_tracks) > 0:
        logging.info("Adding %s tracks to %s's Liked Songs", str(len(new_tracks)), user.spotify_username)
        library.add_tracks_to_library(spotify_client, new_tracks)
    else:
        logging.info("No new tracks to add!")
