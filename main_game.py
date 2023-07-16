import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LAFALAFI')
clock = pygame.time.Clock()

# test_surface = pygame.Surface((500,80))
# test_surface.fill('Red')
# test_surface2 = pygame.Surface((300,200))
# test_surface2.fill('Green')
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
player_surface = pygame.image.load('graphics/Player/player_stand.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen.blit(test_surface,(0,0))
    # screen.blit(test_surface2,(50,70))
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    screen.blit(player_surface,(20,160))
    pygame.display.update()
    clock.tick(60)
