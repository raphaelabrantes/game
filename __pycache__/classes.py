import pygame
import pygame.font
from random import choice


class Estado:
    def __init__(self, tela, sigla, nome, posicao, capital, habitantes, natural, regiao):
        self.nome = nome
        self.sigla = sigla
        self.habitantes = habitantes
        self.natural = natural
        self.regiao = regiao
        self.imagem = pygame.image.load("Estados/" + self.sigla + ".png")
        self.imagem_rect = self.imagem.get_rect()
        self.preto = (0, 0, 0)
        self.tela = tela
        self.x = posicao[0]
        self.y = posicao[1]
        self.capital = capital
        self.desenho()

    def desenho(self):
        self.lugar = pygame.draw.rect(self.tela, self.preto, (self.x, self.y, 10, 10))


class Brasil:
    def __init__(self, tela):
        self.image = pygame.image.load("brasil-estado.png")
        self.rect = self.image.get_rect()
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.estados = [Estado(tela, "AC", "Acre",(270, 270), "Rio Branco", "800.000", "acreano", "Norte"),
                        Estado(tela, "AL", "Alagoas", (828, 292), "Maceio","3.300.000", "alagoano", "Nordeste"),
                        Estado(tela, "AP", "Amapa", (580, 106), "Macapa", "750.000", "amapaense", "Norte"),
                        Estado(tela, "AM", "Amazonas", (337, 199), "Manaus", "4.000.000", "amazonense", "Norte"),
                        Estado(tela, "BA", "Bahia", (735, 333), "Salvador", "15.300.000", "baiano", "Nordeste"),
                        Estado(tela, "CE", "Ceara", (778, 208), "Fortaleza", "9.000.000", "cearense", "Nordeste"),
                        Estado(tela, "DF", "Distrito Federal", (635, 380), "Brasilia", "3.000.000", "brasiliense", "Centro-Oeste"),
                        Estado(tela, "ES", "Espirito Santo", (749, 453), "Vitoria", "4.000.000", "capixaba", "Sudeste"),
                        Estado(tela, "GO", "Goiais", (603, 398), "Goiania", "6.800.000", "goiano", "Centro-Oeste"),
                        Estado(tela, "MA", "Maranhao", (679, 200), "Sao Luis", "7.000.000", "maranhense", "Nordeste"),
                        Estado(tela, "MT", "Mato Grosso",(522, 339), "Cuiaba", "3.300.000", "mato-grossense", "Centro-Oeste"),
                        Estado(tela, "MS", "Mato Grosso do Sul", (529, 460), "Campo Grande", "2.700.000", "mato-grossense-do-sul", "Centro-Oeste"),
                        Estado(tela, "MG", "Minas Gerais", (683, 434), "Belo Horizonte", "21.000.000", "mineiro", "Sudeste"),
                        Estado(tela, "PA", "Para", (552, 203), "Belem", "8.300.000", "paraense", "Norte"),
                        Estado(tela, "PB", "Paraiba", (837, 248), "Joao Pessoa", "4.000.000", "paraibano", "Nordeste"),
                        Estado(tela, "PR", "Parana", (570, 523), "Curitiba", "11.300.000", "paranaense", "Sul"),
                        Estado(tela, "PE", "Pernambuco", (831, 270), "Recife", "9.400.000", "pernambucano", "Nordeste"),
                        Estado(tela, "PI", "Piaui", (729, 251), "Teresina", "3.200.000", "piauiense", "Nordeste"),
                        Estado(tela, "RJ", "Rio de Janeiro", (719, 493), "Rio de Janeiro", "16.700.000", "carioca", "Sudeste"),
                        Estado(tela, "RN", "Rio Grande do Norte", (825, 222), "Natal", "3.500.000", "rio-grandense-do-norte", "Nordeste"),
                        Estado(tela, "RS", "Rio Grande do Sul", (544, 604), "Porto Alegre", "11.300.000", "gaucho", "Sul"),
                        Estado(tela, "RO", "Rondonia", (387, 302), "Porto Velho", "1.800.000", "rondoniense", "Norte"),
                        Estado(tela, "RR", "Roraima", (408, 88), "Boa Vista", "500.000", "roraimense", "Norte"),
                        Estado(tela, "SC", "Santa Catarina", (593, 567), "Florianopolis", "6.900.000", "catarinense", "Sul"),
                        Estado(tela, "SP", "Sao Paulo", (617, 487), "Sao Paulo", "45.000.000", "paulista", "Sudeste"),
                        Estado(tela, "SE", "Sergipe", (812, 308), "Aracaju", "2.200.000", "sergipense", "Nordeste"),
                        Estado(tela, "TO", "Tocantins", (622, 296), "Palmas", "1.500.000", "tocantinense", "Norte")]
        self.posicionar()

    def posicionar(self):
        self.rect.centerx = self.tela_rect.centerx
        self.rect.centery = self.tela_rect.centery

    def render(self):
        self.tela.blit(self.image, self.rect)
        for estado in self.estados:
            estado.desenho()


