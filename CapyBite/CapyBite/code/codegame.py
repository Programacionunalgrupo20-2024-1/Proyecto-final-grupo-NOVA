import pygame
import random
import time
from settings import *
from assets import *
from music import *

clock = pygame.time.Clock()

def show_score(screen, score):
    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, (coffee))
    screen.blit(score_text, (10, 10))

def detect_collision(player_pos, obj_pos, obj_size):
    p_x = player_pos[0]
    p_y = player_pos[1]

    o_x = obj_pos[0]
    o_y = obj_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obj_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obj_size)):
            return True
    return False

def game_over_screen(screen, score, game_over_sound):
    screen.fill(white)
    screen.blit(background_game_over_image, (0, 0))

    font = pygame.font.SysFont("Coffee Spark", 60)
    game_over_text = font.render("Game Over", True, (peach))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 55))

    font = pygame.font.SysFont("Boba Milky", 25)
    score_text = font.render(f"Score: {score}", True, (terracota))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))

    pygame.display.update()

    pygame.time.wait(2000)

def game_loop(screen):
    player_pos = [width // 2, height - 2 * player_size]

    food_pos = [random.randint(0, width - food_size), 0]
    basura_pos = [random.randint(0, width - basura_size), -height // 2]

    score = 0
    food_speed = 5  
    max_food_speed = 20  

    current_food_image = random.choice(food_images)
    current_basura_image = random.choice(basura_images)

    player_index = 0
    player_image_change_time = time.time() 
    animation_delay = 0.5  
    game_over = False
    moving_left = True  

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_pos[0] -= player_speed
                    moving_left = True  
                if event.key == pygame.K_RIGHT:
                    player_pos[0] += player_speed
                    moving_left = False 

        if player_pos[0] < 0:
            player_pos[0] = 0
        if player_pos[0] > width - player_size:
            player_pos[0] = width - player_size

        if score > 0 and score % 6 == 0 and food_speed < max_food_speed:
            food_speed += 0.1

        food_pos[1] += food_speed
        basura_pos[1] += food_speed

        if food_pos[1] > height:
            game_over_sound.play()
            game_over_screen(screen, score, game_over_sound)
            return score

        if basura_pos[1] > height:
            basura_pos = [random.randint(0, width - basura_size), -height // 2]
            current_basura_image = random.choice(basura_images)

        if detect_collision(player_pos, food_pos, food_size):
            score += 1
            food_pos = [random.randint(0, width - food_size), 0]
            current_food_image = random.choice(food_images)
            recolectar_comida_sound.play()

        if detect_collision(player_pos, basura_pos, basura_size):
            game_over_sound.play()
            game_over_screen(screen, score, game_over_sound)
            return score

        current_time = time.time()
        if current_time - player_image_change_time > animation_delay:
            player_index = (player_index + 1) % len(player_images_left)
            player_image_change_time = current_time

        screen.fill(white)
        screen.blit(background_image, (0, 0))

        if moving_left:
            screen.blit(player_images_left[player_index], (player_pos[0], player_pos[1]))
        else:
            screen.blit(player_images_right[player_index], (player_pos[0], player_pos[1]))

        screen.blit(current_food_image, (food_pos[0], food_pos[1]))

        screen.blit(current_basura_image, (basura_pos[0], basura_pos[1]))

        show_score(screen, score)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
