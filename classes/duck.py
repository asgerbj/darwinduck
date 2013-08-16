import pygame
import math

class duck(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([30, 50])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.movementdir = 0
		self.movementspeed = 0

	def right(self):
		self.movementspeed += 3

	def left(self):
		self.movementspeed += 3
		
	def update(self):
		print self.movementspeed
		print self.movementdir
		self.rect.y -= self.movementspeed
		if self.movementspeed > 0:
			self.movementspeed -= 0.25
