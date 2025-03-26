import pygame
pygame.init()
pygame.mixer.music.load('kanye.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
input()
pygame.event.wait()
