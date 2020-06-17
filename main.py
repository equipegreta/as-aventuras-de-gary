import pygame
import random
import sys

# Inicializando o pygame
pygame.init()

# =-= Tamanho da tela =-= #
screen = pygame.display.set_mode((800, 600))

# =-= Imagem do background =-= #
background = pygame.transform.scale(pygame.image.load('fundo.png'), (800, 600))

# =-= Título e ícone =-= #
pygame.display.set_caption("Título")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)
main_font = pygame.font.SysFont("comicsans", 50)


# =-= Menu =-= #
def menu():
    # Imagem botões
    titulo_img = pygame.image.load('titulo.png')
    btn_jogar_img = pygame.image.load('btn.png')
    btn_tutorial_img = pygame.image.load('btn.png')
    btn_saiba_mais_img = pygame.image.load('btn.png')
    btn_ranking_img = pygame.image.load('btn.png')
    btn_creditos_img = pygame.image.load('btn.png')

    running = True
    while running:
        global background
        screen.fill((255, 255, 255))  # Branco
        screen.blit(background, (0, 0))

        # Definindo onde estão os botões
        btn_jogar = pygame.Rect((257, 150), (286, 50))  # left, top, width, height
        btn_tutorial = pygame.Rect((257, 220), (286, 50))
        btn_saiba_mais = pygame.Rect((257, 290), (286, 50))
        btn_ranking = pygame.Rect((257, 360), (286, 50))
        btn_creditos = pygame.Rect((257, 430), (286, 50))

        pygame.draw.rect(screen, (255, 0, 0), btn_jogar)
        pygame.draw.rect(screen, (255, 0, 0), btn_tutorial)
        pygame.draw.rect(screen, (255, 0, 0), btn_saiba_mais)
        pygame.draw.rect(screen, (255, 0, 0), btn_ranking)
        pygame.draw.rect(screen, (255, 0, 0), btn_creditos)

        # Imprimindo as imagens do titulo e dos botões
        screen.blit(titulo_img, (257, 50))
        screen.blit(btn_jogar_img, (257, 150))
        screen.blit(btn_tutorial_img, (257, 220))
        screen.blit(btn_saiba_mais_img, (257, 290))
        screen.blit(btn_ranking_img, (257, 360))
        screen.blit(btn_creditos_img, (257, 430))

        # Pegando o clique do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if btn_jogar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogar()
        if btn_tutorial.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
        if btn_saiba_mais.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
        if btn_ranking.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
        if btn_creditos.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# =-= Jogo =-= #
