import pygame

pygame.mixer.init()

pygame.mixer.music.load("../music/Musica.mp3")
pygame.mixer.music.play(-1) #Sonido infinito (-1)
pygame.mixer.music.set_volume(0.2) #Volumen de la musica

recolectar_comida_sound = pygame.mixer.Sound("../music/Recolectar.mp3")
high_score_sound = pygame.mixer.Sound("../music/HighScore.mp3")
game_over_sound = pygame.mixer.Sound("../music/GameOver.mp3")