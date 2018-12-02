#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import pygame


class Menu:  # -*- coding: utf-8 -*-
    def __init__(self, screen):
        play = 'JOGAR'
        title = "ESCAPE THE JAIL"
        exit_n = 'SAIR'
        regras_opcao = "REGRAS"
        credito = "CREDITOS"
        self.bg = pygame.image.load("background//menu.png")
        self.bg_rect = self.bg.get_rect()
        with open("regras.txt") as filename:
            self.linhas = filename.readlines()
        with open("creditos.txt") as creditos:
            self.creditos = creditos.readlines()
        self.selected = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.on = True
        self.regras_status = False
        self.creditos_status = False
        self.fonte = pygame.font.Font("mostwasted//Mostwasted.ttf", 35)
        self.fonte2 = pygame.font.Font("mostwasted//Mostwasted.ttf", 60)
        self.font_ready(play, exit_n, regras_opcao, title, credito)

    def font_ready(self, play, exit_n, regras_opcao, title, credito):
        self.play = self.fonte.render(play, True, (0, 0, 0))
        self.exit_n = self.fonte.render(exit_n, True, (0, 0, 0))
        self.regras_b = self.fonte.render(regras_opcao, True, (0, 0, 0))
        self.title = self.fonte2.render(title, True, (0, 0, 255))
        self.creditos_b = self.fonte.render(credito, True, (0, 0, 0))
        self.play_rect = self.play.get_rect()
        self.exit_n_rect = self.exit_n.get_rect()
        self.regras_b_rect = self.regras_b.get_rect()
        self.title_rect = self.title.get_rect()
        self.creditos_b_rect = self.creditos_b.get_rect()
        self.bg_rect.center = self.screen_rect.center

        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.top = self.screen_rect.top + 100

        self.play_rect.x = 350
        self.play_rect.y = 220

        self.regras_b_rect.top = self.play_rect.bottom + 50
        self.regras_b_rect.left = self.play_rect.left

        self.creditos_b_rect.top = self.regras_b_rect.bottom + 40
        self.creditos_b_rect.left = self.play_rect.left - 20

        self.exit_n_rect.top = self.creditos_b_rect.bottom + 30
        self.exit_n_rect.left = self.play_rect.left + 10

        self.regras_lista = self.lines(self.linhas)
        self.creditos_lista = self.lines(self.creditos)

    def display_info(self):
        self.screen.blit(self.play, self.play_rect)
        self.screen.blit(self.exit_n, self.exit_n_rect)
        self.screen.blit(self.regras_b, self.regras_b_rect)
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.creditos_b, self.creditos_b_rect)

    def show_regras(self):
        for regra in self.regras_lista:
            self.screen.blit(regra[0], regra[1])
        self.screen.blit(self.exit_n, self.exit_n_rect)

    def show_creditos(self):
        for credito in self.creditos_lista:
            self.screen.blit(credito[0], credito[1])
        self.screen.blit(self.exit_n, self.exit_n_rect)

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)

    def lines(self, linhas):
        contador = 0
        linha_lista = []
        for linha in linhas:
            lin = self.fonte.render(linha.strip(), True, (255, 0, 0))
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

    def blitdead(self):
        self.screen.blit(self.bkgd, self.bkgd.get_rect())


class Score:
    def __init__(self, screen):
        with open("score.txt", 'r') as filename:
            score = filename.readlines()
            score = [int(i.strip()) for i in score]

        score.sort(reverse=True)

        self.best_list = [str(i) for i in score]
        self.fonte = pygame.font.Font("mostwasted//Mostwasted.ttf", 35)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.str_ready()
        self.img_ready()
        self.update("0")

    def str_ready(self):
        self.best_score = self.best_list[0]
        self.second_best = self.best_list[1]
        self.trid_best = self.best_list[2]

    def img_ready(self):
        self.best_score_image = self.fonte.render("1: " + self.best_score, True, (0, 0, 0))
        self.best_score_rect = self.best_score_image.get_rect()
        self.second_best_image = self.fonte.render("2: " + self.second_best, True, (0, 0, 0))
        self.second_best_rect = self.second_best_image.get_rect()
        self.trid_best_image = self.fonte.render("3: " + self.trid_best, True, (0, 0, 0))
        self.trid_best_rect = self.trid_best_image.get_rect()

    def update(self, pontos):
        self.pontos = str(pontos)
        self.atual = self.fonte.render("Atual: " + self.pontos, True, (0, 0, 0))
        self.atual_rect = self.atual.get_rect()
        self.position()

    def position(self):
        self.best_score_rect.top = self.screen_rect.top + 10
        self.best_score_rect.right = self.screen_rect.right - 10
        self.atual_rect.top = self.best_score_rect.bottom + 10
        self.atual_rect.right = self.best_score_rect.right
        self.second_best_rect.right = self.best_score_rect.right
        self.second_best_rect.top = self.atual_rect.bottom + 10
        self.trid_best_rect.top = self.second_best_rect.bottom + 10
        self.trid_best_rect.right = self.second_best_rect.right

    def blitall(self):
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.screen.blit(self.atual, self.atual_rect)
        self.screen.blit(self.second_best_image, self.second_best_rect)
        self.screen.blit(self.trid_best_image, self.trid_best_rect)

    def save(self):
        open("score.txt",'w').close()
        with open("score.txt", 'a') as filename:
            for i in self.best_list:
                filename.write(i + "\n")
            filename.write(self.pontos+ "\n")
