import pygame
import os
from settings import *
from codegame import *
from music import *

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CapyBite")
pygame.display.set_icon(icono_image)

def load_high_score(file_path="high_score.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0

def save_high_score(score, file_path="high_score.txt"):
    with open(file_path, "w") as file:
        file.write(str(score))

high_score = load_high_score()

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, (terracota), rect, 5)
    font = pygame.font.SysFont("Holy Friday", 25)
    text_surface = font.render(text, True, (coffee))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def show_instructions(screen):
    instructions = [
        "Instrucciones:",
        "",
        "Para moverte usa",
        "las flechas (teclas)",
        "de dirección del teclado.",
        "",
        "",
        "",
        "Objetivos del juego:",
        "",
        "Debes recolectar la comida",
        "Evitar que se caiga",
        "No comer las basuras",
        "",
        "",
        "",
        "Presiona ESC para salir al menú"
    ]
    screen.fill(white)
    screen.blit(background_instrucciones_image, (0, 0))
    font = pygame.font.SysFont("Holy Friday", 25)

    for i, line in enumerate(instructions):
        text = font.render(line, True, (coffee))
        screen.blit(text, (width // 2 - text.get_width() // 2, 100 + i * 30))

    pygame.display.update()

    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def show_credits(screen):
    credits = [
        "Créditos:",
        "Desarrollado por:",
        "Maria Jose Garcia Macias",
        "Sebastian Toro Vanegas",
        "y",
        "Sergio Hernandez Lopez",
        "",
        "Assets hechos por:",
        "Maria Jose Garcia Macias",
        "",
        "Fondo por:",
        "Sergio Hernandez Lopez",
        "",
        "",
        "",
        "Presiona ESC para salir al menú"
    ]
    screen.fill(white)
    screen.blit(background_instrucciones_image, (0, 0))
    font = pygame.font.SysFont("Holy Friday", 25)

    for i, line in enumerate(credits):
        text = font.render(line, True, (coffee))
        screen.blit(text, (width // 2 - text.get_width() // 2, 100 + i * 30))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

def main_menu():
    global high_score
    menu = True

    button_width, button_height = 180, 40
    button_instructions = pygame.Rect(width // 2 - button_width // 2, height // 2 + 80, button_width, button_height)
    button_credits = pygame.Rect(width // 2 - button_width // 2, height // 2 + 140, button_width, button_height)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = game_loop(screen)
                    if score is not None and score > high_score:
                        high_score = score
                        save_high_score(high_score)
                        high_score_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_instructions.collidepoint(event.pos):
                    show_instructions(screen)
                if button_credits.collidepoint(event.pos):
                    show_credits(screen)

        screen.fill(white)
        screen.blit(background_menu_image, (0, 0))

        font = pygame.font.SysFont("Coffee Spark", 60)
        text = font.render("CapyBite", True, (peach))
        text_rect = text.get_rect(center=(width // 2, height // 2.29))
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("Boba Milky", 20)
        text = font.render("Press SPACE to Start", True, (terracota))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

        font_small = pygame.font.SysFont("Boba Milky", 25)
        high_score_text = font_small.render(f"HighScore: {high_score}", True, (terracota))
        screen.blit(high_score_text, (10, 10))

        draw_button(screen, button_instructions, "Instrucciones")
        draw_button(screen, button_credits, "Créditos")

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_menu()