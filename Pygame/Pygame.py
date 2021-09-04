'''Pygamae drawing example'''
## Import and initialize the pygame library
#import pygame
#pygame.init()

## Set up the drawing window
#screen = pygame.display.set_mode([500, 500])

## Run until the user asks to quit
#running = True
#while running:

    ## Did the user click the window close button?
    #for event in pygame.event.get(): # For every event detected in event queue
        #print (event) # Print the event
        #if event.type == pygame.QUIT: # If event is detected as quit:
            #running = False # Stop program

    ## Fill the background with white
    #screen.fill((255, 255, 255))

    ## Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    ## Update display
    #pygame.display.flip()

## Done! Time to quit.
#pygame.quit()

#__________________________________________________________________________________________________________________________
'''Moving images example'''

#import sys, pygame
#pygame.init() # initialize

#size = width, height = 320, 240 # Set width to 320, height to 240, and combine them both to a tuple called size
#speed = [1, 1] # Speed values, X speed is the first value, Y speed is the second value
#black = 0, 0, 0

#screen = pygame.display.set_mode(size) # Create a display Surface to certain size

#ball = pygame.image.load("Test.jpg") # Load an image as a Surface object
#ballrect = ball.get_rect() # Turn image into Rect object (rectangle)

#while True: # Infinite loop
    #for event in pygame.event.get(): # Seach all events in event queue
        #if event.type == pygame.QUIT: sys.exit() # If user exits window, exit program

    #ballrect = ballrect.move(speed) # Move the ball by the speed value once
    #if ballrect.left < 0 or ballrect.right > width: # |- If ballrect object touches 
        #speed[0] = -speed[0]                        # |- edges of screen,
    #if ballrect.top < 0 or ballrect.bottom > height:# |- reverse speed value so 
        #speed[1] = -speed[1]                        # |- it goes in opposite direction

    #screen.fill(black) # Erase ball image, fill screen with black so it looks like a black background
    #screen.blit(ball, ballrect) # Redraw ball image by copy/pasting the ball image onto the display SUrface
    #pygame.display.flip() # Update everything
#__________________________________________________________________________________________________________________________
'''Animation'''

import pygame
pygame.init()

loop = 1 # For looping program
screen = pygame.display.set_mode((600,600)) # Set display Surface, with width and height tuple size
color = (5, 5, 5) # Color RGB tuple, represents a RGB color value
rect_color = (250, 100, 255)

# Set a variable to the clock of Pygame
clock = pygame.time.Clock() 

# Fill screen display Surface
screen.fill(color)

# Set movement points
points = [(150,150, 50, 50), (450, 150, 50, 50), (450, 450, 50, 50), (150, 450, 50, 50)]

pointnum = 0

while loop == 1: # Pygame loop
    
    '''Using the ingame clock'''
    clock.tick(10) # FPS
    
    '''Using a time delay'''
    #pygame.time.delay(1000)   
    
    print (pygame.time.get_ticks()) # Total runtime in millisceconds
    #print (clock.get_time()) # Time in milliseconds from previous tick to the next
    #print (clock.get_fps())
    
    for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        if event.type == pygame.QUIT:
            loop = 0
            
    screen.fill(color)
    
    pygame.draw.rect(screen, rect_color, (points[pointnum]), 0)
    
    pointnum += 1
    if pointnum == 4:
        pointnum = 0
    
    
    pygame.display.update() # Call this for every edit to the screen (e.g. Animations)
    


print ("done")
#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________