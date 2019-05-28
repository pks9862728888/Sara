#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:29:17 2019
@author: Pran Kumar Sarkar
"""
__author__ = "Pran Kumar Sarkar"
__version__ = "0.0.1"
__license__ = "BSD"

try:
    import pyttsx3
except Exception:
    print("Could not find pyttsx3. Check installation.")
    print("Exiting...")
    exit(-1)


class Speak:

    def __init__(self, tts_engine='sapi5', volume=1.0, rate=127, voice_serial_number=1):
        """
        Initializes the speech engine.
        :param tts_engine: The name of the TTS engine to use. Default is sapi5
        :param volume: The volume of speech. Default is 1.0
        :param rate: The rate of speech. Default is 126
        :param voice_serial_number: The voice to select. 0 = Male voice, 1 = Female(default)
        """
        try:
            # Initializing engine and selecting TTS engine
            self.engine = pyttsx3.init(tts_engine)

            # Initializing volume
            self.set_volume(volume)

            # Initializing speech rate
            self.set_speech_rate(rate)

            # Setting the voice
            self.voices = self.engine.getProperty('voices')
            self.set_voice(voice_serial_number)
        except Exception:
            print("Error!!! Could not initialize speech engine.")
            print("Exiting...")
            exit(-1)

    def speak(self, text_to_speak):
        """
        Speaks the text to speak
        :param text_to_speak: Text to speak.
        """
        try:
            self.engine.say(text_to_speak)
            self.engine.runAndWait()
            self.engine.stop()
        except Exception as e:
            print("Error! Could not speak.")
            print(f"Error info: {e}")

    def set_volume(self, volume=1.0):
        """
        Sets volume of speech.

        :param volume: The requied volume of speech. Default is 1.0
        """
        self.engine.setProperty('volume', volume)

    def set_speech_rate(self, rate=127):
        """
        Sets the speech rate.

        :param rate: The rate of speech. Default is 126
        """
        self.engine.setProperty('rate', rate)

    def set_voice(self, voice_serial_number=1):
        """
        Sets the voice to speak.
        :param voice_serial_number: The serial number of installed voices.
                                    0 : Male voice
                                    1 : Female voice(default)
        """
        self.engine.setProperty('voice', self.voices[voice_serial_number].id)

    def get_volume(self):
        """
        :return: The current volume.
        """
        return self.engine.getProperty('volume')

    def get_speech_rate(self):
        """
        :return: The current speech rate.
        """
        return self.engine.getProperty('rate')

    def get_voice(self):
        """
        :return: The current voice used.
        """
        return self.engine.getProperty('voice')

    def print_details(self):
        """
        Prints current configuration of speech engine.
        """
        print(f"Current voice details: {self.get_voice()}")
        print(f"Volume : {self.get_volume()}")
        print(f"Speech rate : {self.get_speech_rate()}")

    def stop_engine(self):
        """
        Stops the engine.
        """
        self.engine.stop()

if __name__ == "__main__":
    speak = Speak()
    speak.speak("Hi, I am Sara and I can speak now.")
    speak.speak("Isn't it cool?")
    del speak