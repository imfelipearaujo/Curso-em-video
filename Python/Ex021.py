#Exercício 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#Precisa copiar o mp3 para dentro do projeto quando for utilizar esse código!

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
