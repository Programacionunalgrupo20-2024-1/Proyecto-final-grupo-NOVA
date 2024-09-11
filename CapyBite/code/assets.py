import pygame

player_images_left = [
    pygame.image.load("../graphics/capy izquierda/0.png"),
    pygame.image.load("../graphics/capy izquierda/1.png"),
    pygame.image.load("../graphics/capy izquierda/2.png")
]

player_images_right = [
    pygame.image.load("../graphics/capy derecha/0.png"),
    pygame.image.load("../graphics/capy derecha/1.png"),
    pygame.image.load("../graphics/capy derecha/2.png")
]

player_size = 64
player_images = [pygame.transform.scale(img, (player_size, player_size)) for img in player_images_left and player_images_right]

food_images = [
    pygame.image.load("../graphics/comida/Hoja.png"),
    pygame.image.load("../graphics/comida/Manzana.png"),
    pygame.image.load("../graphics/comida/Sandia.png"),
    pygame.image.load("../graphics/comida/Zanahoria.png") 
]

food_size = 32
food_images = [pygame.transform.scale(img, (food_size, food_size)) for img in food_images]

basura_images = [
    pygame.image.load("../graphics/basura/Basura.png"),
    pygame.image.load("../graphics/basura/Lata.png"),
    pygame.image.load("../graphics/basura/Manzana podrida.png"),
    pygame.image.load("../graphics/basura/Toxico.png")
]

basura_size = 30
basura_images = [pygame.transform.scale(img, (basura_size, basura_size)) for img in basura_images]

background_image = pygame.image.load("../graphics/fondo/fondo.png")
background_menu_image = pygame.image.load("../graphics/fondo/fondo menu.png")
background_game_over_image = pygame.image.load("../graphics/fondo/fondo game over.png")
background_instrucciones_image = pygame.image.load("../graphics/fondo/fondo instrucciones.png")

icono_image = pygame.image.load("../graphics/icono/icono.png")
