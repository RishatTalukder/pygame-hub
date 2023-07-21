import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LAFALAFI')
clock = pygame.time.Clock()

#text_font = pygame.font.SysFont('Arial',22)
text_font = pygame.font.Font('font/Pixeltype.ttf',50)

# test_surface = pygame.Surface((500,80))
# test_surface.fill('Red')
# test_surface2 = pygame.Surface((300,200))
# test_surface2.fill('Green')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,250))
enemy_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
enemy_rect = enemy_surface.get_rect(midbottom = (700,250))
enemy_x_pos = 700

text_surface = text_font.render("LAFALAFI",False,'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen.blit(test_surface,(0,0))
    # screen.blit(test_surface2,(50,70))
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    screen.blit(player_surface,player_rect)
    screen.blit(text_surface,(350,50))
    screen.blit(enemy_surface,enemy_rect)
    enemy_rect.x -= 4
    if enemy_rect.right <= 0: enemy_rect.left = 800
    # enemy_x_pos -= 4
    # if enemy_x_pos < -50:
    #     enemy_x_pos = 900

    pygame.display.update()
    clock.tick(60)
