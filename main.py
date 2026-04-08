# Створити ігровий цикл

# Додати FPS: годиник і константу FPS

import pygame
from sys import exit


pygame.init()
#______DISPLAY____________

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Octopus")

clock = pygame.time.Clock()# < -----------

#_______PLAYER_SPRITE______


player_surface = pygame.image.load("Asset/player.png") # .convert_alpha()
player_rect = player_surface.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))

#__________________________


while True:
    # event - це є наша локальна змінна 
    for event in pygame.event.get():

        # Ловим подію виходу з гри і закінчуєм PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pass

    
    screen.fill((30,30,50))

    screen.blit(player_surface,player_rect)
    pygame.display.update()
    clock.tick(60)# < -----------

