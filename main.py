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

clock = pygame.time.Clock() # Initialize pygame clock

# Create platforms
def create_level1(block_list, slow_list, allsprites):
 
    for x in range(-600, 1500, 200):
        block = Platform(white, 100, 20)
        block.rect.x = x
        block.rect.y = -100
        block_list.add(block)

    for x in range(-500, 1500, 300):
        block = Platform(blue, 100, 20)
        block.rect.x = x
        block.rect.y = 0
        slow_list.add(block)
 
    for x in range(-600, 1500, 200):
        block = Platform(white, 100, 20)
        block.rect.x = x
        block.rect.y = 100
        block_list.add(block)

    allsprites.add(block_list)
    allsprites.add(slow_list)
 
 
# Main program, create the blocks 
block_list = pygame.sprite.Group()
slow_list = pygame.sprite.Group()
allsprites = pygame.sprite.OrderedUpdates() # Create group for all sprites
 
create_level1(block_list, slow_list, allsprites)


duck1 = duck("duck1", white,200,500)
duck2 = duck("duck2", white,300,500)

allsprites.add(duck1)
allsprites.add(duck2)

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
				duck1.left()
			if event.key == pygame.K_LEFT:
				duck1.right()
				
			if event.key == pygame.K_d:
				duck2.left()
			if event.key == pygame.K_a:
				duck2.right()



	# Draw graphics
	screen.fill(bluewater) # Draw background

	block_list.update()
	slow_list.update()
	duck1.update(block_list, slow_list)
	duck2.update(block_list, slow_list)

     
	allsprites.draw(screen)
	# block_list.update()
	
	pygame.display.flip() # Redraw all graphics
	clock.tick(30) # Run game at 50 fps
# - - - END MAIN LOOP - - -
pygame.quit()
sys.exit
