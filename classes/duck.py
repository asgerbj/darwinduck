import pygame

class duck(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([30, 50])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
