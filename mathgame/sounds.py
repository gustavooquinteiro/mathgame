import pygame
import time
import math
import os

class Sound():

    def __init__(self, path='sounds'):
        #frequency, size, channels, buffersize
        pygame.mixer.pre_init(44100, 16, 2, 4096) 
        pygame.mixer.init()
        
        self.sound_library = {}
        self.playlist= []
        
        self.load_library(path)
        self.init_playlist()

    def load_library(self, path):
        if os.path.isdir(path):
            files = os.listdir(path)
            for song in files:
                exploded_file = song.split('.')
                extension = exploded_file[-1]
                if extension == "mp3" or extension == "wav":
                    self.sound_library[path + os.sep + song] = song

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
            self.fadeout()
            self.playlist = self.playlist[1:]+ [self.playlist[0]]
            pygame.mixer.music.load(self.playlist[0])
            self.play_music()

    def play_music(self):
        pygame.mixer.music.set_volume(.6)
        pygame.mixer.music.play()

    def stop_music(self):
        self.fadeout()
        pygame.mixer.music.stop()

    def fadeout(self):
        volume = pygame.mixer.music.get_volume()
        n = 2
        while volume > 0.35:
            volume -= (1/ (2 << n))            
            pygame.mixer.music.set_volume(volume)
            time.sleep(round(volume,1) * 10)
            n += 1
        time.sleep(4)