class Menu:
    def __init__(self, tela):
        play = 'JOGAR'
        exit = 'SAIR DO JOGO'
        regras_opcao = "REGRAS"
        with open("regras.txt") as filename:
            self.linhas = filename.readlines()

        self.image = pygame.image.load("menu2.png")
        self.rect = self.image.get_rect()
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.on = True
        self.regras_status = True
        self.fonte = pygame.font.SysFont(None, 30)
        self.fonte2 = pygame.font.SysFont(None, 20)
        self.font_ready(play, exit, regras_opcao)

    def font_ready(self, play, exit, regras_opcao):
        self.rect.center = self.tela_rect.center
        self.play = self.fonte.render(play, True, (0, 0, 0))
        self.exit = self.fonte.render(exit, True, (0, 0, 0))
        self.regras_b = self.fonte.render(regras_opcao, True, (0, 0, 0))


        self.play_rect = self.play.get_rect()
        self.exit_rect = self.exit.get_rect()
        self.regras_b_rect = self.regras_b.get_rect()

        self.play_rect.centerx = self.rect.centerx
        self.play_rect.top = self.tela_rect.top + 255

        self.exit_rect.bottom = self.rect.bottom - 20
        self.exit_rect.centerx = self.rect.centerx

        self.regras_b_rect.top = self.play_rect.bottom + 50
        self.regras_b_rect.centerx = self.rect.centerx

        contador = 0

        self.regras_lista = []
        for linha in self.linhas:
            lin = self.fonte2.render(linha.strip("\n"), True, (0, 0, 0))
            lin_rect = lin.get_rect()
            lin_rect.left = self.rect.left + 10
            if contador == 0:
                lin_rect.top = self.rect.top + 75
                contador += 15

            else:
                lin_rect.top = self.rect.top + 75 + contador
                contador += 15

            self.regras_lista.append((lin, lin_rect))

    def display_info(self):
        self.tela.blit(self.play, self.play_rect)
        self.tela.blit(self.exit, self.exit_rect)
        self.tela.blit(self.regras_b, self.regras_b_rect)

    def show_regras(self):
        for regra in self.regras_lista:
            self.tela.blit(regra[0], regra[1])
        self.tela.blit(self.exit, self.exit_rect)

    def render(self):
        self.tela.blit(self.image, self.rect)


