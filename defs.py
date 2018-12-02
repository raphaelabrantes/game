import pygame
import sys


def get_events(screen, menu, char, bg, inimigos, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not menu.on:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("menu.mp3")
                    pygame.mixer.music.play(loops=100)

                menu.on = True
                menu.regras_status = False
                menu.creditos_status = False
                score.save()
                bg.__init__(screen)
                char.__init__(screen)
                inimigos.__init__(screen)
                score.__init__(screen)

            elif not menu.on and event.key == pygame.K_SPACE:
                if not char.jumping and not char.up:
                    char.jumping = True
                    char.up = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu.on:
                check_click_menu(menu)


def check_click_menu(menu):
    x, y = pygame.mouse.get_pos()

    if menu.play_rect.collidepoint(x, y):
        menu.on = False
        pygame.mixer.music.stop()
        pygame.mixer.music.load("eita.mp3")
        pygame.mixer.music.play(loops=100)

    elif menu.regras_b_rect.collidepoint(x, y):
        menu.regras_status = True

    elif menu.creditos_b_rect.collidepoint(x, y):
        menu.creditos_status = True

    elif menu.exit_n_rect.collidepoint(x, y):
        sys.exit()


def run_motherfucker_run(char):
    if char.status == 18:
        char.status = 1
    elif char.status == 1 or char.status <= 18:
        char.status += 1


def up_you_go(char):
    if char.walk_rect.y <= 100:
        char.up = False
        char.walk_rect.y = 100
    else:
        char.up_you_go()


def down_bellow(char):
    if char.walk_rect.y >= 300:
        char.jumping = False
        char.walk_rect.y = 300
        char.velocidade = 0
    else:
        char.down_bellow()


def hit_box(char, inimigos):
    for inim in inimigos.lista:
        if inim.collidepoint(char.walk_rect.right - 100, char.walk_rect.bottom - 10):
            char.alive = False
            char.status = 70
        elif inim.collidepoint(char.walk_rect.centerx - 73, char.walk_rect.centery + 140):
            char.alive = False
            char.status = 70
        elif inim.collidepoint(char.walk_rect.top , char.walk_rect.left):
            char.alive = False
            char.status = 70
		

