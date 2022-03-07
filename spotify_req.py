import spotipy
import config
from youtubesearchpython import VideosSearch

next_tracks = dict()


# Getting playing music from spotify api

def spotify_request():
    current = spotify_object.currently_playing()
    song_info['name'] = current['item']['name']
    song_info['autor'] = current['item']['album']['artists'][0]['name']
    song_info['url'] = current['item']['external_urls']['spotify']
    if f"{current['item']['name']} - {current['item']['album']['artists'][0]['name']}" in next_tracks.keys():
        song_info['user'] = next_tracks[f"{current['item']['name']} - {current['item']['album']['artists'][0]['name']}"]
    else:
        song_info['user'] = ''
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


def add_track_to_queue(track_ids, user):
    if 'https://open.spotify.com/track/' not in track_ids:
        if 'https://youtu.be/' in track_ids or 'https://www.youtube.com/watch' in track_ids or \
                'https://youtube.com/watch' in track_ids:
            text = VideosSearch(track_ids).result()["result"][0]['title']
            try:
                url = spotify_object.search(text)['tracks']['items'][0]["external_urls"]["spotify"]
            except IndexError:
                return 'Такого трека не существует egDespair'
        else:
            try:
                url = spotify_object.search(track_ids)['tracks']['items'][0]["external_urls"]["spotify"]
            except IndexError:
                return 'Такого трека не существует egDespair'
    else:
        url = track_ids
    next_tracks[f'{spotify_object.track(url)["name"]} - {spotify_object.track(url)["artists"][0]["name"]}'] = user
    spotify_object.add_to_queue(url, None)
    return f'Успешно добавлен трек 🎵 {spotify_object.track(url)["name"]} - {spotify_object.track(url)["artists"][0]["name"]} 🎵'


def clear_playlist(playlist_id):
    spotify_object.trace = False
    result = spotify_object.playlist_tracks(playlist_id)
    track = []
    for i in result['items']:
        track.append(i['track']['uri'])
    spotify_object.user_playlist_remove_all_occurrences_of_tracks(config.username_spotify, playlist_id, track)
    return 'Плейлист успешно очищен Klass'


def spotify_volume(voluem=50):
    try:
        spotify_object.volume(voluem, None)
    except IndexError:
        return 'Ошибка. Устройсво выключено или к нему нет доступа'
    return f'громкость поставлена на {voluem}%'


def skip():
    try:
        spotify_object.next_track(None)
    except IndexError:
        return 'Ошибка. Устройсво выключено или к нему нет доступа'
    return 'Трек пропущен'


def play():
    try:
        spotify_object.start_playback(device_id=None)
    except IndexError:
        return 'Ошибка. Устройсво выключено или к нему нет доступа'
    return 'воспроизведение трека возобновлено'


def stop():
    try:
        spotify_object.pause_playback(None)
    except IndexError:
        return 'Ошибка. Устройсво выключено или к нему нет доступа'
    return 'воспроизведение остановлено'


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
