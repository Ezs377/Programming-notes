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
import sys, pygame
pygame.init() # initialize

size = width, height = 320, 240 # Set width to 320, height to 240, and combine them both to a tuple called size
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size) # Create a display Surface to certain size

ball = pygame.image.load("Test.jpg") # Load an image as a Surface object
ballrect = ball.get_rect() # Turn image into Rect object

while True: # Infinite loop
    for event in pygame.event.get(): # Seach all events in event queue
        if event.type == pygame.QUIT: sys.exit() # If user exits window, exit program

    ballrect = ballrect.move(speed) # Move the ball by the speed value once
    if ballrect.left < 0 or ballrect.right > width: # |- If ballrect object touches 
        speed[0] = -speed[0]                        # |- edges of screen,
    if ballrect.top < 0 or ballrect.bottom > height:# |- reverse speed value so 
        speed[1] = -speed[1]                        # |- it goes in opposite direction

    screen.fill(black) # Erase ball image, fill screen with black so it looks like a black background
    screen.blit(ball, ballrect) # Redraw ball image by copy/pasting the ball image onto the display SUrface
    pygame.display.flip() # Update everything
#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________