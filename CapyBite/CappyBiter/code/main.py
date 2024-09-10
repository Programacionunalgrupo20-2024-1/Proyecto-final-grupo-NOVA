import pygame
import os
from settings import width, height, white
from codegame import game_loop
from music import high_score_sound

# Inicializar pygame
pygame.init()

# Crear la pantalla con resolución de celular
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CapyBite")

# Función para cargar el puntaje más alto desde un archivo
def load_high_score(file_path="high_score.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0

# Función para guardar el puntaje más alto en un archivo
def save_high_score(score, file_path="high_score.txt"):
    with open(file_path, "w") as file:
        file.write(str(score))

# Inicializar el puntaje más alto
high_score = load_high_score()

# Función para el menú principal
def main_menu():
    global high_score
    menu = True
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
                        save_high_score(high_score)  # Guardar el nuevo puntaje más alto
                        high_score_sound.play()

        screen.fill(white)

        font = pygame.font.SysFont("Coffee Spark", 60)
        text = font.render("CapyBite", True, ("#f7b483"))
        text_rect = text.get_rect(center=(180, 320))
        screen.blit(text, text_rect)

        font = pygame.font.SysFont("Boba Milky", 20)
        text = font.render("Press SPACE to Start", True, ("#de6a3f"))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

        font_small = pygame.font.SysFont("Boba Milky", 25)
        high_score_text = font_small.render(f"HighScore: {high_score}", True, ("#de6a3f"))
        screen.blit(high_score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_menu()