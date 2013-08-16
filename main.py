# Import modules
import os, sys
import pygame
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Colourcodes
black = ( 0, 0, 0)
white = ( 255, 255, 255)
bluewater = ( 25, 155, 225)

# Import classes
sys.path.append("classes")
from duck import duck

# Initialize pygame
pygame.init() # Launch pygame
pygame.mouse.set_visible(1)
pygame.display.set_caption("Darwin Duck!") # Set title
window = pygame.display.set_mode([500,600]) # Set display size
screen = pygame.display.get_surface()

clock = pygame.time.Clock() # Initialize pygame clock

player1 = duck(white,200,300)

allsprites = pygame.sprite.OrderedUpdates() # Create group for all sprites
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

	# Draw graphics
	screen.fill(bluewater) # Draw background
	allsprites.draw(screen)
	
	pygame.display.flip() # Redraw all graphics
	clock.tick(50) # Run game at 50 fps
# - - - END MAIN LOOP - - -
pygame.quit()
sys.exit
