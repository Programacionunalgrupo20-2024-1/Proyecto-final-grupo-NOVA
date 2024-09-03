import pygame
import random
from settings import *
from assets import *
from music import *

# FPS
clock = pygame.time.Clock()

# Función para mostrar el puntaje
def show_score(screen, score):
    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, (terracotta))
    screen.blit(score_text, (10, 10))

# Función para detectar colisiones
def detect_collision(player_pos, food_pos, recolectar_comida_sound):
    p_x = player_pos[0]
    p_y = player_pos[1]

    f_x = food_pos[0]
    f_y = food_pos[1]

    if (f_x >= p_x and f_x < (p_x + player_size)) or (p_x >= f_x and p_x < (f_x + food_size)):
        if (f_y >= p_y and f_y < (p_y + player_size)) or (p_y >= f_y and p_y < (f_y + food_size)):
            return True
    return False

# Función para mostrar la pantalla de Game Over
def game_over_screen(screen, score, game_over_sound):
    screen.fill(white)

    font = pygame.font.SysFont("Coffee Spark", 60)
    game_over_text = font.render("Game Over", True, (peach))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 55))

    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, (terracotta))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))

    pygame.display.update()

    # Esperar unos segundos antes de volver al menú principal
    pygame.time.wait(2000)

def game_loop(screen):
    player_pos = [width // 2, height - 2  * player_size]
    food_pos = [random.randint(0, width - food_size), 0]
    score = 0

    # Seleccionar aleatoriamente una comida para comenzar
    current_food_image = random.choice(food_images)

    player_index = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_pos[0] -= player_speed
                if event.key == pygame.K_RIGHT:
                    player_pos[0] += player_speed

        # Actualizar la posición de la comida
        food_pos[1] += food_speed

        # Si la comida se sale de la pantalla, termina el juego
        if food_pos[1] > height:
            game_over_sound.play()
            game_over_screen(screen, score, game_over_sound)
            return score  # Devuelve el puntaje obtenido para guardarlo

        # Detectar colisiones
        if detect_collision(player_pos, food_pos, recolectar_comida_sound):
            score += 1
            food_pos = [random.randint(0, width - food_size), 0]
            current_food_image = random.choice(food_images)  # Cambiar la comida
            recolectar_comida_sound.play()

        # Rellenar el fondo con color blanco
        screen.fill(white)

        # Dibujar personaje animado
        screen.blit(player_images[player_index], (player_pos[0], player_pos[1]))

        # Ciclo de animación del personaje
        player_index = (player_index + 1) % len(player_images)

        # Dibujar la comida usando la imagen seleccionada
        screen.blit(current_food_image, (food_pos[0], food_pos[1]))

        # Mostrar el puntaje
        show_score(screen, score)

        # Actualizar la pantalla
        pygame.display.update()

        # Configurar los FPS
        clock.tick(fps)

    pygame.quit()
