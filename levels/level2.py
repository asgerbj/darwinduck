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
		for siv in range (-1800, 600, 64):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			siv = (0,siv)
			block = Obstacle(siv, image)
			slow_list.add(block)
	
		for siv in range (-1800, 600, 64):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			siv = (screen_width - 32,siv)
			block = Obstacle(siv, image)
			slow_list.add(block)
			
		for siv in ([32, -50], [32,-120], [32,-190], [32,-280], [64,-150], [64,-225],[96,-170],[96,-250]):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			block = Obstacle(siv, image)
			slow_list.add(block)
	
		for aakande in ([180,-275], [150,150], [390,-340], [350,-550]):
			image = pygame.image.load(os.path.join("images", "aakande.png"))
			block = Obstacle(aakande, image)
			slow_list.add(block)
		
		for rock in ([350,-300], [300,-200], [200,-120]):
			image = pygame.image.load(os.path.join("images", "rock.png"))
			block = Obstacle(rock, image)
			block_list.add(block)
			
		for log in ([128,-180], [300,50], [380,10]):
			image = pygame.image.load(os.path.join("images", "log.png"))
			block = Obstacle(log, image)
			block_list.add(block)
			
		for bigrock in ([196,-350], [256,-500]):
			image = pygame.image.load(os.path.join("images", "bigrock.png"))
			block = Obstacle(bigrock, image)
			block_list.add(block)

		for siv in ([416, -840], [416,-776], [416,-694], [416,-630], \
					[384, -830], [384,-766], [384,-684], \
					[352, -810]):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			block = Obstacle(siv, image)
			slow_list.add(block)
	
		for log in ([32,-900], [96,-900], [160,-900], [224,-900], [288,-900] \
					,[384,-1050], [320,-1050], [256,-1050], [192,-1050]):
			image = pygame.image.load(os.path.join("images", "log.png"))
			block = Obstacle(log, image)
			block_list.add(block)

# After huge row of logs

		for bigrock in ([120,-1200], [300,-1350]):
			image = pygame.image.load(os.path.join("images", "bigrock.png"))
			block = Obstacle(bigrock, image)
			block_list.add(block)

		for rock in ([64,-1300], [194,-1450]):
			image = pygame.image.load(os.path.join("images", "rock.png"))
			block = Obstacle(rock, image)
			block_list.add(block)
			
		for aakande in ([240,-1385], [400,-1310],):
			image = pygame.image.load(os.path.join("images", "aakande.png"))
			block = Obstacle(aakande, image)
			slow_list.add(block)
			
		self.movebundle = -1500
		for siv in ([32, -50+self.movebundle], [32,-120+self.movebundle], [32,-190+self.movebundle], [32,-280+self.movebundle], [64,-150+self.movebundle], [64,-225+self.movebundle],[96,-170+self.movebundle],[96,-250+self.movebundle]):
			image = pygame.image.load(os.path.join("images", "siv.png"))
			block = Obstacle(siv, image)
			slow_list.add(block)

# Sea of damned rocks
		for bigrock in ([140,-1850], [350,-1950], [100,-2050],[50,-2100],[210,-2200],[350,-2300],[40,-2400]):
			image = pygame.image.load(os.path.join("images", "bigrock.png"))
			block = Obstacle(bigrock, image)
			block_list.add(block)

		for rock in ([250,-1700], [410,-1650], [440,-1900],[32,-1900],[400,-2150],[380,-2400],[130,-2450],[250,-2500],[90,-2570],[410,-2520]):
			image = pygame.image.load(os.path.join("images", "rock.png"))
			block = Obstacle(rock, image)
			block_list.add(block)
			
		for aakande in ([270,-2250], [290,-2300],):
			image = pygame.image.load(os.path.join("images", "aakande.png"))
			block = Obstacle(aakande, image)
			slow_list.add(block)
			
		for log in ([105,-2600],[180,-2640],[250,-2645],[315,-2648]):
			image = pygame.image.load(os.path.join("images", "log.png"))
			block = Obstacle(log, image)
			block_list.add(block)
			
		for bigaakande in ([20,-2700], [330,-2720],):
			image = pygame.image.load(os.path.join("images", "bigaakande.png"))
			block = Obstacle(bigaakande, image)
			slow_list.add(block)
		







		allsprites.add(block_list)
		allsprites.add(slow_list)
