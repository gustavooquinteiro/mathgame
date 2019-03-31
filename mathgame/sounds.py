import pygame
import time
import math
import os

class Sound():

    def __init__(self, path='sounds'):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.mixer.init()
        self.sound_library ={}
        self.playlist= []
        self.load_library(path)
        self.init_playlist()

    def load_library(self, path):
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                self.sound_library[path+ os.sep +file] = file

    def init_playlist(self):
        for music in self.sound_library:
            self.playlist.append(music)
        self.playlist = self.playlist[1:]+ [self.playlist[0]]
        pygame.mixer.music.load(self.playlist[0])
        self.play_music()

    def next_song(self):
        if not self.playlist:
            self.init_playlist()
        else:
            self.fadeout(3)
            self.playlist = self.playlist[1:]+ [self.playlist[0]]
            pygame.mixer.music.queue(self.playlist.pop())
            self.play_music()

    def play_music(self):
        pygame.mixer.music.set_volume(.6)
        pygame.mixer.music.play()

    def stop_music(self):
        self.fadeout(1)
        pygame.mixer.music.stop()

    def fadeout(self, tempo):
        volume = pygame.mixer.music.get_volume()
        while tempo > 0:
            time.sleep(tempo)
            tempo -= 1
            volume -= .1618
            pygame.mixer.music.set_volume(volume)
