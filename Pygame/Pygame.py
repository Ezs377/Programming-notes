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
#'''Animation'''

#import pygame
#pygame.init()

#loop = 1 # For looping program
#screen = pygame.display.set_mode((600,600)) # Set display Surface, with width and height tuple size
#color = (5, 5, 5) # Color RGB tuple, represents a RGB color value
#rect_color = (250, 100, 255)

## Set a variable to the clock of Pygame
#clock = pygame.time.Clock() 

## Fill screen display Surface
#screen.fill(color)

## Set movement points
#points = [(150,150, 50, 50), (450, 150, 50, 50), (450, 450, 50, 50), (150, 450, 50, 50)]

#pointnum = 0

#while loop == 1: # Pygame loop
    
    #'''Using the ingame clock'''
    #clock.tick(10) # FPS
    
    #'''Using a time delay'''
    ##pygame.time.delay(1000)   
    
    ##print (pygame.time.get_ticks()) # Total runtime in millisceconds
    ##print (clock.get_time()) # Time in milliseconds from previous tick to the next
    ##print (clock.get_fps()) # Current FPS
    
    #for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        #if event.type == pygame.QUIT:
            #loop = 0
            
    #screen.fill(color)
    
    #pygame.draw.rect(screen, rect_color, (points[pointnum]), 0)
    
    #pointnum += 1
    #if pointnum == 4:
        #pointnum = 0
    
    
    #pygame.display.update() # Call this for every edit to the screen (e.g. Animations)
    


#print ("done")
#__________________________________________________________________________________________________________________________
'''Moving animation!'''
import pygame, sys
pygame.init()

loop = 1 # Instead of using sys.exit, use variable
screen = pygame.display.set_mode((600, 600)) # Set display size
color = (0, 0, 0) # Color RGB tuple
rect_color = (255, 100, 100) # Color RGB tuple 2
clock = pygame.time.Clock() # Create clock object
screen.fill(color) # Fill display color
counter = 0 # Counter value for coordinates
increment = 10 # Value for setting the movement value of square

# List of coordinates to get square to move to
pointlist = [(100, 100), (450, 100), (450, 450), (100, 450)]

# Set x and y coordinates
x = pointlist [counter][0]
y = pointlist [counter][1]

# Set coordinates
coordinates = (x, y)

# Size of square
size = (50, 50)

# While loop is still going i.e. program is still running
while loop == 1:
    # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If Pygame detects program shutdown
            loop = 0
    
    # Set FPS
    clock.tick(30)
    
    # Refresh screen
    screen.fill(color)
    
    # Grid lines
    pygame.draw.lines(screen, (100, 255, 100), False, [(100, 0), (100, 600)], 1) # Left vertical
    pygame.draw.lines(screen, (100, 255, 100), False, [(500, 0), (500, 600)], 1) # Right vertical
    pygame.draw.lines(screen, (100, 255, 100), False, [(0, 100), (600, 100)], 1) # Upper horizontal
    pygame.draw.lines(screen, (100, 255, 100), False, [(0, 500), (600, 500)], 1) # Lower horizontal
    
    
    # Code for coordinates seeking
    if x < pointlist[counter+1][0]: # if x is less than the desired coordinate, add x
        x += increment
    elif x > pointlist[counter+1][0]: # if x is more than desired coordinate, subtract x
        x -= increment
    
    # Same formula used for y
    if y < pointlist[counter+1][1]:
        y += increment
    if y > pointlist[counter+1][1]:
        y -= increment


    # If the cooridnates match the target coordinates, move to the enxt coordinate
    if coordinates == pointlist[counter+1]:
        counter += 1
    

    if counter == 3:
        counter = -1
    
    # Set coordinates of square
    coordinates = (x, y)

    # Draw square
    pygame.draw.rect(screen, rect_color, (coordinates, size), 0)
    
    # Update screen
    pygame.display.update()

print ("done") # Indicate finish
#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________

#__________________________________________________________________________________________________________________________