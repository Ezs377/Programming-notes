# Pygame module

Pygame is a module created for Python to generate a game with Python programming. Pygame wraps the SDL library (Simple Directmedia Layer) as a Python extension. SDL is a cross-platform development library that manages external devices and events for software. It is primarily used to develop games but has its uses for other projects as well. SDL is written in C, so the purpose of Pygame is to allow Python to be able to use SDL libraries withut having to program in C (you can still use SDL as long as you are familiar with any of the C langauges).  

`pygame.init()` initializes Pygame and allows the pygame module to run within the program. There are several modules available within Pygame:
- `cdrom`: Lets you access the CD and DVD drives of a computer to load things, such as audio recordings and etc. Outdated  
- `cursors`: Lets you use and display cursors in your program for any purpose, such as menu selection  
- `display`: Lets you create a display (screen) for your game. Called a 'surface' by Pygame, this is where you display your game to the user  
- `draw`: Lets you 'draw' shapes onto a surface (display)  
- `event`: Lets you manage events and the event queue    
- `font`: Lets you create and render custom TrueType fonts for your program  
- `image`: Lets you save and load images  
- `joystick`: Lets you use a joystick in your game  
- `key`: Lets you bind events to keyboard buttons and perform other functions with the keyboard  
- `mouse`: Lets you bind events to the mouse movement and state and perform other mouse functions  
- `sndarray`: Use the NumPy module to convert Sound objects with a NumPy array. Allows manipulation of sound values and functions to manipulate sound  
- `surfarray`: Use the NumPy module to convert pixels to a NumPy array. Allows manipulation of image pixels and colours.  
- `time`: Lets you handle program timings in milliseconds  
- `transform`: Lets you manipulate images and sprites on the display. Note that some data can be lost if an image is resized over and over, resulting in a more blurry image  

### Initializing:  
1. Import pygame. This can be done by simply writing `import pygame` in python. Note that Pygame has to be installed in order to use it, you can install it using pip and command prompt. If the `import` command doesn't run in your python window, then Pygame probably isn't installed.  
2. Use `pygame.init()` to initialize Pygame functions and modules. This ensures everything is up and running for Pygame. If an error occurs that means either that function/module is uninitialized, or not installed, which measn you need to re-install Pygame. Using `pygame.get_init` will return either True or False, and determines if Pygame is fully initialized or not.  
3. A display is initialized when `pygame.init()`is called. However, if it isn't, use `pygame.display.init()` to initialize a display. A display is referred to as a Surface by Pygame.  

### Display:  
Using `pygame.display.set_mode(coordinates)` lets you set the size of the display, where `coordinates` is equal to a tuple with two integer values, a width and height. For example, `size = 340, 520` creates a tuple called `size` which has the values `(340, 520)`. This is used in the `coordinates` bracket to tell Python what size to set hte display. In this case, 340 pixels wide and 520 pixels tall. A display sets the coordinates of (0,0) at the **top left** of the screen. So X=0 and Y=0 when at the top left of the display, like a tkinter canvas. Only one display be opened by Pygame at a time.  

A display is considered a Surface object by Python. Any images are also considered Surface objects. Drawings are drawn on the `display` Surface. which is the main display that you initialized with `pygame.display.set_mode(coordinates)`.

**Double buffering** is a common technique used in Pygame to render everything in a single frame instead of one by one. The way Pygame works is that computing objects and displaying them on screen are two different processes. Without double buffering, your program would be trying to compute the changes to an image while also trying to display it, resulting in screen flickering and most of your images not appearing. An example of this is making a black background with a moving image of a ball. Python will try to render the moving ball while also drawing the background, resulting in either the ball only displaying or the background only. By double buffering, Python computes everything before displaying them on screen. This ensures that everything is rendered before being displayed in a single frame, reducing flickering or stutters. To update the screen, Pygame uses the `pygame.display.update()`function. This updates every Surface object in the display. If you want to only update specific areas of the display, adding object variables  in the brackets will only update those Surface objects. An alternative function is the `pygame.display.flip()` function, which updates every Surface. But leaving `pygame.display.update()` blank does the same thing anyway.

