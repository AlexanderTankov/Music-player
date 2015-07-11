import unittest

from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.test_playlist = Playlist("Rock'n'roll")
        self.test_song = Song(
            "Hells Bells",
            "ACDC",
            "Hells Bells",
            5,
            309,
            256
        )

    def test_playlist_init(self):
        self.assertEqual(self.test_playlist.name, "Rock'n'roll")

    def test_add_song(self):
        self.test_playlist.add_song(self.test_song)
        self.assertIn(self.test_song, self.test_playlist.songs)

    def test_remove_song(self):
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.remove_song("Hells Bells")
        self.assertNotIn(self.test_song, self.test_playlist.songs)

    def test_total_length(self):
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_song)
        self.assertEqual(self.test_playlist.total_length(), 618)

    def test_remove_disrated(self):
        self.test_bad_song = Song(
            "Highway to hell",
            "ACDC",
            "Hells Bells",
            1,
            309,
            256
        )
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.remove_disrated(2)
        self.assertNotIn(self.test_bad_song, self.test_playlist.songs)
        self.assertIn(self.test_song, self.test_playlist.songs)

    def test_removev_bad_quality(self):
        self.test_bad_song = Song(
            "Highway to hell",
            "ACDC",
            "Hells Bells",
            5,
            309,
            1
        )
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_bad_song)
        self.test_playlist.remove_bad_quality()
        self.assertNotIn(self.test_bad_song, self.test_playlist.songs)
        self.assertIn(self.test_song, self.test_playlist.songs)

    def test_show_artists(self):
        self.test_new_song = Song(
            "November rain",
            "Guns'n'Roses",
            "Hells Bells",
            5,
            240,
            1
        )
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_new_song)
        self.assertEqual(self.test_playlist.show_artists(), ["ACDC", "Guns'n'Roses"])

    def test_str(self):
        self.test_new_song = Song(
            "November rain",
            "Guns'n'Roses",
            "Hells Bells",
            5,
            240,
            1
        )
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_new_song)
        self.assertEqual(str(self.test_playlist), "ACDC Hells Bells - 05:09'\n'Guns'n'Roses November rain - 04:00")

    def test_save(self):
        self.test_new_song = Song(
            "November rain",
            "Guns'n'Roses",
            "Hells Bells",
            5,
            240,
            1
        )
        self.test_playlist.add_song(self.test_song)
        self.test_playlist.add_song(self.test_new_song)
        self.test_playlist.save("json_playlist.json")

#TODO stringIO
    def test_load(self):
        pass

if __name__ == '__main__':
    unittest.main()
