import pygame
import random
import sys
import time

pygame.init()

# size of screen

W = 800
H = 600

# NameOfThegame
pygame.display.set_caption('WinCode_IsraelDevelopers2021')

# The Game
BLUE = (255, 255, 102)
red = (255, 255, 255)
yellow = (255, 0, 0)
ColorBACK = (0, 0, 0)

Player1Size = 50
Player1pos = [W / 2, H - 2 * Player1Size]

enemysize = 50
enemypos = [random.randint(0, W - enemysize), 0]
enemy_list = [enemypos]

speed = 10

screen = pygame.display.set_mode((W, H))

game_over = False

score = 0

Clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)


# Speed set if/elif/else (*Change*)
def set_level(score, speed):
    if score < 2:
        speed = 5

    elif score < 10:
        speed = 7

    elif score < 50:
        speed = 7

    elif score < 80:
        speed = 9

    elif score < 100:
        speed = 11

    elif score < 120:
        speed = 14

    elif score < 150:
        speed = 17

    elif score < 200:
        speed = 22

    elif score < 400:
        spped = 23

    elif score < 500:
        speed = 27

    elif score < 600:
        speed = 35

    elif score < 650:
        speed = 38

    elif score < 700:
        speed = 41

    elif score < 735:
        speed = 46

    else:
        speed = 49
    return speed


# DEF
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, W - enemysize)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemypos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemypos[0], enemypos[1], enemysize, enemysize))


def update_enemy_positions(enemy_list, score):
    for idx, enemypos in enumerate(enemy_list):
        if enemypos[1] >= 0 and enemypos[1] < H:
            enemypos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1

    return score


def collision_check(enemy_list, Player1pos):
    for enemypos in enemy_list:
        if detect_collision(enemypos, Player1pos):
            return True
    return False


def detect_collision(Player1pos, enemypos):
    if (enemypos[0] >= Player1pos[0] and enemypos[0] < (Player1pos[0] + Player1Size)) or (
            Player1pos[0] >= enemypos[0] and Player1pos[0] < (enemypos[0] + enemysize)):
        if (enemypos[1] >= Player1pos[1] and enemypos[1] < (Player1pos[1] + Player1Size)) or (
                Player1pos[1] >= enemypos[1] and Player1pos[1] < (enemypos[1] + enemysize)):
            return True
    return False


while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = Player1pos[0]
            y = Player1pos[1]

            if event.key == pygame.K_LEFT:
                x -= Player1Size
            elif event.key == pygame.K_RIGHT:
                x += Player1Size

            Player1pos = [x, y]

    screen.fill(ColorBACK)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    speed = set_level(score, speed)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, yellow)
    screen.blit(label, (W - 450, H - 40))

    text2 = "After You lose wait 10s And it close"
    label = myFont.render(text2, 1, yellow)
    screen.blit(label, (W - 1200, H - 790))

    if collision_check(enemy_list, Player1pos):
        game_over = True
        time.sleep(6)
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, red, (Player1pos[0], Player1pos[1], Player1Size, Player1Size))

    Clock.tick(30)

    pygame.display.update()
