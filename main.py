import pygame
import pygame.freetype
import random
import sys

# Inicializando o pygame
pygame.init()

# =-= Tamanho da tela =-= #
screen = pygame.display.set_mode((800, 600))
background = pygame.transform.scale(pygame.image.load('fundo.png'), (800, 600))

# =-= Título e ícone =-= #
pygame.display.set_caption("As Aventuras de Gary")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)


# =-= Imagem do background =-= #
# Fontes
main_font = pygame.font.Font("PressStart2P.ttf", 15)


# =-= Menu =-= #
def menu():
    # Imagem botões
    titulo_img = pygame.transform.scale(pygame.image.load('titulo.png').convert_alpha(), (400, 188))
    btn_jogar_img = pygame.transform.scale(pygame.image.load('jogar.png').convert_alpha(), (286, 50))
    btn_tutorial_img = pygame.transform.scale(pygame.image.load('como_jogar.png').convert_alpha(), (286, 50))
    btn_saiba_mais_img = pygame.transform.scale(pygame.image.load('saiba_mais.png').convert_alpha(), (286, 50))
    btn_ranking_img = pygame.transform.scale(pygame.image.load('ranking.png').convert_alpha(), (286, 50))
    btn_creditos_img = pygame.transform.scale(pygame.image.load('creditos.png').convert_alpha(), (286, 50))

    running = True
    while running:
        global background
        screen.fill((255, 255, 255))  # Branco
        screen.blit(background, (0, 0))

        # Definindo onde estão os botões
        btn_jogar = pygame.Rect((257, 225), (286, 45))  # left, top, width, height
        btn_tutorial = pygame.Rect((257, 295), (286, 45))
        btn_saiba_mais = pygame.Rect((257, 365), (286, 45))
        btn_ranking = pygame.Rect((257, 435), (286, 45))
        btn_creditos = pygame.Rect((257, 505), (286, 45))

        pygame.draw.rect(screen, (255, 0, 0), btn_jogar)
        pygame.draw.rect(screen, (255, 0, 0), btn_tutorial)
        pygame.draw.rect(screen, (255, 0, 0), btn_saiba_mais)
        pygame.draw.rect(screen, (255, 0, 0), btn_ranking)
        pygame.draw.rect(screen, (255, 0, 0), btn_creditos)

        # Imprimindo as imagens do titulo e dos botões
        screen.blit(titulo_img, (195, 10))
        screen.blit(btn_jogar_img, (257, 220))
        screen.blit(btn_tutorial_img, (257, 290))
        screen.blit(btn_saiba_mais_img, (257, 360))
        screen.blit(btn_ranking_img, (257, 430))
        screen.blit(btn_creditos_img, (257, 500))

        # Pegando o clique do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if btn_jogar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogar()
        if btn_tutorial.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    como_jogar()
        if btn_saiba_mais.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    saiba_mais()
        if btn_ranking.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ranking()
        if btn_creditos.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    creditos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def como_jogar():
    imagem_tutorial = pygame.image.load('comojogar.png')
    btn_voltar_img = pygame.transform.scale(pygame.image.load('btn-voltar.png').convert_alpha(), (50, 50))

    running = True
    while running:
        screen.blit(imagem_tutorial, (0, 0))

        btn_voltar = pygame.Rect((20, 20), (50, 50))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 0, 0), btn_voltar)
        screen.blit(btn_voltar_img, (20, 20))

        if btn_voltar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def ranking():
    screen.blit(background, (0, 0))
    ranking_img = pygame.image.load('ranking_fundo.png')
    btn_voltar_img = pygame.transform.scale(pygame.image.load('btn-voltar.png').convert_alpha(), (50, 50))
    main_font = pygame.font.Font("PressStart2P.ttf", 40)
    small_font = pygame.font.Font("PressStart2P.ttf", 20)

    running = True
    while running:
        screen.blit(ranking_img, ((800 - ranking_img.get_width())/2, 150))

        btn_voltar = pygame.Rect((20, 20), (50, 50))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 0, 0), btn_voltar)
        screen.blit(btn_voltar_img, (20, 20))

        titulo_ranking = main_font.render(f"RANKING", 1, (0, 0, 0))
        screen.blit(titulo_ranking, (400 - (titulo_ranking.get_width() / 2), 100))

        arquivo_ranking = open('top3.txt', 'r', encoding='utf8')
        colocacao = []
        for linha in arquivo_ranking:
            colocacao.append(linha.strip().upper())
        primeiro_colocado = small_font.render(f"{colocacao[1][:3]}       {colocacao[0].zfill(5)} ", 1, (0, 0, 0))
        screen.blit(primeiro_colocado, (300, 210))
        segundo_colocado = small_font.render(f"{colocacao[3][:3]}       {colocacao[2].zfill(5)}", 1, (0, 0, 0))
        screen.blit(segundo_colocado, (300, 305))
        terceiro_colocado = small_font.render(f"{colocacao[5][:3]}       {colocacao[4].zfill(5)}", 1, (0, 0, 0))
        screen.blit(terceiro_colocado, (300, 400))

        if btn_voltar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def saiba_mais():
    imagem_fundo = pygame.image.load('fundo_saiba_mais.png')
    btn_voltar_img = pygame.transform.scale(pygame.image.load('btn-voltar.png').convert_alpha(), (50, 50))
    img_y = 0
    img_y_deslocamento = 0

    running = True
    while running:
        screen.blit(imagem_fundo, (0, img_y))
        img_y = img_y + img_y_deslocamento

        btn_voltar = pygame.Rect((20, 20), (50, 50))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 0, 0), btn_voltar)
        screen.blit(btn_voltar_img, (20, 20))

        if btn_voltar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    img_y_deslocamento = -8
                elif event.key == pygame.K_UP:
                    img_y_deslocamento = +8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    img_y_deslocamento = 0
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if img_y > 1:
            img_y = 0
        elif img_y < -1800:
            img_y = -1800

        pygame.display.update()