### Images:  
`pygame.image.load(<image URL>)` lets us load an image into Python as a Surface object. This works by keeping the pixel colour values of the image data. This function supports various image file formats including JPG, PNG, GIF, etc. `<image URL>` stands for the image name, and if necessary, the path to the image if the image is not in the same folder as the program. 

Blit (short for block transfer) is a method of copy-pasting an image object to a Surface. This is often used to create animation for moving objects in a Surface. It is often preferably to use the `.convert()` method after the `pygame.image.load()` function, like this: `pygame.image.load(Ball.jpg).convert()`. Using the `convert()` function basicallt onverts the image into the same data type of the display Surface, so when using blitting the program uses less memory to blit an image.

An image can be considered a Surface object, as a Surface is basically a graphical 'surface' of the screen. Like the different layers in digital art, each surface provides the user a graphical representation of the game. The main difference between an image and a sprite is that 

### Drawing:  
Pygame can also draw shapes onto the display Surface instead of importing images in. Pygame uses similar methods of drawing with Tkinter canvas, except it is more specific and more variability than Tkinter canvas. Pygame also uses tuples for a lot of values, such as coordinates. Often, a tuple is generated by allocating two values to a single variable, like `coordinates = 12, 55`. This creates a tuple of `(12, 55)`, which is used by Pygame for ccoordinates, where `X` is the first value, and `Y` is the second value. Tuples can also be generated with any number of values, like making a tuple with 3 values to create an RGB value for color. Please note that any of these parameters can be simplified into a variable first and then inputted into the function.

