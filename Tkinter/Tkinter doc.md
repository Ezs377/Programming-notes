# Tkinter module:  
Tkinter is a simple in-built module used by Python for creating Graphical User Interfaces (GUIs). It contains several classes and functions that can be imported to design GUIs with python. A master is required for every widget, this is usually the main frame that you setup at the start of the program. Widgets are typically features of a GUI that can be made, such as buttons or text. For Tkinter these are:  
- `Button`:  
  Creates a clickable button. Following options are:
  - `activebackground`: Set background colour when mouse is hovered over button
  - `activeforeground`: Set foreground color when mouse is hovered over the button
  - `bd`: Border width in pixels
  - `bg`: Set default background color
  - `command`: Set what happens if button is clicked (what code to run, usually a function)
  - `fg`: Set default foreground color
  - `font`: Set default font. Has 3 parameters: font, text size, and format
  - `height`: Height of the button in characters, or pixels if using an image
  - `highlight`: Set highlihgt color when button is pressed
  - `image`: Set image on the button instead of text. Imported by directory path
  - `justify`: Set the alignment of text if there are multiple lines
  - `padx`: Set the padding to the left and right of text
  - `pady`: Set the padding to above and below the text
  - `relief`: Set the type of button border
  - `state`: Set the state of the button. `DISABLED` renders the button inactive, `NORMAL` is the default state, `ACTIVE` is when the button is clicked
  - `underline`: Underlines the specified characters. Default is -1, any negative value will mean no underlined text
  - `width`: Set the width of the button in characters, or pixels if using an image
  - `wraplength`: Set the wrap length for text (the amount of characters in one line)  
  - The following methods can also be used:  
      - `flash()`: Flashes the button between active and normal colours
      - `invoke()`: Calls the button's callback function and returns what the function returns. Doesn't work if there is no callback.  
- `Canvas`
- `Checkbutton`
- `Entry`
- `Frame`
- `Label`:  
   Creates a singleline text that can be altered. Following options are:  
- `Listbox`
- `Menubutton`
- `Menu`
- `Message`:  
   Creates text that automatically wraps itseFf to multi-line if neccesary. Following options are:  
- `Radiobutton`
- `Scale`
- `Scrollbar`
- `Text`:  
   Creates an editable text box for the user, and can display text as well. Following options are:  
- `Toplevel`
- `Spinbox`
- `Panedwindow`
- `Labelframe`
- `tkMessagebox`

There are also several atrributes available which are used to manipulate these widgets  
- `Dimensions`
- `Colors`
- `Fonts`
- `Anchors`
- `Relief styles`
- `Bitmaps`
- `Cursors`

And finally, there are 3 different methods to position these widgets  
- `pack()`
- `grid()`
- `place()`

#### How to setup a GUI with tkinter module using classes:  
1. Import tkinter
2. Create a class
3. In the `def __init__` function, create 2 arguments, self and variable (any name), This variable will be used to import Tk() (tkinter) into the class
4. `variable = tkinter.Tk()`, followed by `<classname>(<variable name>)` will import tkinter into the class
5. `<variable name>.mainloop()` will keep looping the GUI program until it is closed. This ensures the GUI will stay open until the user closes it. This is basically running a forever `While` loop with `update()` within. `update()` refreshes your GUI and lets you interact with it. Mkae sure `mainloop()` is at the bottom of your program as any code under `mainloop()` will not be run until the GUI is closed, then the `mainloop()` breaks and runs the remaining code
6. `<variable name>.title=(<title name>)` lets you name your GUI window
7. Firstly, setup the frame. Then, widgets can be added as many as you like and moved around the GUI. This is the basics of a GUI
8. To use tkinter with the class, `<variable name>.<another variable> = tkinter.<widget()>` will create a widget for your GUI. Wdigets have many options that can be edited depending on the widget. Remember that Python is case-sensitive and some widgets have a capital letter, if not capitalised then program won't work.

#### Photoimage method:
Tkinter utilises a method called `Photoimage` to import images into a GUI. Tkinter has to convert an image to an object in Python in order to be able to display it. After using `Photoimage` the object can now be used in a widget such as `Label` or `Button`. In order to use the `Photoimage` method, firstly, allocate a variable to the method. Then, that variable can be used for any image parameter in a widget. For example:  
```Python  
import tkinter

class Imageimporting:
	def __init__ (self):
		self.importedimage = tkinter.Photoimage(file=d:/download/images/picture.png)
		text = tkinter.Label(self, image=self.importedimage)
root = Tk()
run = Imageimporting(root)
root.mainloop()
```  
An example of how to use `Photoimage`. Photoimage can only convert PNG, GIF, PGM, and PPM image formats. For other formats such as JPG, another module needs to be imported that can work with Tkinter to convert images.  

#### Layouts:  
Tkinter utilises 3 methods to arrange the layout of a GUI: `pack()`, `grid()`, and `place()`. 
- `pack()` utilises a geometric straight-forward layout, that arranges the elements of a GUI as blocks. THis usually means that elements in a GUI are always stretched to their limit, unless blocked by another element, or coded to a specific size. This type of layout is most suited for neat single rows/columns where you need everything to be aligned in a striaight line.
- `place()` utilises geometrical coordinates to place elements of a GUI. Unlike `grid()` and `pack()`, the elements on a GUI are manually set and don't resize themselves relative to the GUI window. You can set the element relative to other GUI elements, and set the exact coordinates using offsets. This is mostly suited when you want very specific palcements of GUI elements, whether for functionality or aesthetics.
- `grid()` utilises a table=like structure, where the elements of the GUI go. The amount of rows and columns of the 'table' is determined by the programmer, and elements simply fit inside cells in the 'table'. This is generally suited for general use, and can do most of the functions that `place()` and `pack()` can do.

With `padx` and `pady` for GUI elements, using these codes inside the element strcture will create the *inner* padding. For example, `self.heading = tkinter.Label(self.frame, padx=20, pady=10)` will create a Label that has a 20px padding between the text and the Label borders (since a Label is just a ractangle with text). However, placing the `padx` and `pady` inside the `grid()` geometry manager will cause a padding between GUI elements instead of the text and border, which is also why `grid()` is one of the most versatile geometry managers as it lets you deterimne the distance between GUI elements. 

The `grid_rowconfigure(index, weight)` and `rowconfigure(index, weight)` grid functions can be used to alter the size of the widgets should the whole frame (window) be resized. This allows the GUI to scale to the size of the window, so if the user decides to resize the window the GUI elements scale along with the frame instead of remaining static. `index` is the column/row number, and `weight` is the scale of the GUI element. By default, all GUI widgets start out with a weight of 0. Increasing the weight property means giving more priorty to the widget when it is scaled. For example, a Label with a weight of 3 will be bigger than a Label with a weight of 1, even though both will become bigger when the whole window is resized.
