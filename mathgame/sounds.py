import pygame
import time
import math
import os
import youtube_dl
from constants import SOUNDTRACK, DL_OPTIONS, SCREEN_HEIGHT, SCREEN_WIDTH, BLUE

class Sound():

    def __init__(self, path='sounds'):
        #frequency, size, channels, buffersize
        pygame.mixer.pre_init(44100, 16, 2, 4096) 
        pygame.mixer.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]

        self.screen = pygame.display.set_mode(size)
        self.progress = 0
        self.sound_library = {}
        self.playlist= []
        
        self.load_library(path)
        self.init_playlist()

    def load_library(self, path):
        self.progress += 140
        self.progress_bar()
        if os.path.isdir(path):
            files = os.listdir(path)
            cont = 0
            for song in files:
                exploded_file = song.split('.')
                extension = exploded_file[-1]
                if extension == "mp3" or extension == "wav":
                    self.sound_library[path + os.sep + song] = song
                    cont += 1
                self.progress += ((cont * 100) / len(files)) * math.pi
                self.progress_bar()
        else:
            os.mkdir(path)
            os.chdir(path)
            cont = 0
            with youtube_dl.YoutubeDL(DL_OPTIONS) as dl:
                    for music in SOUNDTRACK:
                        dl.download([music])
                        cont += 1
                        self.progress += ((cont * 100) / len(SOUNDTRACK)) * math.pi
                        self.progress_bar()
                        
            os.chdir('../')
            self.load_library(path)
        

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
        pygame.mixer.music.set_volume(.75)
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
    
    def progress_bar(self):
        width = ((self.progress * 100) / SCREEN_WIDTH) * ((1 + math.sqrt(5)) / 2) * math.pi
        pygame.draw.rect(self.screen,
                         BLUE,
                         pygame.Rect(30,
                                     SCREEN_HEIGHT - 20,
                                     width,
                                     SCREEN_HEIGHT /4))
        pygame.display.update()
        time.sleep(1)
