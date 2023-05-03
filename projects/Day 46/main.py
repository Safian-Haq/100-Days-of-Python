import os

import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

CLIENT_ID = '7d87e3c495cb4851b74257efc2b063f8'
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'https://example.com'

if __name__ == '__main__':

    # Input for target year
    target_date = input('Which year do you want to travel to?\nType the date in YYYY-MM-DD below\n> ')
    # target_date = '2006-06-01'

    # Get the songs by scrapping billboard.com
    response = requests.get(URL + target_date)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text)

    songs = {}
    count = 1
    for row in soup.select("li[class^='o-chart-results-list__item']"):
        title = row.select('#title-of-a-story')
        if not title:
            continue
        title = title[0].getText().strip()
        singer = row.find(name='span').getText().strip()
        songs[count] = (title, singer)
        count += 1

    # Authenticate to use API
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="user-library-read, playlist-modify-public"))

    # Create a new playlist or overwrite the existing one
    playlist_name = f'T-MACHINE | {target_date}'
    id = sp.current_user()['id']
    is_new_playlist = True
    playlist_id = None
    for item in sp.user_playlists(id)['items']:
        if item['name'] == playlist_name:
            is_new_playlist = False
            playlist_id = item['id']

    if is_new_playlist:
        sp.user_playlist_create(user=id, name=playlist_name)
    else:
        sp.current_user_unfollow_playlist(playlist_id)
        playlist_id = sp.user_playlist_create(user=id, name=playlist_name)['id']

    # Search and get track id for each song
    tracks = []
    for song in songs.items():
        q = f'artist {song[0]}, track {song[1]}'
        track_id = sp.search(q)['tracks']['items'][0]['id']
        tracks.append(track_id)

    # Add all the track ids to the playlist
    sp.playlist_add_items(playlist_id, tracks)
