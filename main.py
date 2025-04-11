import pygame
import random


# inicialização do pygame
pygame.init()

# criando uma tela
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# Titulos e icones
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Jogador
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Inimigo
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50 , 150)
enemyX_change = 3
enemyY_change = 40

# função jogador
def player(x, y):
    screen.blit(playerImg, (x, y))

# Função inimigo
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop
running = True
while running:

    # RGB - Red, Green, blue
    screen.fill((130, 130, 130))
    # background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pressionando os botoes esquerda e direita
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # movimento da nave(player) limitando as bordas
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # movimento do inimigo
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
