import pygame
import math
import os

class duck(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		# self.image = pygame.Surface([30, 50])
		# self.image.fill(color)
                self.image = pygame.image.load(os.path.join("images/duck1/", "N.png"))
                self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
                self.xpos = float(x)
                self.ypos = float(y)
		self.movementdir = 0
		self.movementspeed = 0

	def right(self):
		self.movementspeed += 2
                self.movementdir -= 30
                if self.movementdir <= 0:
                   self.movementdir = 360

                print ""
                print "movementspeed: " + str(self.movementspeed)
                print "movementdir:   " + str(self.movementdir)

	def left(self):
		self.movementspeed += 2
                self.movementdir += 30
                if self.movementdir >= 360:
                   self.movementdir = 0

                print ""
                print "movementspeed: " + str(self.movementspeed)
                print "movementdir:   " + str(self.movementdir)
		
	def update(self):
		# print self.movementspeed
		self.ypos -= self.movementspeed * math.cos(self.movementdir * math.pi / 180)
                self.rect.y = int(self.ypos)
		self.xpos -= self.movementspeed * math.sin(self.movementdir * math.pi / 180) 
                self.rect.x = int(self.xpos)
		if self.movementspeed > 0:
                   self.movementspeed =  self.movementspeed * 0.95

                if self.movementdir == 0 or self.movementdir == 360:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "N.png"))
                
                if self.movementdir == 30 or self.movementdir == 60:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "NW.png"))

                if self.movementdir == 90:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "W.png"))

                if self.movementdir == 120 or self.movementdir == 150:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "SW.png"))

                if self.movementdir == 180:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "S.png"))

                if self.movementdir == 210 or self.movementdir == 240:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "SE.png"))

                if self.movementdir == 270:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "E.png"))

                if self.movementdir == 300 or self.movementdir == 330:
                   self.image = pygame.image.load(os.path.join("images/duck1/", "NE.png"))


                self.rect.y += 1
                self.ypos += 1
