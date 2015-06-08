import unittest

from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.test_song = Song(
            "Hells Bells",
            "ACDC",
            "Hells Bells",
            5,
            500,
            256
        )

    def test_song_init(self):
        self.assertEqual(self.test_song.title, "Hells Bells")
        self.assertEqual(self.test_song.artist, "ACDC")
        self.assertEqual(self.test_song.album, "Hells Bells")
        self.assertEqual(self.test_song.rating, 5)
        self.assertEqual(self.test_song.length, 500)
        self.assertEqual(self.test_song.bitrate, 256)

    def test_rate(self):
        self.test_song.rate(2)
        self.assertEqual(self.test_song.rating, 2)

if __name__ == '__main__':
    unittest.main()
