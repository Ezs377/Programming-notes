import pygame
pygame.init()

loop = 1 # For looping program
screen = pygame.display.set_mode((700,700)) # Set display Surface, with width and height tuple size
color = (5, 5, 5) # Color RGB tuple, represents a RGB color value
color_line = (255, 100, 100) # Color RGB tuple for line drawing
color_rect = (100, 255, 100) # Color RGB tuple for rectangle drawing
color_circ = (100, 100, 255) # Color RGB tuple for circle drawing
color_arc = (100, 100, 100) # COlor RGB tuple for circle drawing

# Fill screen display Surface
screen.fill(color)

# Draw a line on the screen (display Surface)
# pygame.draw.lines(display, color, closed, pointlist, thickness)
'''where display = display Surface,
color = color RGB tuple,
closed = true or false only (connect
start and end point of the line together),
pointlist = list of tuple coordinates for each point in line,
thickness = width of line in pixels'''
pygame.draw.lines(screen, color_line, False, [(100, 100), (10, 300), (500, 400)], 4)

# Draw a rectangle on the screen (display Surface)
# pygame.draw.rect(display, color, (x,y,width,height), thickness)
'''where display = display Surface,
color = RGB tuple,
(x,y,width,height) = tuple containing values, x,y stands for the coordiantes of the 
upper left corner of the rectangle, width,height stands for the dimensions of the rectangle,
thickness = thickness of rectangle borders in pixels. If zero, rectangle will be filled with color'''
pygame.draw.rect(screen, color_rect, (300, 300, 50, 70), 2)

# Draw a circle on the screen (display Surface)
# pygame.draw.circle(display, color, (x,y), radius, thickness)
'''where display = display Surface,
color = RGB tuple,
(x,y) = tuple with coordinates for the center of the circle,
radius = the length of the radius,
thickness = thickness of the circumference in pixels. If zero, circle is filled with color'''
pygame.draw.circle(screen, color_circ, (200, 40), 20, 5)

# Draw an arc on the screen (display Surface)
# pygame.draw.arc(display, color, (x,y,width,height), start_angle, stop_angle, thickness)
'''where display = display Surface,
color = RGB tuple,
(x,y,width,height) = tupel coordinates for a RECTANGLE that the arc would fit inside. If the width and height
are equal, then the arc would be part of a circle, as a circle fits perfectly in a square. Otherwise, the arc
would be part of an ellipse.
start_angle = starting angle of the arc in RADIANS, where 0 = right side of the circle
stop_angle = stopping angle of the arc in RADIANS, and travels anticlockwise from start point.
Start and stop angles are non-cumulative, meaning that they use exact coordinates to draw instead
of adding onto each other (i.e. (1, 1.2), instead of adding 1.2 radians onto the start point
which results in a coordinate of 2.2 radians, only a very small section of circle is drawn)
thickness = thickness of arc border in pixels'''
pygame.draw.arc(screen, color_arc, (500,400,100,100), 0, 3, 10) # Using square base
pygame.draw.arc(screen, color_arc, (200,450, 50, 150), 0, 5, 10) # Using rectangle base


while loop == 1: # Pygame loop
    
    for event in pygame.event.get(): # Refresh event queue (THIS IS NECESSARY TO PREVENT FREEZING)
        if event.type == pygame.QUIT:
            loop = 0
            
    pygame.display.update() # Call this for every edit to the screen (e.g. Animations)
    


print ("done")