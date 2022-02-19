import spotipy
import config


# Getting playing music from spotify api

def spotify_request():
    current = spotify_object.currently_playing()
    song_info['name'] = current['item']['name']
    song_info['autor'] = current['item']['album']['artists'][0]['name']
    song_info['url'] = current['item']['external_urls']['spotify']
    return song_info


def status():
    current = spotify_object.currently_playing()
    return current['is_playing']


song_info = dict()
scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=config.spotify_client_id,
                                    client_secret=config.spotify_secret,
                                    redirect_uri=config.spotify_redirect_uri,
                                    scope=scope)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)
