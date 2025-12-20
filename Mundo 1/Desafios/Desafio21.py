# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# python -m pip install pygame no cmd.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex1.mp3') # Substitua 'ex1.mp3' pelo caminho do seu arquivo de áudio
pygame.mixer.music.play()
input('Agora você escuta a música, Maior é o Amor!')