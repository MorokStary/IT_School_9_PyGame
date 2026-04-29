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
player_speed = 7
is_down = False # 
player_surface = pygame.image.load("Asset/player.png") # .convert_alpha()
player_rect = player_surface.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))

#____MAIN LOOP_________
while True:
    
    
    
    ## ______________Movement_______________________
    #keys = pygame.key.get_pressed()
    #
    #direction = pygame.math.Vector2(0, 0)
    #direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    #direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    #
    #if direction.length() > 0:
    #    direction = direction.normalize()
#
#
    #direction.x = direction.x * player_speed
    #direction.y = direction.y * player_speed
    #
    #player_rect.x += direction.x
    #player_rect.y += direction.y



    # ______________Movement_______________________
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        is_down = not is_down # False + not - True |   True + not = False
        pygame.time.delay(100)
    direction = pygame.math.Vector2(0, 0)
    
    if is_down:
        direction.y += 1
    else:
        direction.y -= 1

        
    
    if direction.length() > 0:
        direction = direction.normalize()
    
    player_rect.y+=direction.y*player_speed



    #direction.x = direction.x * player_speed
    #direction.y = direction.y * player_speed
    #
    #player_rect.x += direction.x
    #player_rect.y += direction.y

    # ______________Events________________________



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

