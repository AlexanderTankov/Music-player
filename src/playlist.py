import json
from song import Song


class Playlist():

    @staticmethod
    def load(file_name):
        my_file = open(file_name, 'r')
        my_playlist = json.load(my_file)
        my_file.close()
        result = Playlist(my_playlist["name"])
        song_arr = my_playlist["songs"]
        for song in song_arr:
            temp_song = Song(
                song["title"],
                song["artist"],
                song["album"],
                song["rating"],
                song["length"],
                song["bitrate"]
            )
            result.songs.append(temp_song)
        return result

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song)

    def total_length(self):
        result = 0
        for song in self.songs:
            result += song.length
        return result

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating <= rating:
                self.songs.remove(song)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate < 200:
                self.songs.remove(song)

#TODO set
    def show_artists(self):
        result = []
        for song in self.songs:
            is_in_list = False
            for artist_in_result in result:
                if song.artist == artist_in_result:
                    is_in_list = True
            if not is_in_list:
                result.append(song.artist)
        return result

    def __str__(self):
        result = ""
        for song in self.songs:
            song_min = song.length // 60
            song_sec = song.length - song_min * 60
            if song_min < 10 and song_sec > 10:
                result += "{} {} - 0{}:{}'\n'".format(song.artist,
                                                      song.title,
                                                      song_min,
                                                      song_sec
                                                      )
            elif song_min > 10 and song_sec < 10:
                result += "{} {} - {}:0{}'\n'".format(song.artist, song.title, song_min, song_sec)
            elif song_min < 10 and song_sec < 10:
                result += "{} {} - 0{}:0{}'\n'".format(song.artist, song.title, song_min, song_sec)
            else:
                result += "{} {} - {}:{}'\n'".format(song.artist, song.title, song_min, song_sec)
        result = result[:len(result)]
        return result

    def save(self, file_name):
        song_arr = []
        for song in self.songs:
            temp_song = song.__dict__
            song_arr.append(temp_song)
        new_playlist = {"name": self.name, "songs": song_arr}
        new_playlist = json.dumps(new_playlist)

        big_file = open(file_name, 'w')
        big_file.write("".join(new_playlist))
        big_file.close()
