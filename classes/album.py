from typing import Optional

class Album:
    def __init__(self, id: int, title: str, artist: str, release_date: str, genre: Optional[str] = None):
        self.id = id
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.genre = genre
        self.rating = None

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'release_date': self.release_date,
            'genre': self.genre,
            'rating': self.rating
        }






 

        



