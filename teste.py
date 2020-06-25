import pygame
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