class Perguntas:
    def __init__(self, tela):
        self.on = False
        self.errada = False
        self.contador = 0
        self.fonte = pygame.font.SysFont(None, 30)
        self.tela = tela

    def seta_parametros(self, estado, redutor, brasil):
        self.estado = estado
        self.redutor = redutor
        self.brasil = brasil
        self.estado_image = estado.imagem
        self.estado_rect = estado.imagem_rect
        self.index = [i for i in range(0, 27)]
        for i in self.index:
            if brasil.estados[i].regiao == estado.regiao:
                self.index.remove(i)
                self.index.insert(i, "")

        if self.redutor == -3:
            self.perguntas = {self.estado.capital : "capital", self.estado.natural: "natural",
                         self.estado.habitantes: "habitantes"}

        elif self.redutor == -2:
            self.perguntas = {self.estado.nome:"nome", self.estado.regiao: "regiao",  self.estado.sigla: "sigla"}

    def escolha_index(self):
        c_index1 = choice(self.index)
        while c_index1 == "":
            c_index1 = choice(self.index)
        self.index.remove(c_index1)
        self.index.insert(c_index1, "")

        c_index2 = choice(self.index)
        while c_index2 == "":
            c_index2 = choice(self.index)
        self.index.remove(c_index2)
        self.index.insert(c_index2, "")

        c_index3 = choice(self.index)
        while c_index3 == "":
            c_index3 = choice(self.index)

        self.random_pergunta(c_index1, c_index2, c_index3)

    def random_pergunta(self, c_index1, c_index2, c_index3):
        if self.redutor == -3:
            self.random_dificil(c_index1, c_index2, c_index3)

        elif self.redutor == -2:
            self.random_normal(c_index1, c_index2, c_index3)

    def random_dificil(self, c_index1, c_index2, c_index3):
        self.pergunta = self.perguntas[choice([self.estado.capital, self.estado.natural, self.estado.habitantes])]
        if self.pergunta == "capital":
            self.resposta = self.estado.capital
            self.fake1 = self.brasil.estados[c_index1].capital
            self.fake2 = self.brasil.estados[c_index2].capital
            self.fake3 = self.brasil.estados[c_index3].capital

        elif self.pergunta == "natural":
            self.resposta = self.estado.natural
            self.fake1 = self.brasil.estados[c_index1].natural
            self.fake2 = self.brasil.estados[c_index2].natural
            self.fake3 = self.brasil.estados[c_index3].natural

        elif self.pergunta == "habitantes":
            self.resposta = self.estado.habitantes

            self.fake1 = self.brasil.estados[c_index1].habitantes
            if self.fake1 == self.resposta:
                for estado in self.brasil.estados:
                    if estado == "" or estado.habitantes == self.resposta:
                        pass
                    else:
                        self.fake1 = estado.habitantes

            self.fake2 = self.brasil.estados[c_index2].habitantes
            if self.fake2 == self.fake1 or self.fake2 == self.resposta:
                for estado in self.brasil.estados:
                    if estado == "" or estado.habitantes == self.fake1 or estado.habitantes == self.resposta:
                        pass
                    else:
                        self.fake2 = estado.habitantes

            self.fake3 = self.brasil.estados[c_index3].habitantes
            if self.fake1 == self.fake3 or self.fake2 == self.fake3 or self.resposta == self.fake3:
                for estado in self.brasil.estados:
                    if estado == "" or estado.habitantes == self.fake1 or estado.habitantes == self.resposta or estado.habitantes == self.fake2:
                        pass
                    else:
                        self.fake3 = estado.habitantes

    def random_normal(self,  c_index1, c_index2, c_index3):
        self.pergunta = self.perguntas[choice([self.estado.nome, self.estado.regiao, self.estado.sigla])]

        if self.pergunta == "nome":
            self.resposta = self.estado.nome
            self.fake1 = self.brasil.estados[c_index1].nome
            self.fake2 = self.brasil.estados[c_index2].nome
            self.fake3 = self.brasil.estados[c_index3].nome

        elif self.pergunta == "regiao":
            self.resposta = self.estado.regiao
            self.fake1 = self.brasil.estados[c_index1].regiao
            if self.fake1 == self.resposta:
                for estado in self.brasil.estados:
                    if estado == "" or estado.regiao == self.resposta:
                        pass
                    else:
                        self.fake1 = estado.regiao

            self.fake2 = self.brasil.estados[c_index2].regiao
            if self.fake2 == self.fake1 or self.fake2 == self.resposta:
                for estado in self.brasil.estados:
                    if estado == "" or estado.regiao == self.fake1 or estado.regiao == self.resposta:
                        pass
                    else:
                        self.fake2 = estado.regiao

            self.fake3 = self.brasil.estados[c_index3].regiao
            if self.fake1 == self.fake3 or self.fake2 == self.fake3 or self.resposta == self.fake3:
                for estado in self.brasil.estados:
                    if estado == "" or estado.regiao == self.fake1 or estado.regiao == self.resposta or estado.regiao == self.fake2:
                        pass
                    else:
                        self.fake3 = estado.regiao

        elif self.pergunta == "sigla":
            self.resposta = self.estado.sigla
            self.fake1 = self.brasil.estados[c_index1].sigla
            self.fake2 = self.brasil.estados[c_index2].sigla
            self.fake3 = self.brasil.estados[c_index3].sigla

    def ordenador(self):

        possiveis = [self.resposta, self.fake1, self.fake2, self.fake3]
        ordem1 = choice(possiveis)
        possiveis.remove(ordem1)
        ordem2 = choice(possiveis)
        possiveis.remove(ordem2)
        ordem3 = choice(possiveis)
        possiveis.remove(ordem3)
        ordem4 = possiveis.pop()
        self.ordem1_a = ordem1
        self.ordem2_a = ordem2
        self.ordem3_a = ordem3
        self.ordem4_a = ordem4

        self.pergunta_r = self.fonte.render("Qual é o(a) " + self.pergunta + " desse estado", True, (0, 0, 0))
        self.pergunta_r_rect = self.pergunta_r.get_rect()

        self.ordem1 = self.fonte.render(ordem1, True, (0, 0, 0))
        self.ordem1_rect = self.ordem1.get_rect()
        self.ordem2 = self.fonte.render(ordem2, True, (0, 0, 0))
        self.ordem2_rect = self.ordem2.get_rect()
        self.ordem3 = self.fonte.render(ordem3, True, (0, 0, 0))
        self.ordem3_rect = self.ordem3.get_rect()
        self.ordem4 = self.fonte.render(ordem4, True, (0, 0, 0))
        self.ordem4_rect = self.ordem4.get_rect()

        self.pergunta_r_rect.top = self.estado_rect.bottom + 110
        self.pergunta_r_rect.x = 10
        self.ordem1_rect.top = self.estado_rect.bottom + 140
        self.ordem1_rect.x = 10
        self.ordem2_rect.top = self.ordem1_rect.bottom + 10
        self.ordem2_rect.x = 10
        self.ordem3_rect.top = self.ordem2_rect.bottom + 10
        self.ordem3_rect.x = 10
        self.ordem4_rect.top = self.ordem3_rect.bottom + 10
        self.ordem4_rect.x = 10
        self.on = True

    def render(self):
        self.tela.blit(self.pergunta_r, self.pergunta_r_rect)
        self.tela.blit(self.estado_image, self.estado_rect)
        self.tela.blit(self.ordem1, self.ordem1_rect)
        self.tela.blit(self.ordem2, self.ordem2_rect)
        self.tela.blit(self.ordem3, self.ordem3_rect)
        self.tela.blit(self.ordem4, self.ordem4_rect)

    def render_resposta(self):
        texto = "A resposta correta era: " + self.resposta
        continuar = "Continuar"
        resposta_render = self.fonte.render(texto, True, (255, 0, 0))
        continuar_render = self.fonte.render(continuar, True, (255, 0, 0))
        resposta_render_rect = resposta_render.get_rect()
        resposta_render_rect.top = self.ordem4_rect.bottom + 10
        resposta_render_rect.left = self.ordem4_rect.left
        self.continuar_render_rect = continuar_render.get_rect()
        self.continuar_render_rect.top = resposta_render_rect.bottom + 10
        self.continuar_render_rect.left = resposta_render_rect.left
        self.tela.blit(resposta_render, resposta_render_rect)
        self.tela.blit(continuar_render, self.continuar_render_rect)
        self.errada = True


