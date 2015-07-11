from mutagen.mp3 import MP3
import pygame
from song import Song
from playlist import Playlist

import os
NUM = 0


class MusicCrawler():

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        result = Playlist("Rock'n'roll")
        music_files = [f for f in os.listdir(self.path) if f.endswith('.mp3') or f.endswith('.MP3')]
        for song in music_files:
            audio = MP3(self.path + "/" + song)
            my_new_song = Song(audio["TIT2"],
                               audio["TPE1"],
                               audio["TALB"],
                               0,
                               int(audio.info.length),
                               audio.info.bitrate
                               )
            result.add_song(my_new_song)
        return result


def start_song_with_num(array_of_songs, num):
    if num <= len(array_of_songs):
        pygame.mixer.init()
        pygame.mixer.music.load(array_of_songs[num - 1])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            temp_imput = input()
            if temp_imput.lower() == "stop":
                pygame.mixer.music.stop()
                return True
            elif temp_imput.lower() == "exit":
                pygame.mixer.music.stop()
                return False
    else:
        print("Dont have song with that number")
        return True


def start_playlist(array_of_songs, num):
    pygame.mixer.init()
    pygame.mixer.music.load(array_of_songs[num - 1])
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()

def startProgramNoRepeat():
    global NUM
    NUM += 1
    crawler = MusicCrawler("/home/alexandar/Documents/Programming-101/Week2/Music Library")
    playlist = crawler.generate_playlist()
    songs_arr = []
    for elem in playlist.songs:
        songs_arr.append("{} - {}.mp3".format(elem.artist, elem.title))

    if NUM > len(songs_arr):
        NUM = len(songs_arr)
    start_playlist(songs_arr, NUM)


def startProgram():
    print("startProgram")
    global NUM
    NUM += 1
    crawler = MusicCrawler("/home/alexandar/Documents/Programming-101/Week2/Music Library")
    playlist = crawler.generate_playlist()
    songs_arr = []
    for elem in playlist.songs:
        songs_arr.append("{} - {}.mp3".format(elem.artist, elem.title))

    print("Playlist:")
    for idx, elem in enumerate(songs_arr):
        print("[{}] {}".format(idx + 1, elem))
    if NUM > len(songs_arr):
        NUM = 1
    start_playlist(songs_arr, NUM)
