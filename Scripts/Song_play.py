#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thr April 18 18:18:20 2018
@author: Pran Kumar Sarkar
"""

import os
import re
import sys
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import speech_recognition as sr
from threading import Thread

# Defining global variables
SCRIPT_DIR = os.getcwd()

# Making path to work with linux and windows
if '/' in SCRIPT_DIR:
    SONGS_DIR = "../Songs/"
    FAV_SONGS_DIR = "../Songs/Favourite/"
    OTHER_SONGS_DIR = "../Songs/Others/"
else:
    SONGS_DIR = "..\\Songs\\"
    FAV_SONGS_DIR = "..\\Songs\\Favourite\\"
    OTHER_SONGS_DIR = "..\\Songs\\Others\\"


class Music:
    def __init__(self, width=300, height=200):
        """
        Initializing music player window variables
        :param width: Width of the music player
        :param height: Height of the music player
        """
        self.width = width
        self.height = height
        self.background_colour = (17, 0, 79)
        self.running = False

    def get_song(self):
        """
        Gets the name of song from user.

        :return:
            song: The name of the song to play
        """
        recognizer = sr.Recognizer()
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 400

        with sr.Microphone() as source:
            print("Which song should I play?")

            try:
                audio = recognizer.listen(source, timeout=5.0)

                song = recognizer.recognize_google(audio)
            except sr.WaitTimeoutError as e:
                print(e)
                song = ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                song = ""
            except sr.RequestError as e:
                print("Could not request results: {0}".format(e))
                song = ""

            # Pre-processing name of song
            song = song.lower()
            song = re.sub(r"[^a-zA-Z ]+", '', song)
            song = song.lstrip()
            song = song.rstrip()
            song = song.replace(' ', '_')
            return song.capitalize() + '.wav'

    def song_exists(self, song):
        # Checking whether song is present in favourite song folder
        songs_list = os.listdir(FAV_SONGS_DIR)
        song_dir = ""

        if song in songs_list:
             song_dir = FAV_SONGS_DIR

        # Checking whether song is present in other song folder
        songs_list = os.listdir(OTHER_SONGS_DIR)
        if song in songs_list:
             song_dir = OTHER_SONGS_DIR

        return song_dir

    def play_music(self, file, file_path):
        """
        Plays music
        :param file: File name of the music to be played
        :param file_path: Relative path of the song to be played
        """
        os.chdir(file_path)

        # Initializing mixer and loading music file
        pygame.mixer.init()
        pygame.mixer.music.load(file)

        # Initializing player window
        screen = pygame.display.set_mode((self.width, self.height))
        screen.fill(self.background_colour)
        pygame.display.set_caption('Playing: ' + file)
        pygame.display.flip()

        # Playing music
        pygame.mixer.music.play()
        self.running = True

        # Keeping window running while music is played
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        # Closing window when playback is complete
        pygame.display.quit()
        pygame.mixer.quit()
        pygame.quit()

        # Changing to original script directory
        os.chdir(SCRIPT_DIR)


def main():
    music = Music()

    # Getting name of song
    song_name = music.get_song()

    # Playing song if it exists
    dir_name = music.song_exists(song_name)
    if dir_name:
        # Playing requested song
        play_music_thread = Thread(target=music.play_music, args=(song_name, dir_name))
        play_music_thread.start()
    else:
        print("Sorry {} is not present in our collection.".format(song_name))

    # Waiting till thread is completed
    sys.exit(0)


if __name__ == "__main__":
    main()