class Pontuacao:
    def __init__(self, tela):
        self.pontuacao_defined = False
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.pontuacao = 0
        self.fonte = pygame.font.SysFont(None, 30)
        self.normal_buttom = self.fonte.render("NORMAL", True, (0, 0, 0))
        self.normal_buttom_r = self.normal_buttom.get_rect()
        self.dificil_buttom = self.fonte.render("DIFICIL", True, (0, 0, 0))
        self.dificil_buttom_r = self.dificil_buttom.get_rect()
        self.normal_buttom_r.center = self.tela_rect.center
        self.normal_buttom_r.y = self.normal_buttom_r.y - 20
        self.dificil_buttom_r.center = self.tela_rect.center
        self.dificil_buttom_r.top = self.normal_buttom_r.bottom + 20

    def dificil(self):
        self.adisionador = 5
        self.redutor = - 3

    def normal(self):
        self.adisionador = 5
        self.redutor = -2

    def add(self, conta):
        self.pontuacao += conta

    def render(self):
        fonte = self.fonte.render("Pontuacao: " + str(self.pontuacao), True, (0, 0, 0))
        fonte_rect = fonte.get_rect()
        fonte_rect.top = self.tela_rect.top
        fonte_rect.right = self.tela_rect.right - 10
        self.tela.blit(fonte, fonte_rect)

    def render_menu(self):
        self.tela.blit(self.normal_buttom, self.normal_buttom_r)
        self.tela.blit(self.dificil_buttom, self.dificil_buttom_r)

    def render_final(self, menu):
        menu_rect = menu.rect
        total = "Pontuação Final: " + str(self.pontuacao)
        if self.pontuacao == 25:
            premio = self.fonte.render("5 troféus: Gênio", True, (0, 0, 0))

        elif self.pontuacao < 25 and self.pontuacao > 20:
            premio = self.fonte.render("4 troféus:Muito inteligente.", True, (0, 0, 0))

        elif self.pontuacao < 20 and self.pontuacao > 15:
            premio = self.fonte.render("3 troféus:Esperto.", True, (0, 0, 0))

        elif self.pontuacao < 15 and self.pontuacao > 10:
            premio = self.fonte.render("2 troféus:Você não foi tão bem.", True, (0, 0, 0))

        elif self.pontuacao < 10 and self.pontuacao > 5:
            premio = self.fonte.render("1 troféu:Melhor na próxima.", True, (0, 0, 0))

        elif self.pontuacao < 5:
            premio = self.fonte.render("0 troféus:Precisa estudar mais", True, (0, 0, 0))


        pontuacao = self.fonte.render(total, True, (0, 0, 0))
        premio_rect = premio.get_rect()
        pontuacao_rect = pontuacao.get_rect()
        pontuacao_rect.top = menu_rect.top + 87
        pontuacao_rect.left = menu_rect.left + 10
        premio_rect.top = pontuacao_rect.bottom + 10
        premio_rect.left = pontuacao_rect.left
        self.tela.blit(pontuacao, pontuacao_rect)
        self.tela.blit(premio, premio_rect)

