#pygame screen
from sys import exit
import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Hello World', True, (255,25,255))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700,300))

snail_x_position = 600


player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

player_rect = player_surface.get_rect(midbottom = (80,300))

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_rect.right -= 4

    if snail_rect.right <=0:
        snail_rect.left = 800
    
    screen.blit(snail_surface,snail_rect)
    player_rect.left += 2
    screen.blit(player_surface,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("shit")
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)

