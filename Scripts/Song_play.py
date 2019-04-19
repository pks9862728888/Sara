#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thr April 18 18:18:20 2018

@author: Pran Kumar Sarkar
"""

import os
import sys
import pygame
import speech_recognition as sr
from threading import Thread

# Defining global variables
SCRIPT_DIR = os.getcwd()

# Making path to work with linux and windows
if '/' in SCRIPT_DIR:
    SONGS_DIR = "../Songs/"
    FAV_SONGS_DIR = "../Songs/Favourite/"
else:
    SONGS_DIR = "..\\Songs\\"
    FAV_SONGS_DIR = "..\\Songs\\Favourite\\"


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
        """
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Name the song you want to play")

            try:
                audio = recognizer.listen(source, timeout=5.0)
                print("Here")

                song = recognizer.recognize_google(audio)
            except sr.WaitTimeoutError as e:
                print(e)
                song = -1
            except sr.UnknownValueError:
                print("Could not understand audio")
                song = -1
            except sr.RequestError as e:
                print("Could not request results: {0}".format(e))
                song = -1

            return song

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
    print(song_name)

    # Playing favourite song in a thread
    play_music_thread = Thread(target=music.play_music, args=("Theres_no_limit.wav", FAV_SONGS_DIR))
    play_music_thread.start()

    # Waiting till thread is completed
    sys.exit(0)


if __name__ == "__main__":
    main()
