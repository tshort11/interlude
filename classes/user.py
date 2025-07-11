import json
from typing import List

class User:
    MAX_FAVORITES = 5

    def __init__(self, user_id: int, username: str, email: str, password: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password  # TODO: Hash this for security
        self.favorite_albums: List = []
        self.favorite_songs: List = []
        self.favorite_artists: List = []

    def check_password(self, password: str) -> bool:
        # TODO: Replace with hashed password check
        return self.password == password

    def add_favorite_album(self, album):
        if len(self.favorite_albums) >= self.MAX_FAVORITES:
            raise ValueError(f"You can only add up to {self.MAX_FAVORITES} favorite albums.")
        self.favorite_albums.append(album)
        print(f"Album '{album.title}' added to {self.username}'s favorites.")

    def add_favorite_song(self, song):
        if len(self.favorite_songs) >= self.MAX_FAVORITES:
            raise ValueError(f"You can only add up to {self.MAX_FAVORITES} favorite songs.")
        self.favorite_songs.append(song)
        print(f"Song '{song.title}' added to {self.username}'s favorites.")

    def add_favorite_artist(self, artist):
        if len(self.favorite_artists) >= self.MAX_FAVORITES:
            raise ValueError(f"You can only add up to {self.MAX_FAVORITES} favorite artists.")
        self.favorite_artists.append(artist)
        print(f"Artist '{artist.name}' added to {self.username}'s favorites.")

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'favorite_albums': [album.to_dict() for album in self.favorite_albums],
            'favorite_songs': [song.to_dict() for song in self.favorite_songs],
            'favorite_artists': [artist.to_dict() for artist in self.favorite_artists]
        }
