import pygame
import math
import os

class duck(pygame.sprite.Sprite):
	def __init__(self, name, color,x,y):
		pygame.sprite.Sprite.__init__(self) 
		self.name = name
		self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
		self.rect = self.image.get_rect()
		self.rect = self.rect.inflate(-10,-10)
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
			pygame.sprite.Sprite.remove(self, player_list)
			diff = 50 - self.rect.y
			self.rect.y = 50
			self.ypos = 50
        # player2.rect.y += diff
			for block in block_list:
				block.rect.y += 3	
			for block in slow_list:
				block.rect.y += 3
			for player in player_list:
				player.rect.y += 4
				player.ypos = player.rect.y
			
			player_list.add(self)
	def playercollision(self, player_list):
		pygame.sprite.Sprite.remove(self, player_list)
		
		# player_collide = pygame.sprite.spritecollide(self, player_list, False)
		# if player_collide:
		#     # We collided, go back to the old pre-collision location
		#     self.rect.x = old_x
		#     self.rect.y = old_y
		#     self.xpos = old_x
		#     self.ypos = old_y
		
		player_collision = pygame.sprite.spritecollide(self, player_list, False)
		for player_collide in player_collision:
			# if player_collide.rect.x < self.rect.x:
			# 	self.movementdir = player_collide.movementdir
			# 	self.movementspeed = player_collide.movementspeed * 0.5
			# 	player_collide.movementspeed *= -0.3

			if self.rect.x < player_collide.rect.x or player_collide.rect.x < self.rect.x:
				# player_collide.movementdir = self.movementdir
				speedvar = self.movementspeed
				self.movementspeed -= player_collide.movementspeed * 0.1
				player_collide.movementspeed -= speedvar * 0.1

			# if player_collide.rect.y > self.rect.y:
			# 	self.movementdir = player_collide.movementdir
			# 	self.movementspeed += player_collide.movementspeed * 0.5
			# 	player_collide.movementspeed *= -0.3

			# if player_collide.rect.y < self.rect.y:
			# 	player_collide.movementdir =  self.movementdir 
			# 	player_collide.movementspeed += self.movementspeed * 0.5
			# 	self.movementspeed *= -0.3

		player_list.add(self)

	def update(self, player_list, block_list, slow_list):
                old_x = self.rect.x
                old_y = self.rect.y

		self.ypos -= self.movementspeed * math.cos(self.movementdir * math.pi / 180)
                self.rect.y = int(self.ypos)
		self.xpos -= self.movementspeed * math.sin(self.movementdir * math.pi / 180) 
                self.rect.x = int(self.xpos)

                slowed = pygame.sprite.spritecollide (self, slow_list, False)
                for i in slowed:
                    self.movementspeed = self.movementspeed * 0.9 # Controls the slow effect

		# if self.movementspeed > 0:
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

				# self.hitbox = self.rect.inflate(-5,-5)
                collide = pygame.sprite.spritecollide (self, block_list, False)
                if collide:
                    # We collided, go back to the old pre-collision location
                    self.rect.x = old_x
                    self.rect.y = old_y
                    self.xpos = old_x
                    self.ypos = old_y
                    self.movementspeed = 0

                
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

                # self.rect.y += 1
                # self.ypos += 1

                if self.rect.y > 600:
                   self.kill()
                   
                