def creditos():
    imagem_fundo = pygame.image.load('desenvolvedores.png')
    btn_voltar_img = pygame.transform.scale(pygame.image.load('btn-voltar.png').convert_alpha(), (50, 50))

    running = True
    while running:
        screen.blit(imagem_fundo, (0, 0))

        btn_voltar = pygame.Rect((20, 20), (50, 50))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 0, 0), btn_voltar)
        screen.blit(btn_voltar_img, (20, 20))

        if btn_voltar.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# =-= High Score =-= #
def hscr():
    var = True
    while var:
        global background
        screen.fill((255, 255, 255))  # Branco
        screen.blit(background, (0, 0))
        input_box = pygame.Rect(225, 260, 350, 80)
        main_font = pygame.font.Font("PressStart2P.ttf", 20)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        cor = color_inactive
        active = False
        text = ''
        while True:
            mnsghsc1 = main_font.render(f"PONTUAÇÃO NO TOP 3!!!", 1, (0, 0, 255))
            screen.blit(mnsghsc1, (400 - (mnsghsc1.get_width() / 2), 100))
            mnsghsc2 = main_font.render(f"ENTRE SEU NOME:", 1, (0, 0, 255))
            screen.blit(mnsghsc2, (400 - (mnsghsc2.get_width() / 2), 150))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        # caixa ativa.
                        active = True
                    else:
                        active = False
                    # Change the current color of the input box.
                    cor = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            var = False
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Render the current text.
            txt_surface = main_font.render(text, 1, (0, 0, 255))
            # Blit the text.
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, cor, input_box, 2)

            pygame.display.update()


