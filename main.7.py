import pygame
import random
# import math

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
main_font = pygame.font.SysFont("comicsans", 50)

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
cores = [armaazul, armabranca, armapreta, armaverde]
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
chao_img = pygame.transform.scale(pygame.image.load('chao.png'),(800,50))
chao_x = 0
chao_y = 555

# lixo
# azul - papel
folha = pygame.image.load('folha.png')
caderno = pygame.image.load('caderno.png')
# branco - orgânico
banana = pygame.image.load('banana.png')
maca = pygame.image.load('maca.png')
# verde - reciclável
embalagem = pygame.image.load('embalagem.png')
marmitaisopor = pygame.image.load('marmita.png')
# preto - rejeito
copo = pygame.image.load('copo.png')
guardanapo = pygame.image.load('guardanapo.png')

# separação
papeis = [folha, caderno]
reciclaveis = [embalagem, marmitaisopor]
organicos = [banana, maca]
rejeitos = [copo, guardanapo]
# todos
lixos_img = [papeis, organicos, reciclaveis, rejeitos]
# posicao etc
lixos_imgs = []
lixo_x = [enemy_x]
lixo_y = [enemy_y]
lixoy_change = []
catou = 0
catou_errado = 0
ncatou = 0


def gerar_lixo ():
    j = random.randint(0, 3)
    k = random.randint(0, 1)
    lixos_imgs.append(lixos_img[j][k])
    lixo_x.append(enemy_x)
    lixo_y.append(enemy_y)
    lixoy_change.append(2)


def player(x, y):
    screen.blit(player_img, (x, y))  # (imagem, coordenadas)


def arma(ind, x, y):
    screen.blit(pygame.image.load(cores[ind]), (x,y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def chao(x, y):
    screen.blit(chao_img, (x, y))


def jogar_lixo(i, x, y):
    screen.blit(lixos_imgs[i], (x, y))
def colisao_lixeira (xa,ya,xb,yb):
    if (xa-xb)<=20 and (ya-yb)<=20 :
        return True
    else:
        return False
def colisao_chao (ya,yb) :
    if (ya-yb)<20 :
        return True
    else:
        return False

# =-=-=-= GAME LOOP =-=-=-= #
running = True
while running:

    # =-=-=-=-=-=-=-=-=-= BACKGROUND =-=-=-=-=-=-=-=-=-= #
    screen.fill((255,255,255))  # RGB
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
    # se são as teclas WASD
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            m = 0 #azul
        elif event.key == pygame.K_a:
            m = 1 #branco
        elif event.key == pygame.K_s:
            m = 2 #preta
        elif event.key == pygame.K_d:
            m = 3 #verde
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
            armax_change = 0
    arma_x += armax_change
    player_x += playerX_change

    # =-=-=-=-=-=-=-=-= LIXOS =-=-=-=-=-=-=-=-= #
    if random.randrange(0, 210) == 1:
        gerar_lixo()
    for i in range(len(lixos_imgs)):
          lixo_y[i] += lixoy_change[i]

          jogar_lixo(i, lixo_x[i], lixo_y[i])

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
        enemyX_change = 2
    elif enemy_x > 726:
        enemyX_change = -2

    # =-= ELEMENTOS =-=
    # precisam ser impressos após o screen fill e antes do display update
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    chao(chao_x, chao_y)
    arma(m, arma_x, arma_y)
    # checar colisões
    for i,lixo in enumerate(lixos_imgs):
       if colisao_lixeira(arma_x,arma_y,lixo_x[i],lixo_y[i]) :
           screen.blit(lixo, (50,50))
           if m == 0 and (lixo in papeis):
              catou += 1
              lixos_imgs.pop(i)
              lixo_x.pop(i)
              lixo_y.pop(i)
              lixoy_change.pop(i)
           elif m == 1 and organicos.count(lixos_imgs[i])== 1 :
               catou += 1
               lixos_imgs.pop(i)
               lixo_x.pop(i)
               lixo_y.pop(i)
               lixoy_change.pop(i)
           elif m == 2 and rejeitos.count(lixos_imgs[i])== 1 :
               catou += 1
               lixos_imgs.pop(i)
               lixo_x.pop(i)
               lixo_y.pop(i)
               lixoy_change.pop(i)
           elif m == 3 and reciclaveis.count(lixos_imgs[i])== 1 :
               catou += 1
               lixos_imgs.pop(i)
               lixo_x.pop(i)
               lixo_y.pop(i)
               lixoy_change.pop(i)
           else:
               catou_errado +=1
               lixos_imgs.pop(i)
               lixo_x.pop(i)
               lixo_y.pop(i)
               lixoy_change.pop(i)
       elif colisao_chao(chao_y,lixo_y[i]):
            ncatou+=1
            lixos_imgs.pop(i)
            lixo_x.pop(i)
            lixo_y.pop(i)
            lixoy_change.pop(i)

    # draw text
    cat_label = main_font.render(f"CATOU: {catou}", 1, (0,0,255))
    ncat_label = main_font.render(f"POLUIU: {ncatou}", 1, (0,0,255))
    cater_label = main_font.render(f"Errou: {catou_errado}", 1, (0, 0, 255))

    screen.blit(cat_label, (10, 10))
    screen.blit(ncat_label, (800 - cat_label.get_width() - 10, 10))
    screen.blit(cater_label, (400 - (cat_label.get_width()/2) , 10))

    # nada aparece se não tiver a função update
    pygame.display.update()
