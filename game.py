# import as bibliotecas e as funções
# noinspection PyUnresolvedReferences
import pygame
from defs import get_events, run_motherfucker_run, up_you_go, down_bellow, hit_box
from menu import Menu, Background, Score
from char import Char
from inimigo import Inimigos


def run_game():
    # inicia a biblioteca pygame
    pygame.init()
    pygame.mixer.music.load("menu.mp3")
    # cria o objeto surface
    screen = pygame.display.set_mode((1080, 600))
    menu = Menu(screen)
    char = Char(screen)
    score = Score(screen)
    bg = Background(screen)
    clock = pygame.time.Clock()
    inimigos = Inimigos(screen)
    contador = 0
    pygame.mixer.music.play(loops=100)
    # loop do jogo
    while True:
        get_events(screen, menu, char, bg, inimigos, score)
        if menu.on:
            contador = 0
            menu.render()
            if menu.regras_status:
                menu.show_regras()
            elif menu.creditos_status:
                menu.show_creditos()
            else:
                menu.display_info()
        else:
            inimigos.check_in_clean(char.alive)
            if char.alive:
                hit_box(char, inimigos)
                bg.blitme()
                if char.jumping:
                    if char.up:
                        up_you_go(char)
                    else:
                        down_bellow(char)
                run_motherfucker_run(char)

            else:
                bg.blitdead()
                if contador >= 50:

                    char.status = 80
                contador += 1

            score.update(str(bg.x * - 1))

            score.blitall()
            inimigos.blit(char.alive)
            char.blitme()
        clock.tick(60)
        pygame.display.update()


run_game()
