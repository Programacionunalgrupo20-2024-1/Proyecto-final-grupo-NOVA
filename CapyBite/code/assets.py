import pygame

# Cargar imágenes del personaje animado

player_images_left = [
    pygame.image.load("../graphics/Capy_Izquierda/0.png"),
    pygame.image.load("../graphics/Capy_Izquierda/1.png"),
    pygame.image.load("../graphics/Capy_Izquierda/2.png")
]

# Cargar imágenes del personaje animado
player_images_right = [
    pygame.image.load("../graphics/Capy_Derecha/0.png"),
    pygame.image.load("../graphics/Capy_Derecha/1.png"),
    pygame.image.load("../graphics/Capy_Derecha/2.png")
]

# Escalar las imágenes del personaje si es necesario
player_size = 64
player_images = [pygame.transform.scale(img, (player_size, player_size)) for img in player_images_left and player_images_right]

# Cargar imágenes de la comida
food_images = [
    pygame.image.load("../graphics/comida/Hoja.png"),
    pygame.image.load("../graphics/comida/Manzana.png"),
    pygame.image.load("../graphics/comida/Sandia.png"),
    pygame.image.load("../graphics/comida/Zanahoria.png") 
]

# Escalar las imágenes de la comida si es necesario
food_size = 32
food_images = [pygame.transform.scale(img, (food_size, food_size)) for img in food_images]


# Cargar imágenes de basura
basura_images = [
    pygame.image.load("../graphics/Basura/Basura.png"),
    pygame.image.load("../graphics/Basura/Lata.png"),
    pygame.image.load("../graphics/Basura/Manzana podrida.png"),
    pygame.image.load("../graphics/Basura/Toxico.png")
]

# Escalar las imágenes de basura si es necesario
basura_size = 30
basura_images = [pygame.transform.scale(img, (basura_size, basura_size)) for img in basura_images]
