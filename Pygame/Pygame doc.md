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

A display is considered a Surface object by Python. Any images are also considered Surface objects. Drawings are drawn on the `display` Surface.  

`pygame.image.load` lets us load an image into Python as a Surface object. This works by keeping the pixel colour values of the image data. This function supports various image file formats including JPG, PNG, GIF, etc.  

Blit (short for block transfer) is a method of copy-pasting an image object to a Surface. This is often used to create animation for moving objects in a Surface.  

Double buffering is a common technique used in Pygame to render everything in a single frame instead of one by one. The way Pygame works is that computing objects and displaying them on screen are two different processes. Without double buffering, your program would be trying to compute the changes to an image while also trying to display it, resulting in screen flickering and most of your images not appearing. An example of this is making a black background with a moving image of a ball. Python will try to render the moving ball while also drawing the background, resulting in either the ball only displaying or the background only. By double buffering, Python computes everything before displaying them on screen. This ensures that everything is rendered before being displayed in a single frame, reducing flickering or stutters. To update the screen, Pygame uses the `pygame.display.update()`function. This updates every Surface object in the display. If you want to only update specific areas of the display, adding object variables  in the brackets will only update those Surface objects. An alternative function is the `pygame.display.flip()` function, which updates every Surface. But leaving `pygame.display.update()` blank does the same thing anyway. 


### Events:  


