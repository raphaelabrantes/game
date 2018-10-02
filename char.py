import pygame

class Char:
	def __init__(self, screen):
		self.alive = True
		self.jumping = False
		self.up = False
		self.status = 1
		self.get_images(screen)
		self.get_rects()
		self.set_rects()
		
	def get_images(self, screen):
		self.screen = screen
		self.walk1 = pygame.image.load("char/walk1.png")
		self.walk2 = pygame.image.load("char/walk2.png")
		self.walk3 = pygame.image.load("char/walk3.png")
		self.walk4 = pygame.image.load("char/walk4.png")
		self.walk5 = pygame.image.load("char/walk5.png")
		self.walk6 = pygame.image.load("char/walk6.png")
		self.stop_w = pygame.image.load("char/stop_w.png")
		self.hit = pygame.image.load("char/hit.png")
		self.hit_2 = pygame.image.load("char/hit2.png")

	def get_rects(self):
		self.walk_rect = self.walk1.get_rect()
		self.hit_rect = self.hit_2.get_rect()
		self.screen_rect = self.screen.get_rect()

	def set_rects(self):
		self.walk_rect.bottom = self.screen_rect.bottom - 20
		self.walk_rect.left = self.screen_rect.left + 30
		self.hit_rect.bottom = self.walk_rect.bottom 
		self.hit_rect.left = self.walk_rect.left

	def blitme(self):
		if self.status > 0  and self.status <= 3:
			self.screen.blit(self.walk1, self.walk_rect)
		elif self.status > 3 and self.status <= 6:
			self.screen.blit(self.walk2, self.walk_rect)
		elif self.status > 6 and self.status <= 9:
			self.screen.blit(self.walk3, self.walk_rect)
		elif self.status > 9 and self.status <= 12:
			self.screen.blit(self.walk4, self.walk_rect)
		elif self.status > 12 and self.status <= 15:
			self.screen.blit(self.walk5, self.walk_rect)	
		elif self.status > 15  and self.status <= 18:
			self.screen.blit(self.walk6, self.walk_rect)

		elif self.status == 70:
			self.screen.blit(self.hit, self.walk_rect)

		elif self.status == 80:
			self.screen.blit(self.hit_2, self.hit_rect)

		elif self.status==90:
			self.screen.blit(self.stop_w, self.walk_rect)
	