**Lines:**  
`pygame.draw.lines(screen, color, closed, pointlist, thickness`. Following parameters are:
- `screen` = The display Surface variable (where you initialized the main display). 
- `color` = A RGB value that consists of 3 integers in a tuple (e.g. Like `(255, 120, 33)`. 
- `closed` = Whether to connect the end point with the start point (making a closed shape). Acccepts only True or False.  
- `pointlist` = A list containing tuple coordinates, such as `(12, 50)`. Thereotically an infitnite number of coordinates could be inputted here, as long as you can fit it in one list. An example of a `pointlist` paramter would be: `coordinates = [(23, 11), (54, 100), (220, 19), (150, 300)]`.  
- `thickness` = The thickness of the line in pixels.

**Rectangles:**  
`pygame.draw.rect(screen, color, (x,y,width,height), thickness)`. Following parameters are: 
- `screen` = The display Surface variable (where you initialized the main display).
-  `color` = A tuple containing an 3-integer RGB value.
-  `(x, y, width, height)` = A tuple cotaining coordinates and dimensions of the rectangle. `x` and `y` represent the coordinates of the TOP LEFT CORNER of the rectangle. `width` and `height` represent the width and height of the rectangle, in pixels. This can all be decided before calling the draw function (e.g. `rectangle = 300, 150, 40, 60`, then `reactangle` can simply be put in as the parameter for rectangle dimensions instead of `(300, 150, 40, 60)`).
-  `thickness` = The thickness of the border line of the rectangle. If zero is used, then the rectangle is filled with the same color instead.

**Circles:**  
`pygame.draw.circle(screen, color, (x,y), radius, thickness)`. Following parameters are:  
- `screen` = The display Surface variable (where you initialized the main display). 
- `color` = A RGB value that consists of 3 integers in a tuple (e.g. Like `(255, 120, 33)`.
- `(x, y)` = A tuple value that gives coordinates for the CENTRE of the circle. `x` is x position, `y` is y position. Remember that coordinates are based off the TOP LEFT corner of the display screen (i.e. (0,0) = top left corner).
- `radius` = The length of the radius in the same unit as coordinates.
- `thickness` = The thiccness of the circle border (i.e. the circumference). If left as zero, then the circle will be filled with the same color instead.

**Arcs:**  
`pygame.draw.arc(screen, color, (x, y, width, height), start_angle, stop_angle, thickness)`. Following parameters are:  
- `screen` = The display Surface variable (where you initialized the main display). 
- `color` = A RGB value that consists of 3 integers in a tuple (e.g. Like `(255, 120, 33)`.
- `(x, y, width, height)` = Coordinates and dimensions for the RECTANGLE that the arc will fit inside. If the rectangle is a perfect square (i.e. width = height) then the arc will be part of a perfect circle instead of an ellipse). The rectangle will not appear on the display, it is only used to map out the arc dimensions.
- `start_angle` = The starting angle point for the arc. By default, 0 is the right side of an ellipse, i.e. the direction of East, and rotates positive anti-clockwise. MEASURES IN RADIANS (e.g. To start from the top of the ellipse (north), `start_angle` = π/2)
- `stop_angle` = The ending angle point of the arc. Measured in radians as well, and follows same rules as `start_angle`.
- `Thickness` = Thickness of the arc in pixels.

**Animations:**  
When moving a drawing from one position to another, usually the whole screen is cleared by filling it with the same colour as the background, then re-drawing the drawings with different coordinates. Since the `pygame.display.update()` employs double buffering, that means that the changes to the display are applied at the saem time, so it appears as the drawing has moved. This is a common method of animation with Pygame, and is the most reliable. If the screen wasn't cleared before redrawing the drawing, then the previous drawing would remain, so there would be 2 drawings on the display, instead of a moving drawing.

**Setting the framerate:**  
An in-game clock can be modified to set the delay between screen updates, thus appearing to 'slow down' the speed that the drawings are drawn. There are two main ways to use this in Pygame: Using a time delay, or using the in-game clock. 
- `pygame.time.delay(milliseconds)`: Set the delay between each frame, where `milliseconds` = the delay in milliseconds. Inserted into the `while` loop of a Pygame update loop. E.g. `pygame.time.delay(100)` sets a time delay of 100 milliseconds between frames, which is also 10 frames per second.
- `<variable name> = pygame.time.Clock()` followed by `<variable name?.tick(FPS)`: Set the amount of frames per second, where `<variable name>` = you usual variable, FPS = Frames per second. `<variable name> = pygame.time.Clock()` is inserted outside the display update loop, while `<variable name?.tick(FPS)` is inserted inside the display update loop. For example:  
```Python
import pygame, sys
ingameclock = pygame.time.Clock()
color = (255, 255, 100)

while True:
  for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
  screen.fill(color)
  
  ingameclock.tick(30)
 ```  
In this program, the framerate has been set to 30 FPS by using the in-game clock (this program doesn't do anything however, it will just color in the display). The `ingameclock.tick(FPS)` function simply forces a maximum amount of frames per second; thus, it also sets the maximmum amount of times the loop repeats itself in a second. It will enforce a delay to ensure that the framerate never exceeds the given FPS, HOWEVER it does not mean that your program will go faster, just that it will stay under the given FPS.

It is often preferable to use the clock over a time delay, as the time delay requires you to calculate the delay between frames to achieve a certain framerate, while `Clock` creates an object that manages time and framerate for you. By using `Clock` you are also able to debug the tick values and frame data. The following functions let you extract debug data.
- `pygame.time.get_ticks())`: The only debug data you can extract if you use a time delay, but can also be used if you use the `Clock` object. This will give you the total runtime of the program in milliseconds. Useful for finding out if your program is lagging or not. E.g.  
![Screenshot](https://github.com/Ezs377/Programming-notes/blob/main/Images/Pygame%20runtime%20example.jpg).  
Using the debug data we can see that the program takes 2280 milliseconds to start the Pygame loop, which could be useful when trying to optimize perfomance in a program.
- `clock.get_time()`: Where `clock` = `pygame.time.Clock()`, this will give the time in milliseconds from one tick to the next. A 'tick' is basically the next update loop. This function needs a Clock object, so it can't be used if you use a time delay instead of the in-game clock. This is useful for finding the time between frames, so if lag occurs you can see where the time between frames has spiked. 
- `clock.get_fps()`: Where `clock` = `pygame.time.Clock()`, this also requires a Clock object. Gives the current Frames Per Second of the current loop, can also be used to see when your program slows down.


### Events:  


