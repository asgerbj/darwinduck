import pygame
import math
import os

class duck(pygame.sprite.Sprite):
	def __init__(self, name, color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		# self.image = pygame.Surface([30, 50])
		# self.image.fill(color)
                self.name = name
                self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
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
                if self.movementdir < 0:
                   self.movementdir = 330

	def left(self):
		self.movementspeed += 1
                self.movementdir += 30
                if self.movementdir > 360:
                   self.movementdir = 30

	def detectsprint(self, player_list, block_list, slow_list):
        if self.rect.y <= 50:
            diff = 50 - self.rect.y
            self.rect.y = 50
            self.ypos = 50
        # player2.rect.y += diff
        for block in block_list:
            block.rect.y += 3	
        for block in slow_list:
            block.rect.y += 3
        for player in player_list:
            player.rect.y += 3
            player.ypos = player.rect.y

	def update(self, player_list, block_list, slow_list):
                old_x = self.rect.x
                old_y = self.rect.y

		self.ypos -= self.movementspeed * math.cos(self.movementdir * math.pi / 180)
                self.rect.y = int(self.ypos)
		self.xpos -= self.movementspeed * math.sin(self.movementdir * math.pi / 180) 
                self.rect.x = int(self.xpos)

                slowed = pygame.sprite.spritecollide (self, slow_list, False)
                for i in slowed:
                    self.movementspeed = self.movementspeed * 0.80 # Controls the slow effect

		if self.movementspeed > 0:
                   self.movementspeed =  self.movementspeed * 0.95

                if self.movementdir == 0 or self.movementdir == 360:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
                
                if self.movementdir == 30 or self.movementdir == 60:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "NW.png"))

                if self.movementdir == 90:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "W.png"))

                if self.movementdir == 120 or self.movementdir == 150:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "SW.png"))

                if self.movementdir == 180:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "S.png"))

                if self.movementdir == 210 or self.movementdir == 240:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "SE.png"))

                if self.movementdir == 270:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "E.png"))

                if self.movementdir == 300 or self.movementdir == 330:
                   self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "NE.png"))

                collide = pygame.sprite.spritecollide (self, block_list, False)
                if collide:
                    # We collided, go back to the old pre-collision location
                    self.rect.x = old_x
                    self.rect.y = old_y
                    self.xpos = old_x
                    self.ypos = old_y
                    self.movementspeed = 0

                pygame.sprite.Sprite.remove(self, player_list)
                
                player_collide = pygame.sprite.spritecollide(self, player_list, False)
                if player_collide:
                    # We collided, go back to the old pre-collision location
                    self.rect.x = old_x
                    self.rect.y = old_y
                    self.xpos = old_x
                    self.ypos = old_y
                
                player_list.add(self)
                
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
                   
                
