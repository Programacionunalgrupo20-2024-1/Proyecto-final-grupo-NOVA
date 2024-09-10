import pygame
import random
import time
from settings import width, height, white, player_speed, fps
from assets import player_images_left, player_images_right, food_images, player_size, food_size, basura_images, basura_size
from music import recolectar_comida_sound, game_over_sound

# FPS
clock = pygame.time.Clock()

#imagen de fondo

background_image = pygame.image.load("../graphics/Fondo/fondo.png")

# Función para mostrar el puntaje
def show_score(screen, score):
    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, ("#de6a3f"))
    screen.blit(score_text, (10, 10))

# Función para detectar colisiones
def detect_collision(player_pos, obj_pos, obj_size):
    p_x = player_pos[0]
    p_y = player_pos[1]

    o_x = obj_pos[0]
    o_y = obj_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obj_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obj_size)):
            return True
    return False

# Función para mostrar la pantalla de Game Over
def game_over_screen(screen, score, game_over_sound):
    screen.fill(white)

    font = pygame.font.SysFont("Coffee Spark", 60)
    game_over_text = font.render("Game Over", True, ("#f7b483"))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 55))

    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, ("#de6a3f"))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))

    pygame.display.update()

    # Esperar unos segundos antes de volver al menú principal
    pygame.time.wait(2000)

def game_loop(screen):
    player_pos = [width // 2, height - 2 * player_size]
    
    # Posiciones iniciales para comida y basura
    food_pos = [random.randint(0, width - food_size), 0]
    basura_pos = [random.randint(0, width - basura_size), -height // 2]  # Basura empieza más arriba de la pantalla

    score = 0
    food_speed = 5  # Velocidad inicial de la comida
    max_food_speed = 20  # Velocidad máxima de la comida

    # Seleccionar aleatoriamente comida y basura para comenzar
    current_food_image = random.choice(food_images)
    current_basura_image = random.choice(basura_images)

    player_index = 0
    player_image_change_time = time.time()  # Tiempo actual en segundos
    animation_delay = 0.5  # Tiempo en segundos para cambiar la imagen
    game_over = False
    moving_left = True  # Indicador de la dirección del jugador, por defecto a la izquierda

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_pos[0] -= player_speed
                    moving_left = True  # Cambia a assets de movimiento hacia la izquierda
                if event.key == pygame.K_RIGHT:
                    player_pos[0] += player_speed
                    moving_left = False  # Cambia a assets de movimiento hacia la derecha

        # Limitar el movimiento del jugador para que no salga de la pantalla
        if player_pos[0] < 0:
            player_pos[0] = 0
        if player_pos[0] > width - player_size:
            player_pos[0] = width - player_size

        # Aumentar la velocidad de la comida en incrementos de 0.1 cada 3 puntos, hasta un máximo de 20
        if score > 0 and score % 3 == 0 and food_speed < max_food_speed:
            food_speed += 0.1

        # Actualizar la posición de la comida y la basura
        food_pos[1] += food_speed
        basura_pos[1] += food_speed

        # Si la comida se sale de la pantalla, mostrar Game Over
        if food_pos[1] > height:
            game_over_sound.play()
            game_over_screen(screen, score, game_over_sound)
            return score  # El juego termina si la comida se sale de la pantalla

        # Si la basura se sale de la pantalla, reaparece pero más arriba para que caiga espaciada
        if basura_pos[1] > height:
            basura_pos = [random.randint(0, width - basura_size), -height // 2]
            current_basura_image = random.choice(basura_images)

        # Detectar colisiones con la comida
        if detect_collision(player_pos, food_pos, food_size):
            score += 1
            food_pos = [random.randint(0, width - food_size), 0]
            current_food_image = random.choice(food_images)
            recolectar_comida_sound.play()

        # Detectar colisiones con la basura (esto causa game over)
        if detect_collision(player_pos, basura_pos, basura_size):
            game_over_sound.play()
            game_over_screen(screen, score, game_over_sound)
            return score  # El juego termina si se toca la basura

        # Actualizar el ciclo de animación del jugador
        current_time = time.time()
        if current_time - player_image_change_time > animation_delay:
            player_index = (player_index + 1) % len(player_images_left)  # Usamos el tamaño de cualquier lista
            player_image_change_time = current_time

        # Rellenar el fondo con color blanco
        screen.fill(white)

        # Seleccionar la imagen del jugador según la dirección del movimiento
        if moving_left:
            screen.blit(player_images_left[player_index], (player_pos[0], player_pos[1]))
        else:
            screen.blit(player_images_right[player_index], (player_pos[0], player_pos[1]))

        # Dibujar la comida usando la imagen seleccionada
        screen.blit(current_food_image, (food_pos[0], food_pos[1]))

        # Dibujar la basura usando la imagen seleccionada
        screen.blit(current_basura_image, (basura_pos[0], basura_pos[1]))

        # Mostrar el puntaje
        show_score(screen, score)

        # Actualizar la pantalla
        pygame.display.update()

        # Configurar los FPS
        clock.tick(fps)

    pygame.quit()
