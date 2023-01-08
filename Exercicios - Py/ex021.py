"""        Exercício - 21 ( Tocando um MP3 )
Façaum programa em Python que abra e reproduza o audio de um arquivo MP3  """

import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
