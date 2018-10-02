#import as bibliotecas e as funções
import pygame
from defs import get_events, run_motherfucker_run, up_you_go, down_bellow
from menu import Menu, Background
from char import Char

def run_game():
    #inicia a biblioteca pygame
	pygame.init()
    #cria o objeto surface
	screen = pygame.display.set_mode((1080, 600))
	menu = Menu(screen)
	char = Char(screen)
	bg = Background(screen)
	clock = pygame.time.Clock()
    #loop do jogo
	while True:
		get_events(screen, menu, char, bg)
		if menu.on:
			menu.render()
			if menu.regras_status:
				menu.show_regras()
			elif menu.creditos_status:
				menu.show_creditos()
			else:
				menu.display_info()
		else:
			bg.blitme()
			if char.jumping:
				if char.up:
					up_you_go(char)
				else:
					down_bellow(char)
							
						
			run_motherfucker_run(char)
			char.blitme()

		pygame.display.update()
		clock.tick(60)


run_game()
