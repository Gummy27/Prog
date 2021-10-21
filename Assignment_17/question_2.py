class MusicAlbum:
    def __init__(self, 
                band:str = "unknown band", 
                title:str = "unknown", 
                year: int = "unknown year"
        ) -> None:

        self.band = band
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"Album {self.title} by {self.band}, released in {self.year}."

    def set_album(self, 
                band:str = "unknown band", 
                title:str = "unknown", 
                year: int = "unknown year"
        ) -> None:

        self.band = band
        self.title = title
        self.year = year

album = MusicAlbum()

BAND = "Talking Heads"

TITLE= "Remain in Light"

YEAR = 1980

album.set_album(BAND, TITLE, YEAR)

print(album)
print(str(album))
print(f"Album {TITLE} by {BAND}, released in {YEAR}.")
assert str(album) == f"Album {TITLE} by {BAND}, released in {YEAR}."