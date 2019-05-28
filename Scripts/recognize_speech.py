#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:25:20 2019
@author: Pran Kumar Sarkar
"""
__author__ = "Pran Kumar Sarkar"
__version__ = "0.0.1"
__license__ = "BSD"

try:
    import speech_recognition as sr
except Exception:
    print("Could not import speech_recognition.")
    print("Exiting...")
    exit(-1)


class RecognizeSpeech:

    def __init__(self, dynamic_energy_threshold=False, pause_threshold=1):
        """
        Initializes the various threshold for speech recognition.
        """
        self.speech = None
        self.recognizer = sr.Recognizer()

        # Determines the number of seconds of silence to consider as end of speech
        self.recognizer.pause_threshold = pause_threshold

        # For taking care of ambient noise in the background
        self.recognizer.dynamic_energy_threshold = dynamic_energy_threshold


    def recognize_speech(self):
        """
        This module recognizes speech and returns the text form of speech.
        :return:
            (str) self.speech : The decoded speech.
                                None if any error occurs.
        """

        try:
            with sr.Microphone() as source:
                print("Listening...")
                recorded_audio = self.recognizer.listen(source)

                try:
                    print("Decoding speech...")
                    self.speech = self.recognizer.recognize_google(recorded_audio, language="en-in")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                    print("Please speak again.\n")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

        except AttributeError:
            print("Could not find PyAudio 0.2.11 or later. Check installation.")
            print("Exiting...")
            exit(-1)
        except Exception:
            print("Could not access Microphone.")

        return self.speech


if __name__ == "__main__":
    speech_object = RecognizeSpeech()
    speech = speech_object.recognize_speech()
    print(speech)
