class Artist:
    def __init__(self, id, name, genre=None):
        self.id = id
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"{self.name} (Genre: {self.genre if self.genre else 'Unknown'})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre
        }


    
