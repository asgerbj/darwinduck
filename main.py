# Import modules
import os, sys, math
import pygame
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Colourcodes
black = ( 0, 0, 0)
blue  = ( 0, 255, 0)
white = ( 255, 255, 255)
bluewater = ( 25, 155, 225)

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


# Initialize pygame
pygame.init() # Launch pygame
pygame.mouse.set_visible(1)
pygame.display.set_caption("Darwin Duck!") # Set title
screen_width, screen_height = 500, 600
screen=pygame.display.set_mode((screen_width, screen_height)) 
# window = pygame.display.set_mode([500,600]) # Set display size
# window = pygame.display.set_mode([500,600]) # Set display size
# screen = pygame.display.get_surface()

clock = pygame.time.Clock() # Initialize pygame clock

# Create platforms
def create_level1(block_list,all_sprites_list):
 
    for x in range(-600, 1500, 200):
        block = Platform(white, 100, 20)
        # Set x and y 
        block.rect.x = x
        block.rect.y = -100
 
        block_list.add(block)
        # all_sprites_list.add(block)
 
    for x in range(-600, 1500, 200):
        block = Platform(white, 100, 20)
        # Set x and y 
        block.rect.x = x
        block.rect.y = 420
 
        block_list.add(block)
        # all_sprites_list.add(block)

    for x in range(-500, 1500, 300):
        block = Platform(blue, 100, 20)
        # Set x and y 
        block.rect.x = x
        block.rect.y = 340
 
        block_list.add(block)
        allsprites.add(block_list)
 
 
# Main program, create the blocks 
block_list = pygame.sprite.Group()
 
allsprites = pygame.sprite.OrderedUpdates() # Create group for all sprites
 
create_level1(block_list,allsprites)


player1 = duck(white,200,500)

allsprites.add(player1)

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
				player1.left()
			if event.key == pygame.K_LEFT:
				player1.right()
				



	# Draw graphics
	screen.fill(bluewater) # Draw background
	player1.update()
	block_list.update()

        if player1.rect.y <= 50:
 	   diff = 50 - player1.rect.y
 	   player1.rect.y = 50
 	   # player2.rect.y += diff
 	   for block in block_list:
 	       block.rect.y += diff
     
	if player1.rect.y >= screen_height:
	   # player1.kill()
 	   # diff = player1.rect.y - 500
 	   player1.rect.y = screen_height-player1.rect[3]
 	   # player2.rect.y -= diff
 	   # for block in block_list:
 	   #     block.rect.y -= diff

	if player1.rect.x <= 0:
 	   # diff = player1.rect.y - 500
 	   player1.rect.x = 0
 	   player1.xpos = 0

	if player1.rect.x >= screen_width - player1.rect[2]:
 	   # diff = player1.rect.y - 500
 	   player1.rect.x = screen_width - player1.rect[2]
 	   player1.xpos = screen_width - player1.rect[2]


	allsprites.draw(screen)
	block_list.update()
	
	pygame.display.flip() # Redraw all graphics
	clock.tick(30) # Run game at 50 fps
# - - - END MAIN LOOP - - -
pygame.quit()
sys.exit
