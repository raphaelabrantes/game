import pygame
import sys


def get_events(screen, menu, char, bg):

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				menu.on = True
				menu.regras_status = False
				menu.creditos_status = False
				bg.__init__(screen)
				char.__init__(screen)
			
			elif (not menu.on and event.key == pygame.K_SPACE):
				if not char.jumping and not char.up:
					char.jumping = True
					char.up = True
									
				
				
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if menu.on:
				check_click_menu(menu)

					
def check_click_menu(menu):
	x,y = pygame.mouse.get_pos()
	print(x,y)

	if menu.play_rect.collidepoint(x,y):
		menu.on = False

	elif menu.regras_b_rect.collidepoint(x,y):
		menu.regras_status = True

	elif menu.creditos_b_rect.collidepoint(x,y):
		menu.creditos_status = True

	elif menu.exit_rect.collidepoint(x,y):
		sys.exit()		
        

def run_motherfucker_run(char):
	if char.status == 18:
		char.status = 1
	elif char.status == 1 or char.status <= 18:
		char.status +=1

def up_you_go(char):
	print(char.walk_rect.y)
	if char.walk_rect.y <= 150:
		char.up = False
		
	else:
		char.walk_rect.y -= 5
		
def down_bellow(char):
	if char.walk_rect.y >= 300:
		char.jumping = False
	else:
		char.walk_rect.y += 5

	
		
