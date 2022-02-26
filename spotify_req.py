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


def data_update():
    global song_info, scope, token, token_dict, spotify_object
    song_info = dict()
    scope = 'playlist-modify-public playlist-modify-private user-read-currently-playing user-read-playback-state ' \
            'user-modify-playback-state'

    oauth_object = spotipy.SpotifyOAuth(client_id=config.spotify_client_id,
                                        client_secret=config.spotify_secret,
                                        redirect_uri=config.spotify_redirect_uri,
                                        scope=scope)

    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotify_object = spotipy.Spotify(auth=token)


def add_track_to_playlist(playlist_id, track_ids):
    spotify_object.trace = False

    if 'https://open.spotify.com/track/' not in track_ids[0]:
        track = spotify_object.search(track_ids)
        try:
            track_ids = [track['tracks']['items'][0]["external_urls"]["spotify"]]
        except IndexError:
            return 'Ошибка при добавлении. Возможно вы использовали ссылку не на спотифай или написали бесмысленный ' \
                   'набор символов egDespair TeaTime'

    playlist_id = playlist_id.split('/')[4].split('?')[0]
    spotify_object.playlist_add_items(playlist_id, track_ids)
    return 'Успешно добавлен'


song_info = dict()
scope = 'playlist-modify-public playlist-modify-private user-read-currently-playing user-read-playback-state ' \
            'user-modify-playback-state'

oauth_object = spotipy.SpotifyOAuth(client_id=config.spotify_client_id,
                                    client_secret=config.spotify_secret,
                                    redirect_uri=config.spotify_redirect_uri,
                                    scope=scope)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)
