import pygame
import random
#import math

# inicializando o pygame
pygame.init()

# =-=-=-=-=-=-=-=-=-= TAMANHO DA TELA =-=-=-=-=-=-=-=-=-= #
screen = pygame.display.set_mode((800, 600))  # ((width, height))  ((x, y))
#
#       -------------------- >
#       |               800 px
#       |
#       |
#       |
#       V 600 px

# =-=-=-=-=-=-=-=-=-= BACKGROUND =-=-=-=-=-=-=-=-=-= #
background = pygame.transform.scale(pygame.image.load('fundo.png'),(800,600))

# =-=-=-=-=-=-=-=-=-= TÍTULO E ÍCONE =-=-=-=-=-=-=-=-=-= #
pygame.display.set_caption("Título do jogo")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)

# =-=-=-=-=-=-=-=-=-= ADICIONANDO ELEMENTOS =-=-=-=-=-=-=-=-=-= #
# jogador principal
player_img = pygame.image.load('protagonista.png')
player_x = 370
player_y = 500
playerX_change = 0
# lixeira / arma
armaazul = 'azul.png'
armabranca = 'branca.png'
armapreta = 'preta.png'
armaverde = 'verde.png'
cores = [armaazul,armabranca,armapreta,armaverde]
m = 0
arma_x = 370
arma_y = 470
armax_change = 0
# inimigo
enemy_img = pygame.image.load('inimigo.png')
enemy_x = random.randint(0, 800)
enemy_y = 20
enemyX_change = 3
# chão
chao_img = pygame.image.load('chao.png')
chao_x = 0
chao_y = 555


def player(x, y):
    screen.blit(player_img, (x, y))  # (imagem, coordenadas)


def arma(ind, x, y):
    screen.blit(pygame.image.load(cores[ind]), (x,y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def chao(x, y):
    screen.blit(chao_img, (x, y))


# =-=-=-= GAME LOOP =-=-=-= #
running = True
while running:

    # =-=-=-=-=-=-=-=-=-= BACKGROUND =-=-=-=-=-=-=-=-=-= #
    screen.fill((255, 255, 255))  # RGB
    # imagem de fundo
    screen.blit(background, (0, 0))  # faz os elementos ficarem mais lentos
    # =-=-=-=-=-=-=-=-=-= FECHAR A PÁGINA =-=-=-=-=-=-=-=-=-= #
    for event in pygame.event.get():  # procurando dentro de todos os eventos se o evento está dentro
        if event.type == pygame.QUIT:  # se o evento quit está, running se torna falso e o jogo fecha
            running = False
    # =-=-=-=-=-=-=-=-=-= MOVIMENTANDO COM O TECLADO =-=-=-=-=-=-=-=-=-= #
    # se alguma tecla está pressionada
    if event.type == pygame.KEYDOWN:
        # se a tecla é esquerda ou direita
        if event.key == pygame.K_LEFT:
            playerX_change = -5
            armax_change = -5
        elif event.key == pygame.K_RIGHT:
            playerX_change = 5
            armax_change = 5
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            m = 0
        elif event.key == pygame.K_a:
            m = 1
        elif event.key == pygame.K_s:
            m = 2
        elif event.key == pygame.K_d:
            m = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
            armax_change = 0
    arma_x += armax_change
    player_x += playerX_change

    # =-=-=-=-=-=-=-=-= PARA O ELEMENTO NÃO SUMIR QUANDO ENCONTRAR A BORDA  =-=-=-=-=-=-=-=-= #
    # jogador
    if player_x <= 0:
        arma_x = 0
        player_x = 0
    elif player_x > 754:  # diminui 46 de 800 por conta da largura da imagem
        player_x = 754
        arma_x = 754
    #inimigo
    enemy_x += enemyX_change
    if enemy_x <= 0:
        enemyX_change = 3
    elif enemy_x > 736:
        enemyX_change = -3

    # =-= ELEMENTOS =-=
    # precisam ser impressos após o screen fill e antes do display update
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    chao(chao_x, chao_y)
    arma(m, arma_x, arma_y)

    # nada aparece se não tiver a função update
    pygame.display.update()