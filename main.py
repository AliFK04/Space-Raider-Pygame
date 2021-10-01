#Ali's space wars pygame

import pygame
import math
import random
from pygame import mixer

# initalize the pygame
pygame.init()

# creating the game window using pygame
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background (1).png")

#background music
mixer.music.load("assets_GamePlay.mp3")
mixer.music.play(-1)


# Changing the Title and Icon
pygame.display.set_caption("Ali Khan's pygame")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Adding the player image
playerImage = pygame.image.load("rocket (1).png")
PlayerX = 370
PlayerY = 480
PlayerX_change = 0
PlayerY_change = 0

# Adding the enemy image
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load("ufo.png"))
    EnemyX.append(random.randint(0, 736))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(1)
    EnemyY_change.append(30)

# Adding the bullet image
bulletImage = pygame.image.load("bullet.png")
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 15
# Ready - you can't see the bullet on the screen
# Fire - The bullet begins to move
Bullet_state = "ready"


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(bulletImage, (x, y))


def isCollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((math.pow(EnemyX - BulletX, 2)) + (math.pow(EnemyY - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# score
score_value = 0
font = pygame.font.SysFont("comicsansms.ttf", 40)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (235, 52, 72))
    screen.blit(score, (x, y))

over_font = pygame.font.SysFont("comicsansms.ttf", 64)


def game_over_text():
    over_text = font.render("GAME OVER YOU LOSE HAHAHAHAHAHAHAH ", True, (235, 52, 72))
    screen.blit(over_text, (50,250 ))



# creating the close button for the window using game loop
running = True
while running:

    # Changing the colour of the background using ((R, G, B))
    screen.fill((10, 10, 10))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -2
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 2
            if event.key == pygame.K_SPACE:
                if Bullet_state is "ready":
                    Bullet_Sound = mixer.Sound("assets_Soundeffects_Space-SFX-Shoot1.wav")
                    Bullet_Sound.play()
                    fire_bullet(PlayerX, BulletY)
                BulletY = PlayerY
                BulletX = PlayerX

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PlayerY_change = -2
            if event.key == pygame.K_DOWN:
                PlayerY_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_change = 0

    # creating boundaries for the players and enemies
    for i in range(num_of_enemies):

        #GAME OVER
        if EnemyY[i] > 400:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break


        if EnemyX[i] <= 0:
            EnemyX_change[i] = 2
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -2
            EnemyY[i] += EnemyY_change[i]

        EnemyX[i] += EnemyX_change[i]

        # collision
        collision = isCollision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            collision_sound = mixer.Sound("assets_Soundeffects_Space-SFX-DestroyAsteroid1 (1).wav")
            collision_sound.play()
            BulletX = PlayerX
            BulletY = PlayerY
            Bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(0, 736)
            EnemyY[i] = random.randint(50, 150)

        enemy(EnemyX[i], EnemyY[i], i)

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    if PlayerY >= 536:
        PlayerY = 536
    if PlayerY <= 300:
        PlayerY = 300

    PlayerX += PlayerX_change
    PlayerY += PlayerY_change

    if Bullet_state is "fire":
        BulletY -= BulletY_change
        fire_bullet(BulletX, BulletY)

    player(PlayerX, PlayerY)
    show_score(textX, textY)
    pygame.display.update()

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Ali khan's Pygame, press the mouse to begin...", 1, (255,255,255))
        win.blit(title_label(WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

main_menu()


