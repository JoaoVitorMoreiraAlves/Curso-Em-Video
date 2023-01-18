#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.


import pygame

pygame.init()
pygame.mixer.music.load(r'C:\Users\JoaoV\Desktop\MeusProjetos\Curso-Em-Video\Python\Mundo-1\Disco Arranhado.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()