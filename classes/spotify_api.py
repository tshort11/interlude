import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Optional, List, Dict

class SpotifyAPI:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: Optional[str] = None):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        ))

    def search_album(self, album_name: str) -> Dict:
        try:
            result = self.sp.search(q=f"album:{album_name}", type='album', limit=1)
            if result['albums']['items']:
                album = result['albums']['items'][0]
                return {
                    'title': album['name'],
                    'artist': album['artists'][0]['name'],
                    'release_date': album['release_date']
                }
        except Exception as e:
            print(f"Error searching album: {e}")
        return {}

    def search_song(self, song_name: str) -> Dict:
        try:
            result = self.sp.search(q=song_name, type='track', limit=1)
            if result['tracks']['items']:
                track = result['tracks']['items'][0]
                return {
                    'title': track['name'],
                    'artist': track['artists'][0]['name'],
                    'album': track['album']['name'],
                    'duration_ms': track['duration_ms']
                }
        except Exception as e:
            print(f"Error searching song: {e}")
        return {}

    def search_artist(self, artist_name: str) -> Dict:
        try:
            result = self.sp.search(q=artist_name, type='artist', limit=1)
            if result['artists']['items']:
                artist = result['artists']['items'][0]
                return {
                    'id': artist['id'],
                    'name': artist['name'],
                    'genre': artist['genres'][0] if artist['genres'] else 'Unknown'
                }
        except Exception as e:
            print(f"Error searching artist: {e}")
        return {}

    def get_new_releases(self, limit: int = 5) -> List[Dict]:
        try:
            result = self.sp.new_releases(limit=limit)
            albums = result['albums']['items']
            return [{
                'title': album['name'],
                'artist': album['artists'][0]['name'],
                'release_date': album['release_date']
            } for album in albums]
        except Exception as e:
            print(f"Error fetching new releases: {e}")
            return []