# =-= Jogo =-= #
def jogar():

    # =-= Elementos do jogo =-= #

    # Sons
    lixo_certo = pygame.mixer.Sound('certo.wav')
    lixo_errado = pygame.mixer.Sound('errado.wav')
    caiu_fora = pygame.mixer.Sound('fora.wav')
    perdeu = pygame.mixer.Sound('perdeu.wav')

    # Jogador principal
    player_img = pygame.transform.scale(pygame.image.load('protagonista.png').convert_alpha(), (50, 73))
    player_x = 370
    player_y = 482
    player_x_deslocamento = 0

    # Arma do personagem (lixeiras)
    arma_azul = 'azul.png'  # papel
    arma_branca = 'branco.png'  # orgânico
    arma_preta = 'preto.png'  # rejeito
    arma_verde = 'verde.png'  # reciclável
    cores = [arma_azul, arma_branca, arma_preta, arma_verde]
    cor_arma = 0
    arma_x = 375
    arma_y = 447
    arma_x_deslocamento = 0

    # Inimigo
    enemy_img = pygame.transform.scale(pygame.image.load('inimigo.png'), (142, 100))
    enemy_x = random.randint(0, 800)
    enemy_y = 20
    enemy_x_deslocamento = 4

    # Chão
    chao_img = pygame.transform.scale(pygame.image.load('chao.png'), (800, 50))
    chao_x = 0
    chao_y = 555

    # Lixos

    # Azul - papel
    folha = pygame.transform.scale(pygame.image.load('folha.png').convert_alpha(), (30, 30))
    caderno = pygame.transform.scale(pygame.image.load('caderno.png').convert_alpha(), (40, 40))
    postit = pygame.transform.scale(pygame.image.load('postit.png').convert_alpha(), (40, 40))
    # Branco - orgânico
    banana = pygame.transform.scale(pygame.image.load('banana.png').convert_alpha(), (35, 35))
    maca = pygame.transform.scale(pygame.image.load('maca.png').convert_alpha(), (40, 40))
    laranja = pygame.transform.scale(pygame.image.load('laranja.png').convert_alpha(), (40, 40))
    # Verde - reciclável
    cebolitos = pygame.transform.scale(pygame.image.load('cebolitos.png').convert_alpha(), (40, 40))
    latinha = pygame.transform.scale(pygame.image.load('latinha.png').convert_alpha(), (30, 30))
    garrafapet = pygame.transform.scale(pygame.image.load('garrafapet.png').convert_alpha(), (50, 50))
    # Preto - rejeito
    copo = pygame.transform.scale(pygame.image.load('copo.png').convert_alpha(), (30, 30))
    guardanapo = pygame.transform.scale(pygame.image.load('guardanapo.png').convert_alpha(), (40, 40))
    fita = pygame.transform.scale(pygame.image.load('fita.png').convert_alpha(), (40, 40))

    # Botão voltar pra o jogo
    btn_voltar_img = pygame.image.load('btn.png')

    # Separação
    papeis = [folha, caderno, postit]
    reciclaveis = [cebolitos, latinha,garrafapet]
    organicos = [banana, maca, laranja]
    rejeitos = [copo, guardanapo, fita]

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
    coraçao_metade = pygame.transform.scale(pygame.image.load('coração-metade.png'), (20, 20))
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
        lixo_y_deslocamento.append(3)

    # Imprimindo na tela o protagonista
    def player(x, y):
        screen.blit(player_img, (x, y))

    # Imprimindo na tela a arma
    def arma(ind, x, y):
        screen.blit(pygame.transform.scale(pygame.image.load(cores[ind]).convert_alpha(), (40, 40)), (x, y))

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
                if event.key == pygame.K_w or event.key == pygame.K_1:
                    cor_arma = 0  # Azul
                elif event.key == pygame.K_a or event.key == pygame.K_2:
                    cor_arma = 1  # Branco
                elif event.key == pygame.K_s or event.key == pygame.K_3:
                    cor_arma = 2  # Preto
                elif event.key == pygame.K_d or event.key == pygame.K_4:
                    cor_arma = 3  # Verde
        # =-= Pausar o jogo =-= #
                elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        mnsgnp = main_font.render(f"APERTE P PRA VOLTAR A JOGAR", 1, (0, 0, 0))
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
            if lixo_y[-1] > 90:
                if random.randrange(0, abs(150-pontuacao)) == 1:
                    gerar_lixo()
        except IndexError:
            if random.randrange(0, 190) == 1:
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
            enemy_x_deslocamento = 4
        elif enemy_x > 658:
            enemy_x_deslocamento = -4

        # =-= Elementos =-= #
        # Atenção: Precisam ser impressos após o screen fill e antes do display update
        player(player_x, player_y)
        enemy(enemy_x, enemy_y)
        chao(chao_x, chao_y)
        arma(cor_arma, arma_x, arma_y)

        # =-= Checando colisões =-= #
        for i, lixo in enumerate(lixos_imgs):
            if colisao_lixeira(arma_x, arma_y, lixo_x[i], lixo_y[i]):
                # screen.blit(lixo, (50, 50))
                # Azul
                if cor_arma == 0 and papeis.count(lixos_imgs[i]) == 1:
                    lixo_certo.play()
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Branca
                elif cor_arma == 1 and organicos.count(lixos_imgs[i]) == 1:
                    lixo_certo.play()
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Preta
                elif cor_arma == 2 and rejeitos.count(lixos_imgs[i]) == 1:
                    lixo_certo.play()
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Verde
                elif cor_arma == 3 and reciclaveis.count(lixos_imgs[i]) == 1:
                    lixo_certo.play()
                    pontuacao += 1
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
                # Se coletar um lixo na lixeira errada
                else:
                    lixo_errado.play()
                    lixos_imgs.pop(i)
                    lixo_x.pop(i)
                    lixo_y.pop(i)
                    lixo_y_deslocamento.pop(i)
            # Se colidiu com o chão
            elif colisao_chao(chao_y, lixo_y[i]):
                caiu_fora.play()
                lixos_imgs.pop(i)
                lixo_x.pop(i)
                lixo_y.pop(i)
                lixo_y_deslocamento.pop(i)
                vida[contagem_vidas - 1] = coracao_vazio
                contagem_vidas -= 1

        # Tabela de pontuação e vidas
        pont_label = main_font.render(f"{pontuacao}".zfill(7), 1, (0, 0, 0))
        screen.blit(pont_label, (10, 10))  # (400 - (pont_label.get_width() / 2)
        screen.blit(vida[0], (10, 30))
        screen.blit(vida[1], (30, 30))
        screen.blit(vida[2], (50, 30))
        screen.blit(vida[3], (70, 30))
        screen.blit(vida[4], (90, 30))

        if contagem_vidas == 0:
            perdeu.play()
            game_over(pontuacao)

        # Atenção: Nada aparece se não tiver a função update!
        # Se não tiver, a tela não atualiza
        pygame.display.update()


