import pygame
from pygame.locals import *
from sys import exit

pygame.init()

player_width = 20
player_height = 50

width = 640 
height = 480

player_one_x = 30
player_one_y = int(height/2)-int(player_height/2)
player_one_points = 0

player_two_x = int(width-30)
player_two_y = int(height/2)-int(player_height/2)
player_two_points = 0

line_one = [int(width/2),0]
line_two = [int(width/2), height]

cicle_x = int(width/2)
cicle_y = int(height/2)

reset_cicle_x = int(width/2)
reset_cicle_y = int(height/2)

font = pygame.font.SysFont("arial", 40, True, True)

screen = pygame.display.set_mode((width, height))

black_color = (0,0,0)
red_color = (255,0,0)
green_color = (0,255,0)
white_color = (255,255,255)
blue_color = (0,0,255)

clock = pygame.time.Clock()

vertical_move_cicle = True
horizontal_move_cicle = True

def cicle_up():
    global cicle_y, vertical_move_cicle
    if cicle_y <= 10:
        vertical_move_cicle = False
    cicle_y -= 7

def cicle_down():
    global cicle_y, vertical_move_cicle
    if cicle_y >= (height-10):
        vertical_move_cicle = True
    cicle_y += 7


while True:
    clock.tick(30)
    screen.fill(black_color)
    points_one = (f'{player_one_points}')
    fotmated_points_player_one = font.render(points_one, True, green_color)
    points_two = (f'{player_two_points}')
    fotmated_points_player_two = font.render(points_two, True, blue_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    player_one = pygame.draw.rect(screen, red_color,(player_one_x, player_one_y, player_width,player_height))
    player_two = pygame.draw.rect(screen, red_color,(player_two_x, player_two_y, player_width,player_height))

    line = pygame.draw.line(screen, white_color,line_one,line_two, 5)

    ball = pygame.draw.circle(screen, white_color, (cicle_x,cicle_y),10,0)

    if pygame.key.get_pressed()[K_w]:
        player_one_y -= 10
        if player_one_y <= 0:
            player_one_y = 0
    if pygame.key.get_pressed()[K_s]:
        player_one_y += 10
        if player_one_y >= height:
            player_one_y = height

    if pygame.key.get_pressed()[K_UP]:
        player_two_y -= 10
        if player_two_y <= 0:
            player_two_y = 0
    if pygame.key.get_pressed()[K_DOWN]:
        player_two_y += 10
        if player_two_y >= height:
            player_two_y = height

    if horizontal_move_cicle == True:
        cicle_x -= 5
    elif horizontal_move_cicle == False:
        cicle_x += 5

    if vertical_move_cicle == True:
        cicle_up()
    elif vertical_move_cicle == False:
        cicle_down()


    if player_one.colliderect(ball):
        horizontal_move_cicle = False

    if player_two.colliderect(ball):
        horizontal_move_cicle = True

    if cicle_x == 0:
        player_two_points += 1
        cicle_x = reset_cicle_x
        cicle_y = reset_cicle_y
    
    elif cicle_x == width:
        player_one_points += 1
        cicle_x = reset_cicle_x
        cicle_y = reset_cicle_y


    screen.blit(fotmated_points_player_one, (int(width/2)-70, 50))
    screen.blit(fotmated_points_player_two, (int(width/2)+40, 50))

    pygame.display.flip()
    