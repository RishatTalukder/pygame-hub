import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()//1000-starting_time
    score_surface = text_font.render("score: " + str(current_time),False,(103,103,103))
    score_rect = score_surface.get_rect(center= (400,100))
    screen.blit(score_surface,score_rect)


pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LAFALAFI')
clock = pygame.time.Clock()
game_active = False
starting_time = 0
#text_font = pygame.font.SysFont('Arial',22)
text_font = pygame.font.Font('font/Pixeltype.ttf',50)

# test_surface = pygame.Surface((500,80))
# test_surface.fill('Red')
# test_surface2 = pygame.Surface((300,200))
# test_surface2.fill('Green')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
#player_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,250))


player_stand_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()

player_stand_surface = pygame.transform.rotozoom(player_stand_surface,0,2)
player_stand_rect = player_stand_surface.get_rect(center=(400,200))




gravity = 0
enemy_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
enemy_rect = enemy_surface.get_rect(midbottom = (700,250))
enemy_x_pos = 700

text_surface = text_font.render("LAFALAFI",False,(111,200,233))
text_rect = text_surface.get_rect(center= (400,80))

massage_text = text_font.render("PRESS SPACE TO PLAY",False,(11,200,233))
massege_rect = massage_text.get_rect(center=(400,350))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("down")

        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("UP")

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

        if game_active:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 250:
                    gravity = -20

            if event.type == pygame.KEYUP:
                pass

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.left = 800
                    starting_time = pygame.time.get_ticks()//1000

    # screen.blit(test_surface,(0,0))
    # screen.blit(test_surface2,(50,70))
    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,250))
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 250:
            player_rect.bottom = 250
        screen.blit(player_surface,player_rect)
        display_score()
        #screen.blit(text_surface,(350,50))
        screen.blit(enemy_surface,enemy_rect)
        enemy_rect.x -= 4
        if enemy_rect.right <= 0: enemy_rect.left = 800

        if enemy_rect.colliderect(player_rect):
            # pygame.quit()
            # exit()
           game_active = False

    else:
        screen.fill((94,103,212)) 
        screen.blit(player_stand_surface,player_stand_rect)
        screen.blit(text_surface,text_rect)
        screen.blit(massage_text,massege_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("JUMp")


    # enemy_x_pos -= 4
    # if enemy_x_pos < -50:
    #     enemy_x_pos = 900

    # if player_rect.colliderect(enemy_rect):
    #     print("collision")

    # mouse_position = pygame.mouse.get_pos()
    
    # print(player_rect.collidepoint(mouse_position))

    # print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
