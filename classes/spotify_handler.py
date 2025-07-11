import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyHandler:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = self.authenticate()

    def authenticate(self):
        auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        return spotipy.Spotify(auth_manager=auth_manager)

    def search_album(self, album_name, limit=1):
        try:
            results = self.sp.search(q=f"album:{album_name}", type='album', limit=limit)
            albums = results.get('albums', {}).get('items', [])
            # Extract simplified album info
            return [{
                'title': album['name'],
                'artist': album['artists'][0]['name'] if album['artists'] else 'Unknown',
                'release_date': album['release_date']
            } for album in albums]
        except Exception as e:
            print(f"Error searching albums: {e}")
            return []

