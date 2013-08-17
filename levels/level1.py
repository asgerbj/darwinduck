import pygame
import os

class Platform (pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1

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

		allsprites.add(block_list)
		allsprites.add(slow_list)
