import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input('Aperte Enter para parar a música')
pygame.event.wait()
pygame.mixer.music.stop()


