# Import modules
import os, sys, math
import pygame
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Settings
volume = 1 # Variable used to set volume level.

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

# Initialize pygame
pygame.init() # Launch pygame
pygame.mouse.set_visible(1)
pygame.display.set_caption("Darwin Duck!") # Set title
screen_width, screen_height = 480, 600
screen=pygame.display.set_mode((screen_width, screen_height)) 
pygame.mixer.init()
clock = pygame.time.Clock() # Initialize pygame clock
font = pygame.font.Font(None, 16) # Set font

# Main program, create the blocks 
player_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
slow_list = pygame.sprite.Group()
allsprites = pygame.sprite.OrderedUpdates() # Create group for all sprites

# Create platforms
sys.path.append("levels")
# from level1 import createlevel
from level2 import createlevel
createlevel(block_list, slow_list, allsprites, screen_width)

duck1 = duck("redhead"   , volume, 200, 500)
duck2 = duck("rubberduck", volume, 300, 500)

player_list.add(duck1)
player_list.add(duck2)
allsprites.add(player_list)

run = True
collision_true = False
collision_true_counter = 0
# - - - BEGIN MAIN LOOP - - -
while run == True:
    # Events
    for event in pygame.event.get(): # Check for events
        if event.type == pygame.QUIT: # If close-button is hit
            run = False			
        if event.type == pygame.KEYDOWN: # Keypresses
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_d:
                duck1.right()
            if event.key == pygame.K_a:
                duck1.left()

            if event.key == pygame.K_RIGHT:
                duck2.right()
            if event.key == pygame.K_LEFT:
                duck2.left()

    # Draw graphics
    screen.fill(bluewater) # Draw background

    block_list.update()
    slow_list.update()
    player_list.update(player_list, block_list, slow_list)

    collision_true = duck1.playercollision(player_list)
    # collision_true = duck2.playercollision(player_list)

    # max_collisions = 2
    # if collision_true_counter < 1 :
    # 	collision_true = duck1.playercollision(player_list)
    # 	# collision_true = duck2.playercollision(player_list)
    # if collision_true:
    # 	collision_true_counter += 1
    # 	if collision_true_counter == 2:
    # 	   collision_true_counter = 0
    # 	   collision_true = False



    # duck1.detectsprint(player_list, block_list, slow_list)
    # duck2.detectsprint(player_list, block_list, slow_list)


    allsprites.draw(screen)
    # block_list.update()

    currentfps = int(clock.get_fps())
    text_fps=font.render("fps: "+str(currentfps), True, white)
    screen.blit(text_fps, (screen_width-50, 2))

    pygame.display.flip() # Redraw all graphics
    clock.tick(30) # Run game at 30 fps
# - - - END MAIN LOOP - - -
pygame.quit()
# sys.exit