def jogar():

    # =-= Elementos do jogo =-= #

    # Jogador principal
    player_img = pygame.transform.scale(pygame.image.load('protagonista.png').convert_alpha(),(50,64))
    player_x = 370
    player_y = 500
    player_x_deslocamento = 0

    # Arma do personagem (lixeiras)
    arma_azul = 'azul.png'  # papel
    arma_branca = 'branco.png'  # orgânico
    arma_preta = 'preto.png'  # rejeito
    arma_verde = 'verde.png'  # reciclável
    cores = [arma_azul, arma_branca, arma_preta, arma_verde]
    cor_arma = 0
    arma_x = 375
    arma_y = 465
    arma_x_deslocamento = 0

    # Inimigo
    enemy_img = pygame.image.load('inimigo.png')
    enemy_x = random.randint(0, 800)
    enemy_y = 20
    enemy_x_deslocamento = 3

    # Chão
    chao_img = pygame.transform.scale(pygame.image.load('chao.png'), (800, 50))
    chao_x = 0
    chao_y = 555

    # Lixos

    # Azul - papel
    folha = pygame.transform.scale(pygame.image.load('folha.png').convert_alpha(), (40, 50))
    caderno = pygame.transform.scale(pygame.image.load('caderno.png').convert_alpha(), (40, 50))
    postit = pygame.transform.scale(pygame.image.load('postit.png').convert_alpha(), (30, 30))
    # Branco - orgânico
    banana = pygame.transform.scale(pygame.image.load('banana.png').convert_alpha(), (30, 40))
    maca = pygame.transform.scale(pygame.image.load('maca.png').convert_alpha(), (40, 40))
    laranja = pygame.transform.scale(pygame.image.load('laranja.png').convert_alpha(), (40, 40))
    # Verde - reciclável
    cebolitos = pygame.transform.scale(pygame.image.load('cebolitos.png').convert_alpha(), (40, 60))
    latinha = pygame.transform.scale(pygame.image.load('latinha.png').convert_alpha(), (40, 40))
    garrafapet = pygame.transform.scale(pygame.image.load('garrafapet.png').convert_alpha(), (40, 50))
    # Preto - rejeito
    copo = pygame.transform.scale(pygame.image.load('copo.png').convert_alpha(), (40, 50))
    guardanapo = pygame.transform.scale(pygame.image.load('guardanapo.png').convert_alpha(), (40, 40))
    fita = pygame.transform.scale(pygame.image.load('fita.png').convert_alpha(), (50, 40))

    # Botão voltar pra o jogo
    btn_voltar_img = pygame.image.load('btn.png')

    # Separação
    papeis = [folha, caderno,postit]
    reciclaveis = [cebolitos,latinha,garrafapet]
    organicos = [banana, maca,laranja]
    rejeitos = [copo, guardanapo,fita]

    # Todos
    lixos_img = [papeis, organicos, reciclaveis, rejeitos]

    # Posicionamento
    lixos_imgs = []
    lixo_x = []
    lixo_y = []
    lixo_y_deslocamento = []

    # Pontuação
    pontuacao = 0

    coracao_cheio = pygame.transform.scale(pygame.image.load('coração-cheio.png'), (20, 20))
    coracao_vazio = pygame.transform.scale(pygame.image.load('coração-vazio.png'), (20, 20))
    vida = [coracao_cheio, coracao_cheio, coracao_cheio, coracao_cheio, coracao_cheio]
    contagem_vidas = 5

    # =-= Funções =-= #

    # Gerando lixo aleatoriamente com a biblioteca random
    def gerar_lixo():
            j = random.randint(0, 3)
            k = random.randint(0, 2)
            lixos_imgs.append(lixos_img[j][k])
            lixo_x.append(enemy_x)
            lixo_y.append(enemy_y)
            lixo_y_deslocamento.append(2)
    # Imprimindo na tela o protagonista
    def player(x, y):
        screen.blit(player_img, (x, y))

    # Imprimindo na tela a arma
    def arma(ind, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load(cores[ind]).convert_alpha(),(40,40)), (x,y))

    # Imprimindo na tela o inimigo
    def enemy(x, y):
        screen.blit(enemy_img, (x, y))

    # Imprimindo na tela o chão
    def chao(x, y):
        screen.blit(chao_img, (x, y))

    # Imprimindo os lixos que foram gerados aleatoriamente
    def jogar_lixo(i, x, y):
        screen.blit(lixos_imgs[i], (x, y))

    # Verificando colisão com a lixeira
    def colisao_lixeira(xa, ya, xb, yb):
        if abs(xa - xb) <= 40 and (ya - yb) <= 15:
            return True
        else:
            return False

    # Verificando a colisão com o chão
    def colisao_chao(ya, yb):
        if (ya-yb) < 20:
            return True
        else:
            return False

    # =-= Loop central do jogo =-= #
    pause = False
    running = True
    while running:

        # =-= Fundo da tela =-= #
        screen.fill((255, 255, 255))  # Branco

        # Imagem de fundo
        # Obs: A imagem de fundo acaba deixando o loop mais lento,
        # só é ajustar a velocidade dos elementos para corrigir
        screen.blit(background, (0, 0))

        # =-= Fechar o jogo =-= #
        # Muito importante ter!! Não tirar!!
        # Se tirar, trava o computador, pois o jogo vira um loop eterno!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # =-= Movimentando com o teclado =-= #
        # Verificando se alguma tecla está pressionada ou não
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_deslocamento = -5
                    arma_x_deslocamento = -5
                elif event.key == pygame.K_RIGHT:
                    player_x_deslocamento = 5
                    arma_x_deslocamento = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_deslocamento = 0
                    arma_x_deslocamento = 0
        # =-= Mudando a cor da arma =-= #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cor_arma = 0  # Azul
                elif event.key == pygame.K_a:
                    cor_arma = 1  # Branco
                elif event.key == pygame.K_s:
                    cor_arma = 2  # Preto
                elif event.key == pygame.K_d:
                    cor_arma = 3  # Verde
        # =-= Pausar o jogo =-= #
                elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        mnsgnp = main_font.render(f"APERTE P PRA VOLTAR A JOGAR", 1, (0, 0, 255))
                        screen.blit(mnsgnp, (400 - (mnsgnp.get_width() / 2), 300))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    pause = False

        arma_x += arma_x_deslocamento
        player_x += player_x_deslocamento

        # =-= Chamando a função que gera os lixos =-= #
        try:
            if lixo_y[-1] > 60:
                if random.randrange(0, 150) == 1:
                    gerar_lixo()
        except IndexError:
            if random.randrange(0, 150) == 1:
                gerar_lixo()
        for i in range(len(lixos_imgs)):
            lixo_y[i] += lixo_y_deslocamento[i]
            jogar_lixo(i, lixo_x[i], lixo_y[i])

        # =-= Para o elemento não sumir quando encontrar a borda =-= #
        # Protagonista
        if player_x <= 0:
            arma_x = 5
            player_x = 0
        # Prestar atenção na largura da imagem aqui caso mude!
        # (tamanho_tela - largura_imagem = 754)
        elif player_x > 754:
            player_x = 754
            arma_x = 759

        # Inimigo
        enemy_x += enemy_x_deslocamento
        if enemy_x <= 0:
            enemy_x_deslocamento = 2
        elif enemy_x > 726:
            enemy_x_deslocamento = -2

        # =-= Elementos =-= #
        # Atenção: Precisam ser impressos após o screen fill e antes do display update
        player(player_x, player_y)
        enemy(enemy_x, enemy_y)
        chao(chao_x, chao_y)
        arma(cor_arma, arma_x, arma_y)

        # =-= Checando colisões =-= #
        for i, lixo in enumerate(lixos_imgs):
            if colisao_lixeira(arma_x, arma_y, lixo_x[i], lixo_y[i]):
                screen.blit(lixo, (50, 50))
                # Azul
                if cor_arma == 0 and papeis.count(lixos_imgs[i]) == 1:
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Branca
                elif cor_arma == 1 and organicos.count(lixos_imgs[i]) == 1:
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Preta
                elif cor_arma == 2 and rejeitos.count(lixos_imgs[i]) == 1:
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Verde
                elif cor_arma == 3 and reciclaveis.count(lixos_imgs[i]) == 1:
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Se coletar um lixo na lixeira errada
                else:
                    pontuacao -= 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
            # Se colidiu com o chão
            elif colisao_chao(chao_y, lixo_y[i]):
                pontuacao -= 1
                lixos_imgs.pop(i)
                lixo_x.pop(i)
                lixo_y.pop(i)
                lixo_y_deslocamento.pop(i)
                vida[contagem_vidas - 1] = coracao_vazio
                contagem_vidas -= 1

        # Tabela de pontuação e vidas
        pont_label = main_font.render(f"PONTUAÇÃO: {pontuacao}", 1, (0, 0, 255))
        screen.blit(pont_label, (10, 10))  # (400 - (pont_label.get_width() / 2)
        screen.blit(vida[0], (10, 50))
        screen.blit(vida[1], (30, 50))
        screen.blit(vida[2], (50, 50))
        screen.blit(vida[3], (70, 50))
        screen.blit(vida[4], (90, 50))

        if contagem_vidas == 0:
            game_over()

        # Atenção: Nada aparece se não tiver a função update!
        # Se não tiver, a tela não atualiza
        pygame.display.update()


# =-= Fim de jogo =-= #
def game_over():
    btn_voltar_img = pygame.image.load('btn.png')
    running = True
    while running:

        btn_voltar = pygame.Rect((257, 150), (286, 50))  # left, top, width, height
        pygame.draw.rect(screen, (255, 0, 0), btn_voltar)

        screen.blit(btn_voltar_img, (257, 150))

        # Pegando o clique do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if btn_voltar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        mnsgngo = main_font.render(f"PERDEU!!!", 1, (0, 0, 255))
        screen.blit(mnsgngo, (400 - (mnsgngo.get_width() / 2), 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


menu()
