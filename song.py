class Song():
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        if rate >= Song.MIN_RATING and rate <= Song.MAX_RATING:
            self.rating = rate
        else:
            raise ValueError("Rating out of range {} - {}").format(Song.MIN_RATING, Song.MAX_RATING)
