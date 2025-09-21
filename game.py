import math
import  os
import random
import pygame

path =os.getcwd()

folder='C:\\Users\\mirza\\OneDrive\\Desktop\\codingal_python\\python_challenges\\spaceinvaders'

screen_width = 800
screen_height = 500
player_startx = 370
player_starty = 380
enemy_starty_min = 50
enemy_starty_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27


background = pygame.image.load(folder+'\\background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(folder+'\\ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load(folder+'\\player.png')
playerX = player_startx
playerY = player_starty
playerX_change = 0

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(folder+'\\enemy.png'))
    enemyX.append(random.randint(0,screen_width-64))
    enemyY.append(random.randint(enemy_starty_min, enemy_starty_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)

bulletImg = pygame.image.load(folder+'\\bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)
