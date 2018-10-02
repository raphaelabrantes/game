#!/usr/bin/env python3

import pygame

class Menu:# -*- coding: utf-8 -*-
	def __init__(self, screen):
		play = 'JOGAR'
		title = "ESCAPE THE JAIL"
		exit = 'SAIR DO JOGO'
		regras_opcao = "REGRAS"
		credito = "CREDITOS"
		self.bg = (255,255,255)
		with open("regras.txt") as filename:
			self.linhas = filename.readlines()
		with open("creditos.txt") as creditos:
			self.creditos = creditos.readlines()
		self.selected = None
		self.screen= screen
		self.screen_rect = screen.get_rect()
		self.on = True
		self.regras_status = False
		self.creditos_status = False
		self.fonte = pygame.font.SysFont(None, 30)
		self.fonte2 = pygame.font.SysFont(None, 40)
		self.font_ready(play, exit, regras_opcao, title, credito)

	def font_ready(self, play, exit, regras_opcao, title, credito):
		self.play = self.fonte.render(play, True, (0, 0, 0))
		self.exit = self.fonte.render(exit, True, (0, 0, 0))
		self.regras_b = self.fonte.render(regras_opcao, True, (0, 0, 0))
		self.title = self.fonte2.render(title, True, (0,0,0))
		self.creditos_b = self.fonte.render(credito, True, (0,0,0))
		self.play_rect = self.play.get_rect()
		self.exit_rect = self.exit.get_rect()
		self.regras_b_rect = self.regras_b.get_rect()
		self.title_rect = self.title.get_rect()
		self.creditos_b_rect = self.creditos_b.get_rect()
		
		self.title_rect.top = self.screen_rect.top + 100
		self.title_rect.left = self.screen_rect.left + 10

		self.play_rect.left = self.screen_rect.left + 10
		self.play_rect.top = self.screen_rect.top + 255

		self.exit_rect.bottom = self.screen_rect.bottom
		self.exit_rect.left = self.screen_rect.left + 10

		self.regras_b_rect.top = self.play_rect.bottom + 100
		self.regras_b_rect.left = self.screen_rect.left + 10
		
		self.creditos_b_rect.top = self.regras_b_rect.bottom + 100
		self.creditos_b_rect.left = self.screen_rect.left + 10

		self.regras_lista = self.lines(self.linhas)
		self.creditos_lista = self.lines(self.creditos)
				

	def display_info(self):
		self.screen.blit(self.play, self.play_rect)
		self.screen.blit(self.exit, self.exit_rect)
		self.screen.blit(self.regras_b, self.regras_b_rect)
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.creditos_b, self.creditos_b_rect)

	def show_regras(self):
		for regra in self.regras_lista:
			self.screen.blit(regra[0], regra[1])
		self.screen.blit(self.exit, self.exit_rect)
	
	def show_creditos(self):	
		for credito in self.creditos_lista:
			self.screen.blit(credito[0], credito[1])	
		self.screen.blit(self.exit, self.exit_rect)		

	def render(self):
		self.screen.fill(self.bg)

	def lines(self, linhas):
		contador = 0
		linha_lista= []
		for linha in linhas:
			lin = self.fonte.render(linha.strip(), True, (0, 0, 0))
			lin_rect = lin.get_rect()
			lin_rect.left = self.screen_rect.left + 10
			if contador == 0:
				lin_rect.top = self.screen_rect.top + 100
				contador += 25

			else:
				lin_rect.top = self.screen_rect.top + 100 + contador
				contador += 25
		
			linha_lista.append((lin, lin_rect))
		return linha_lista

class Background:
#	def __init__(self, screen):
#		self.screen = screen
#		self.image = pygame.image.load("background//background2.png")
#		self.screen_rect = self.screen.get_rect()
#		self.image_rect = self.image.get_rect()
#		self.left = self.image_rect.left 
#		
#		self.image_rect.bottom = self.screen_rect.bottom
#		self.image_rect.left = self.screen_rect.left

#	def blitme(self):
#		self.left -= 1
#		print(self.left)
#		self.image_rect = self.image_rect.move(self.left, self.image_rect.y)
#		self.screen.blit(self.image, self.image_rect)
	
	def __init__(self, screen):
		self.bkgd = pygame.image.load("background//background2.png").convert()
		self.screen = screen
		self.x = 0

	def blitme(self):
		rel_x = self.x % self.bkgd.get_rect().width
		self.screen.blit(self.bkgd, (rel_x - self.bkgd.get_rect().width, 0))
		if rel_x < self.screen.get_rect().width:
			self.screen.blit(self.bkgd, (rel_x, 0))
		self.x -= 10	