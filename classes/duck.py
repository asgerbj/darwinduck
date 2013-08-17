import pygame
import math
import os

class duck(pygame.sprite.Sprite):
	def __init__(self, name, volume,x,y):
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
		# Load sounds
		self.sound_stone_hit = pygame.mixer.Sound(os.path.join('sound', 'stone_hit.wav'))
		self.sound_stone_hit.set_volume(volume)
		self.sound_duck1 = pygame.mixer.Sound(os.path.join('sound', 'duck_sound1.wav'))
		self.sound_duck1.set_volume(volume)
		self.sound_duck2 = pygame.mixer.Sound(os.path.join('sound', 'duck_sound2.wav'))
		self.sound_duck2.set_volume(volume)
		

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
		speedvar = self.movementspeed
		dirvar = self.movementdir
		for player_collide in player_collision:

			# self.movementspeed = player_collide.movementspeed
			# player_collide.movementspeed = 10

			# self.movementdir = player_collide.movementdir
			# player_collide.movementdir = dirvar


			# if self.rect.x < player_collide.rect.x or player_collide.rect.x < self.rect.x:
				# speedvar = self.movementspeed
				# duckspeed = 0.5	
				# if self.movementspeed > player_collide.movementspeed:
				# 	player_collide.movementdir = self.movementdir
				# 	self.movementspeed -= player_collide.movementspeed * 3
				# 	player_collide.movementspeed = speedvar * duckspeed
				# else: 
				# 	self.movementdir = player_collide.movementdir 
				# 	self.movementspeed = player_collide.movementspeed * duckspeed
				# 	player_collide.movementspeed -= speedvar * 3
			xtra = self.rect.x - player_collide.rect.x
			ytra = self.rect.y - player_collide.rect.y
			if ytra > 22*3/4 and xtra < ytra:
				print "top" + self.name
				player_collide.movementdir =  self.movementdir 
				player_collide.movementspeed += self.movementspeed * 0.5
				self.movementspeed *= -0.3
			elif xtra > 30*3/4  and ytra < xtra:
				print "left" + self.name # hit on left
				self.movementdir = player_collide.movementdir
				self.movementspeed += player_collide.movementspeed * 0.5
				player_collide.movementspeed *= -0.3
			elif xtra < -30*3/4 and ytra > xtra:
				print "right" + self.name
				self.movementdir = player_collide.movementdir
				self.movementspeed += player_collide.movementspeed * 0.5
				player_collide.movementspeed *= -0.3
			elif ytra < -22*3/4 :
				print "bot" + self.name
				self.movementdir = player_collide.movementdir
				self.movementspeed += player_collide.movementspeed * 0.5
				player_collide.movementspeed *= -0.3
			else:
				print "den burde ikke gaa herind "
				print "xtra: " + str(xtra)
				print "ytra: " + str(ytra)



			# if player_collide.rect.y > self.rect.y:
				# self.movementdir = player_collide.movementdir
				# self.movementspeed += player_collide.movementspeed * 0.5
				# player_collide.movementspeed *= -0.3

			# if player_collide.rect.y < self.rect.y:
				# player_collide.movementdir =  self.movementdir 
				# player_collide.movementspeed += self.movementspeed * 0.5
				# self.movementspeed *= -0.3

# VIRKER I Y
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
                    if self.sound_last_collide == False:
                       self.sound_stone_hit.play()
                       self.sound_last_collide = True
                else:
                    self.sound_last_collide = False
                
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
                   
                
