#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:13:17 2019
@author: Pran Kumar Sarkar
"""
__author__ = "Pran Kumar Sarkar"
__version__ = "0.0.1"
__license__ = "BSD"

from datetime import datetime
from recognize_speech import RecognizeSpeech
from speak import Speak


class Sara:

    def __init__(self):
        # Initializing speech recognition engine
        self.speech_recognition_object = RecognizeSpeech()

        # Initializing TTS engine
        self.speak_object = Speak()

    def listen(self):
        """
        This function returns decoded speech
        :return:
            (str) speech : The decoded speech.
        """
        speech = self.speech_recognition_object.recognize_speech()
        return speech

    def speak(self, text):
        """
        Converts text to speech and speaks aloud
        :param text: The text to speak.
        """
        self.speak_object.speak(text)

    def get_time(self):
        """
        :return: (str) Current time in 12 hour format.
        """
        time = datetime.now()
        if time.hour < 12:
            time = (str)(time.hour) + ":" + (str)(time.minute) + " AM"
        else:
            time = (str)(time.hour) + ":" + (str)(time.minute) + " PM"
        return time

    def generate_greetings(self):
        """
        Generates greetings based upon time.

        :return: (str) Greetings.
        """
        greetings = "Good "
        time = datetime.now()
        if time.hour >= 0 and time.hour < 12:
            greetings = greetings + "Morning"
        elif time.hour >= 12 and time.hour < 18:
            greetings = greetings + "Afternoon"
        elif time.hour >= 18 and time.hour <= 24:
            greetings = greetings + "Night"
        return greetings

    def introduction(self):
        """
        :return: (str) Introduction speech with greetings.
        """
        text = "Hi, " + self.generate_greetings() + "."
        text = text + " I am Sara, and how can I help you?\n"
        return text

if __name__ == "__main__":
    sara = Sara()

    # Printing and speaking introductory speech.
    print(sara.introduction())
    sara.speak(sara.introduction())

    # Listening and executing commands
    while(1):
        command = sara.listen()

        # If command is decodable then proceeding else listening again
        if command:
            command = command.lower()
        else:
            continue

        # Exiting on sleep now command
        if "sleep" in command and "now" in command:
            exit_text = "\nOkay! It's been nice assisting you. Take care. Bye."
            print(exit_text)
            sara.speak(exit_text)
            exit(0)
