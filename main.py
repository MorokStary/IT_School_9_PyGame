# Створити ігровий цикл

# Додати FPS: годиник і константу FPS

import pygame
from sys import exit


pygame.init()
#______DISPLAY____________
screen = pygame.display.set_mode((400,800))
pygame.display.set_caption("Octopus")

clock = pygame.time.Clock()# < -----------


while True:
    # event - це є наша локальна змінна 
    for event in pygame.event.get():

        # Ловим подію виходу з гри і закінчуєм PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pass

    

    pygame.display.update()
    clock.tick(60)# < -----------

