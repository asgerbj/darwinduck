import pygame
import os

class Obstacle (pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect.y += 1

class createlevel:
	def __init__(self, block_list, slow_list, allsprites, screen_width):
		for siv in range (-3000, 600, 64):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			siv = (0,siv)
			block = Obstacle(siv, image)
			slow_list.add(block)
	
		for siv in range (-3000, 600, 64):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			siv = (screen_width - 32,siv)
			block = Obstacle(siv, image)
			slow_list.add(block)
			
		for siv in ([32, -50], [32,-120], [32,-190], [32,-280], [64,-150], [64,-225],[96,-170],[96,-250]):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			block = Obstacle(siv, image)
			slow_list.add(block)
	
		for aakande in ([194,-300], [350,100]):
			image = pygame.image.load(os.path.join("images", "aakande.png"))
			block = Obstacle(aakande, image)
			slow_list.add(block)
		
		for rock in ([350,0], [300,150], [200,-120]):
			image = pygame.image.load(os.path.join("images", "rock.png"))
			block = Obstacle(rock, image)
			block_list.add(block)
			
		for log in ([128,-180], [300,50], [380,10]):
			image = pygame.image.load(os.path.join("images", "log.png"))
			block = Obstacle(log, image)
			block_list.add(block)
			
		for log in ([32,-900], [96,-900], [160,-900], [224,-900], [288,-900] \
					,[416,-1050], [352,-1050], [288,-1050], [224,-1050], [160,-1050]):
			image = pygame.image.load(os.path.join("images", "log.png"))
			block = Obstacle(log, image)
			block_list.add(block)

		allsprites.add(block_list)
		allsprites.add(slow_list)
