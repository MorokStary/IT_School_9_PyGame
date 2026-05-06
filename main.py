# Створити ігровий цикл

# Додати FPS: годиник і константу FPS

import pygame
from sys import exit
import random

pygame.init()
#______DISPLAY____________

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Octopus")

clock = pygame.time.Clock()# < -----------

score = 0

#_______PLAYER_SPRITE______
player_speed = 7
is_down = False # 
player_surface = pygame.image.load("Asset/player.png") # .convert_alpha()
player_rect = player_surface.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))

#______COIN_SPRITE______
coin_surface = pygame.image.load("Asset/coin_static.png")
coin_rect = coin_surface.get_rect(
    center = (
        random.randint(50, SCREEN_WIDTH-50),
        random.randint(50, SCREEN_HEIGHT-50)
    )
)

#______buster_SPRITE______
buster_surface = pygame.image.load("Asset/buster.jpg")
buster_rect = buster_surface.get_rect(
    center = (
        random.randint(50, SCREEN_WIDTH-50),
        random.randint(50, SCREEN_HEIGHT-50)
    )
)


#____MAIN LOOP_________
while True:
    
    
    
    # ______________Movement_______________________
    keys = pygame.key.get_pressed()
    
    direction = pygame.math.Vector2(0, 0)
    direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    
    if direction.length() > 0:
        direction = direction.normalize()


    direction.x = direction.x * player_speed
    direction.y = direction.y * player_speed
    
    player_rect.x += direction.x
    player_rect.y += direction.y



    # ______________Events________________________



    # event - це є наша локальна змінна 
    for event in pygame.event.get():

        # Ловим подію виходу з гри і закінчуєм PyGame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pass
        
    # Коли Гравець перетинається з Монетою
    if player_rect.colliderect(coin_rect):
        score = score + 1
        next_x_coin = random.randint(50,SCREEN_WIDTH-50)
        next_y_coin = random.randint(50,SCREEN_HEIGHT-50)


        coin_rect.center=(next_x_coin, next_y_coin)
        print(score)

    # Коли Гравець перетинається з Монетою
    if player_rect.colliderect(buster_rect):
        player_speed += 1
        next_x_buster = random.randint(50,SCREEN_WIDTH-50)
        next_y_buster = random.randint(50,SCREEN_HEIGHT-50)


        buster_rect.center=(next_x_buster, next_y_buster)



    
    screen.fill((30,30,50))



    screen.blit(player_surface,player_rect)
    
    screen.blit(buster_surface,buster_rect)

    screen.blit(coin_surface,coin_rect)

    
    
    pygame.display.update()
    clock.tick(60)# < -----------

