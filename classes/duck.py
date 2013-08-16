import pygame
import math
import os

class duck(pygame.sprite.Sprite):
	def __init__(self, name, color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		# self.image = pygame.Surface([30, 50])
		# self.image.fill(color)
                self.name = name
                self.image = pygame.image.load(os.path.join("images/duck1/", "N.png"))
                self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
                self.xpos = float(x)
                self.ypos = float(y)
		self.movementdir = 0
		self.movementspeed = 5

	def right(self):
		self.movementspeed += 1
                self.movementdir -= 30
                if self.movementdir <= 0:
                   self.movementdir = 360

	def left(self):
		self.movementspeed += 1
                self.movementdir += 30
                if self.movementdir >= 360:
                   self.movementdir = 0

	def update(self, block_list, slow_list):
                old_x = self.rect.x
                old_y = self.rect.y

		self.ypos -= self.movementspeed * math.cos(self.movementdir * math.pi / 180)
                self.rect.y = int(self.ypos)
		self.xpos -= self.movementspeed * math.sin(self.movementdir * math.pi / 180) 
                self.rect.x = int(self.xpos)

                slowed = pygame.sprite.spritecollide (self, slow_list, False)
                for i in slowed:
                    self.movementspeed -= 0.4 # Controls the slow effect

		if self.movementspeed > 0:
                   self.movementspeed =  self.movementspeed * 0.95

   # data = [line.strip() for line in open("map%d.txt"%map)]
                if self.movementdir == 0 or self.movementdir == 360:
                   # self.image = pygame.image.load(os.path.join("images/duck1/", "N.png"))
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
                
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

                collide = pygame.sprite.spritecollide (self, block_list, False)
                if collide:
                    # We collided, go back to the old pre-collision location
                    self.rect.x = old_x
                    self.rect.y = old_y
                    self.xpos = old_x
                    self.ypos = old_y
                    self.movementspeed = 0

                if self.rect.y <= 50:
                   diff = 50 - self.rect.y
                   self.rect.y = 50
                   self.ypos = 50
                   # player2.rect.y += diff
                   for block in block_list:
                       block.rect.y += 3	
                   for block in slow_list:
                       block.rect.y += 3	

                if self.rect.y >= 600 : # screen height
                   # diff = player1.rect.y - 500
                   self.rect.y = 600 - self.rect[3]
                   # player2.rect.y -= diff
                   # for block in block_list:
                   #     block.rect.y -= diff

                if self.rect.x <= 0:
                   # diff = player1.rect.y - 500
                   self.rect.x = 0
                   self.xpos = 0

                if self.rect.x >= 500 - self.rect[2]:
                   # diff = player1.rect.y - 500
                   self.rect.x = 500 - self.rect[2]
                   self.xpos = 500  - self.rect[2]

                self.rect.y += 1
                self.ypos += 1

                if self.rect.y > 600:
                   self.kill()