# =-= Fim de jogo =-= #
def game_over(pont):

    # Salvando no ranking
    leia = True
    while leia:
        try:
            ranking = open("top3.txt", 'r', encoding='utf8')
            copia_rk = ranking.readlines()
            ranking.close()
            leia = False
        except FileNotFoundError:
            ranking = open("top3.txt", 'w', encoding='utf8')
            for i in range(0, 6):
                ranking.write('0\n')
            ranking.close()
    if pont > int(copia_rk[4]):
        if pont > int(copia_rk[0]):
            # 1°
            copia_rk[4] = copia_rk[2]
            copia_rk[5] = copia_rk[3]
            copia_rk[2] = copia_rk[0]
            copia_rk[3] = copia_rk[1]
            copia_rk[0] = str(pont) + '\n'
            copia_rk[1] = hscr() + '\n'
        elif pont > int(copia_rk[2]):
            # 2°
            copia_rk[4] = copia_rk[2]
            copia_rk[5] = copia_rk[3]
            copia_rk[2] = str(pont) + '\n'
            copia_rk[3] = hscr() + '\n'
        elif pont > int(copia_rk[4]):
            # 3°
            copia_rk[4] = str(pont) + '\n'
            copia_rk[5] = hscr() + '\n'
        ranking = open("top3.txt", 'w', encoding='utf8')
        for i in range(0, 6):
            ranking.write(copia_rk[i])
        ranking.close()

    btn_menu_img = pygame.transform.scale(pygame.image.load('btn_menu.png').convert_alpha(), (200, 77))
    game_over_img = pygame.transform.scale(pygame.image.load('game_over.png').convert_alpha(), (300, 161))
    running = True
    while running:

        screen.blit(background, (0, 0))

        # Botão voltar pra o menu
        btn_menu = pygame.Rect((305, 322), (190, 73))  # left, top, width, height
        pygame.draw.rect(screen, (255, 0, 0), btn_menu)
        screen.blit(btn_menu_img, (400 - (btn_menu_img.get_width() / 2), 320))
        # Imagem game over
        screen.blit(game_over_img, (400 - (game_over_img.get_width() / 2), 100))

        # Pegando o clique do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if btn_menu.collidepoint((mouse_x, mouse_y)):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


menu()
