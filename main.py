# Import modules
import os, sys, math
import pygame
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Settings
volume = 0.5 # Variable used to set volume level.

# Colourcodes
black = ( 0, 0, 0)
blue  = ( 0, 255, 0)
red = ( 255, 0 , 0)
white = ( 255, 255, 255)
# bluewater = ( 25, 155, 225)
bluewater = ( 29, 108, 152)

# Import classes
sys.path.append("classes")
from duck import duck

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

# Initialize pygame
pygame.init() # Launch pygame
pygame.mouse.set_visible(1)
pygame.display.set_caption("Darwin Duck!") # Set title
screen_width, screen_height = 500, 600
screen=pygame.display.set_mode((screen_width, screen_height)) 
pygame.mixer.init()
clock = pygame.time.Clock() # Initialize pygame clock

# Create platforms
def create_level1(block_list, slow_list, allsprites):

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

	for aakande in ([100,100], [300,100], [300, -200], [300, -400]):
		image = pygame.image.load(os.path.join("images", "aakande.png"))
		block = Obstacle(aakande, image)
		slow_list.add(block)
	
	for rock in ([200,100], [300,150], [300, -250], [300, -450]):
		image = pygame.image.load(os.path.join("images", "rock.png"))
		block = Obstacle(rock, image)
		block_list.add(block)
		
	for log in ([200,0], [300,50]):
		image = pygame.image.load(os.path.join("images", "log.png"))
		block = Obstacle(log, image)
		block_list.add(block)

	allsprites.add(block_list)
	allsprites.add(slow_list)
 
 
# Main program, create the blocks 
player_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
slow_list = pygame.sprite.Group()
allsprites = pygame.sprite.OrderedUpdates() # Create group for all sprites
 
create_level1(block_list, slow_list, allsprites)

duck1 = duck("rubberduck", volume,200,500)
duck2 = duck("redhead", volume,300,500)

player_list.add(duck1)
player_list.add(duck2)
allsprites.add(player_list)

run = True
# - - - BEGIN MAIN LOOP - - -
while run == True:
	# Events
	for event in pygame.event.get(): # Check for events
		if event.type == pygame.QUIT: # If close-button is hit
			run = False			
		if event.type == pygame.KEYDOWN: # Keypresses
			if event.key == pygame.K_ESCAPE:
				run = False
			
			if event.key == pygame.K_RIGHT:
				duck1.right()
			if event.key == pygame.K_LEFT:
				duck1.left()
				
			if event.key == pygame.K_d:
				duck2.right()
			if event.key == pygame.K_a:
				duck2.left()



	# Draw graphics
	screen.fill(bluewater) # Draw background

	block_list.update()
	slow_list.update()
	player_list.update(player_list, block_list, slow_list)

	duck1.playercollision(player_list)
	duck2.playercollision(player_list)

	duck1.detectsprint(player_list, block_list, slow_list)
	duck2.detectsprint(player_list, block_list, slow_list)

     
	allsprites.draw(screen)
	# block_list.update()
	
	pygame.display.flip() # Redraw all graphics
	clock.tick(30) # Run game at 30 fps
# - - - END MAIN LOOP - - -
pygame.quit()
sys.exit
