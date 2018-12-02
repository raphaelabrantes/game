# noinspection PyUnresolvedReferences
import pygame
import random


class Inimigos:
    def __init__(self, screen):
        self.dificuldade = 0
        self.baril = pygame.image.load("objetos//barrilok2.png")
        self.drone = pygame.image.load("objetos//droneok.png")
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.lista = []

    def generate_rando(self):
        contador = 0
        for i in range(self.dificuldade):

            choice = random.choice([self.baril, self.drone])
            if choice == self.baril:
                image_rect = choice.get_rect()
                image_rect.bottom = self.screen_rect.bottom - 20
                image_rect.right = self.screen_rect.right + contador
                contador += random.randint(500, 800)

            else:
                image_rect = self.drone.get_rect()
                image_rect.top = self.screen_rect.top + 100
                image_rect.right = self.screen_rect.right + contador
                contador += random.randint(500, 800)
            self.lista.append(image_rect)

    def check_in_clean(self, alive):
        if len(self.lista) == 0:
            self.dificuldade += 1
            self.generate_rando()
        else:
            self.blit(alive)
            self.pop()

    def blit(self, alive):
        for i in range(len(self.lista)):
            if self.lista[i].left <= self.screen_rect.right + 300:
                if self.lista[i].top == self.screen_rect.top + 100:
                    self.screen.blit(self.drone, self.lista[i])
                else:
                    self.screen.blit(self.baril, self.lista[i])
            if alive:
                self.lista[i].right = self.lista[i].right - 5

    def pop(self):
        for i in self.lista:
            if i.x < -200:
                self.lista.remove(i)
