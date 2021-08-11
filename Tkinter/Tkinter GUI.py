# Tkinter GUI guide


# 12 functions, so a 3*4 square of buttons
# Functions:
# Entry. Canvas, Checkbutton, Listbox, 
# Message, Radiobutton, Scale, Scrollbar,
# Text, Toplevel, Spinbox, Panedwindow

import tkinter

# Set up toplevel window
def Toplevel_frame(self):
        self.window = tkinter.Toplevel() # Create new window
        
        # Frame
        self.toplevel_frame = (self.window)
        self.toplevel_frame.grid()    

# main class
class Main:
        # Function for creating the buttons
        # label sets the title of the button, function sets the command of the button
        def button(self, label, function):
                return tkinter.Button(self.frame,
                               text = label,
                               width = 15,
                               height = 3,
                               command = function)  
        
        
        def __init__(self, x): # Main() calls the class, Main('four') means 'four' is used in the def init. Root is used to allow tkinter to be used

                background = "#f2f2f2" # Set background color variable. To change background color change this only

                '''Main frame'''
                self.frame = tkinter.Frame(x,
                                           pady=5,
                                           padx=10,
                                           bg = background) # Set the frame
                self.frame.grid() # Create grid

                '''Main page'''		
                # Create label text
                self.textlabel = tkinter.Label(self.frame,
                                               text = "Tkinter Widgets",
                                               bg = "#80c1ff",
                                               font= (("Century Schoolbook"), 40))

                # Set position of text at the top, in the center
                self.textlabel.grid(row=0,
                                    columnspan = 3,
                                    padx=0,
                                    pady=5,
                                    sticky=tkinter.E+tkinter.W)
                
                # Button labels
                buttons = ["Toplevel", "Canvas", "Checkbutton", "Listbox", "Message", "Radiobutton",
                             "Scale", "Scrollbar", "Text", "Entry", "Spinbox", "PanedWindow"]
                
                # Classes to call
                functions = [Toplevel, Canvas, Checkbutton, Listbox, Message, Radiobutton, Scale,
                             Scrollbar, Text, Entry, Spinbox, Panedwindow]
                
                # Variable counters
                function_no = 0
                row_no = 1
                column_no = 0
                
                '''Buttons for menu'''
                for a in buttons:
                        
                        # Button creation function
                        self.some_button = self.button(a, functions[function_no])
                        
                        # If all functions have been used
                        if function_no < (len(functions)-1):
                                function_no += 1
                        else:
                                function_no = 0
                        
                        # Grid placement for each button
                        self.some_button.grid(row=row_no,
                                              column=column_no,
                                              pady = 0,
                                              sticky = tkinter.W+tkinter.E) # Occupy all space in grid cell
                        
                        # Change column and row values when needed
                        column_no += 1
                        if column_no == 3:
                                row_no += 1
                                column_no = 0
                        
                


class Toplevel:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                '''A Toplevel window allows multiple windows to be made from the main window'''
                self.text1 = tkinter.Label(self.window,
                                           text = "This is a toplevel window")
                self.text1.grid(row=0,
                                columnspan = 1)
                
                # Exit button
                self.exit1 = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit1.grid(row=1,
                                columnspan = 1)

class Canvas:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text2 = tkinter.Label(self.window,
                                           text = "These are canvases, each with a different method")
                self.text2.grid(row=0,
                                columnspan = 3)
                
                '''A Canvas allows drawing graphics and inserting images'''
                # First canvas
                self.canvas = tkinter.Canvas(self.window,
                                             height = 100,
                                             width = 100)
                self.canvas.grid(row=1,
                                 column=0)
                '''(0, 0) coordinates start from TOP LEFT for drawing stuff'''
                
                # Create a line.
                # Fill: fill colour | width = line width | 
                self.canvas.create_line(0,0,100,100, fill='red', width=5)
                
                
                # Second canvas
                self.canvas2 = tkinter.Canvas(self.window,
                                              height=100,
                                              width=100)
                self.canvas2.grid(row=1,
                                 column=1)                
                
                # Create rectangle. The first 2 coordinates mark origin point, the TOP LEFT corner of rectangle
                # Third and fourth values determine coordinates of BOTTOM RIGHT corner
                # Third coordiante determines height, fourth coordinate determines width
                self.canvas2.create_rectangle(10,10, 90, 90)
                
                
                # Third canvas
                self.canvas3 = tkinter.Canvas(self.window,
                                              height=100,
                                              width=100)
                self.canvas3.grid(row=1,
                                 column=2)
                
                # Create oval. Same rules as rectangle
                self.canvas3.create_oval(10,10, 90, 90)
                
                
                # Fourth canvas
                self.canvas4 = tkinter.Canvas(self.window,
                                              height=100,
                                              width=100)    
                self.canvas4.grid(row=2,
                                 column=0)                
                
                # Create polygon. Same rules as previous shapes, but as many more coordinates can be added for each side, as long as it is a even number
                # Each pair of coordinates determines a point of the polygon
                self.canvas4.create_polygon (10, 90, 50, 10, 90, 90, fill = 'blue')
                
                
                # Fifth canvas
                self.canvas5 = tkinter.Canvas(self.window,
                                              height=100,
                                              width=100)    
                self.canvas5.grid(row=2,
                                 column=1) 
                
                # Create an arc. Uses the coordinate system of an oval, but has 2 extra parameters: start and extent
                # start determines the starting point of the curve, 0 degrees = 3 o'clock position
                # extent determines how far the curve goes, in degrees
                # style determines the type of curve drawn: pieslice (default), arc (circumference only), chord (connects the start and endpoint together with a line)
                self.canvas5.create_arc (10, 10, 90, 90, start=40, extent = 240, style = "pieslice")
                
                
                # Sixth canvas
                self.canvas6 = tkinter.Canvas(self.window,
                                              height=100,
                                              width=100)
                self.canvas6.grid(row=2,
                                 column=2)                 
                # Import image, convert it into an object, and display it in the canvas.
                # Coordinates represent the position of the center of the image
                # To resize image use PIL module
                self.picture = tkinter.PhotoImage(file = "BLM image.png")
                self.canvas6.create_image (50, 50, image=self.picture)
                
                '''Text and widgets can also be inserted into a canvas'''
                '''To delete items, use delete(). Use coords() to move items, or use move() to move items based 
                on their current position. lift() and lower() allow manipulation of item layers.'''
                                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=3,
                                columnspan = 3)                
        
class Checkbutton:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text3 = tkinter.Label(self.window,
                                           pady=10,
                                           padx=10,
                                           text="These are checkbuttons")
                self.text3.grid(row=0,
                                columnspan=2)
                
                '''A Checkbutton allows the user to tick boxes'''
                self.checkbutton1 = tkinter.Checkbutton(self.window,
                                                        pady=10,
                                                        padx=10,
                                                        text="Option 1")
                self.checkbutton1.grid (row=1,
                                        columnspan=2)
                
                self.checkbutton2 = tkinter.Checkbutton(self.window,
                                                        pady=10,
                                                        padx=10,
                                                        text="Option 2")
                
                self.checkbutton2.grid (row=2,
                                        columnspan=2)    
                
                self.checkbutton3 = tkinter.Checkbutton(self.window,
                                                        pady=10,
                                                        padx=10,
                                                        text="Option 3")  
                self.checkbutton3.grid (row=3,
                                        columnspan=2)
                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=4,
                                columnspan = 2)

class Listbox:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text4 = tkinter.Label(self.window,
                                           pady=10,
                                           padx=10,
                                           text="This is a listbox")
                self.text4.grid(row=0,
                                columnspan=2)             
                
                '''A listbox puts information into a list format'''
                self.listbox = tkinter.Listbox(self.window)
                self.listbox.insert(1, "Option 1")
                self.listbox.insert(2, "Option 2")
                self.listbox.insert(3, "Option 3")
                self.listbox.insert(4, "Option 4")
                self.listbox.insert(5, "Option 5")
                self.listbox.insert(6, "Option 6")
                
                self.listbox.grid(row=1,
                                  columnspan=2)
                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=2,
                                columnspan = 2)                
                
                
class Message:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text5 = tkinter.Label(self.window,
                                           text="This is a message",
                                           padx=10,
                                           pady=10)
                self.text5.grid(row=0,
                                columnspan=2)
                
                '''A message displays text that automatically wraps itself based on the window size.
                This is different from Label text, which only displays text in one line unless
                told to wrap length'''
                self.text_var = tkinter.StringVar()
                self.text_var.set ("Message is here!")
                
                self.message = tkinter.Message(self.window,
                                               textvariable=self.text_var,
                                               padx=10,
                                               pady=10,
                                               relief=tkinter.RAISED)
                self.message.grid (row=1,
                                   columnspan=2)
                
               
               
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=2,
                                columnspan = 2)                 

class Radiobutton:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text6 = tkinter.Label(self.window,
                                           text="These are radiobuttons",
                                           pady=10,
                                           padx=10)
                self.text6.grid(row=0,
                                columnspan=2)
                
                '''A radiobutton lets the user pick one option out of several'''
                control = tkinter.IntVar()
                
                self.radiobutton = tkinter.Radiobutton(self.window,
                                                       text="Option 1",
                                                       pady=10,
                                                       padx=10,
                                                       value=1,
                                                       variable=control)
                self.radiobutton.grid(row=1,
                                      column=0)
                
                self.radiobutton2 = tkinter.Radiobutton(self.window,
                                                       text="Option 2",
                                                       pady=10,
                                                       padx=10,
                                                       value=2,
                                                       variable=control)
                self.radiobutton2.grid(row=1,
                                      column=1)
                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=2,
                                columnspan = 2)                   


class Scale:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame (self)
                
                # Title
                self.text7 = tkinter.Label(self.window,
                                           text="This is a scale",
                                           pady=10,
                                           padx=10)
                self.text7.grid(row=0,
                                columnspan=2)
                
                '''A scale is an adjustable set of values by the user'''
                counter = tkinter.IntVar()
                
                self.scale = tkinter.Scale(self.window,
                                           variable = counter)
                self.scale.grid(row=1,
                                columnspan=2)
                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=2,
                                columnspan = 2)                   




class Scrollbar:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text8 = tkinter.Label(self.window,
                                           text = "This is a scrollbar",
                                           pady=10,
                                           padx=10)
                self.text8.grid(row=0,
                                columnspan=2)
                
                '''A scrollbar allows the scrolling of certain widgets'''
                # Create scrollbar
                self.scrollbar = tkinter.Scrollbar(self.window)
                self.scrollbar.grid(row=1, column=2, sticky=tkinter.N+tkinter.S) # Bind scrollbar to right side, from north to south
                
                # Create a list, and set the Y movement to a scrollbar
                self.mylist = tkinter.Listbox(self.window, yscrollcommand = self.scrollbar.set )
                
                # Add items into the listbox
                no = 0
                for line in range(100):
                        self.mylist.insert(no, "This is line number " + str(line))     
                        no += 1
                
                
                self.mylist.grid(row=1,
                                 column=0)
                
                # Set the command of the scrollbar so that when it moves, change the Y view of the Listbox
                '''The config is neccesary as trying to set a command to the Listbox before it is created creates error,
                and setting the Scrollbar after the Listbox means setting the yscroll command of the Listbox to a non-existent 
                Scrollbar creating another error'''
                self.scrollbar.config (command=self.mylist.yview)
                
                # Exit button
                self.exit = tkinter.Button(self.window,
                                            text = "Exit",
                                            command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit.grid(row=2,
                                columnspan = 2)                   
        


class Text:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text9 = tkinter.Label(self.window,
                                          text="This is a text",
                                          pady=10,
                                          padx=10)
                self.text9.grid(row=0, columnspan=2)
                
                ''' A Text displays text that can be easily configured and edited, as well as 
                allowing user input text'''
                self.TextW = tkinter.Text(self.window)
                
                self.TextW.insert(tkinter.INSERT, "Type ")
                self.TextW.insert(tkinter.END, "something!")
                self.TextW.insert(tkinter.INSERT, " Another insert!")
                self.TextW.grid(row=1,
                           columnspan=2)
                
                # Exit button
                self.exit1 = tkinter.Button(self.window,
                                           text = "Exit",
                                           command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit1.grid(row=2,
                                columnspan = 2)                
class Entry:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text10 = tkinter.Label(self.window,
                                            text="This is an entrybox",
                                            pady=10,
                                            padx=10)
                self.text10.grid(row=0,
                                 columnspan=2)
                
                '''An entrybox allows users to input text which can be retrieved by Python later'''
                self.entry = tkinter.Entry(self.window)
                
                self.entry.grid(row=1,
                                columnspan=2)
                
                # Label that shows entrybox results
                self.notif = tkinter.Label(self.window,
                                           text="Type something and press enter",
                                           pady=10,
                                           padx=10)
                
                self.notif.grid(row=2,
                                columnspan=2)
                
                # Binding
                self.window.bind("<Return>", self.entryget)
                
        
                # Exit button
                self.exit1 = tkinter.Button(self.window,
                                           text = "Exit",
                                           command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit1.grid(row=3,
                                columnspan = 2)
        
        # Get value from entrybox and use it
        def entryget(self, x):
                value = self.entry.get()
                self.notif.configure (text=value)

class Spinbox:
        def __init__(self):
                # Setup toplevel frame
                Toplevel_frame(self)
                
                # Title
                self.text11 = tkinter.Label(self.window,
                                            text="This is a spinbox",
                                            pady=10,
                                            padx=10)
                self.text11.grid(row=0, columnspan=2)
                
                '''A Spinbox lets the user pick a value from a range of values'''
                self.spinbox = tkinter.Spinbox(self.window,
                                               from_=0,
                                               to=100)
                
                self.spinbox.grid(row=1,
                                  columnspan=2)
                
                
                # Exit button
                self.exit1 = tkinter.Button(self.window,
                                           text = "Exit",
                                           command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit1.grid(row=2,
                                columnspan = 2)                
class Panedwindow:
        def __init__(self):
                # Setup frame
                Toplevel_frame(self)
                
                # Title
                self.text12 = tkinter.Label(self.window,
                                            text="This is a PanedWindow",
                                            padx=10,
                                            pady=10)
                self.text12.grid(row=0, columnspan=2)
                
                
                # PanedWindow bar
                self.panedwindow = tkinter.PanedWindow(self.window,
                                                       bg="red",
                                                       showhandle=True,
                                                       orient=tkinter.HORIZONTAL)
                self.panedwindow.grid(row=1)
                
                # Adding widgets
                self.left = tkinter.Label(self.panedwindow,
                                          text="On the left pane, horizontal shift",
                                          padx=10,
                                          pady=10)
                self.panedwindow.add(self.left)
                
                self.right = tkinter.Label(self.panedwindow,
                                        text="On the right pane",
                                        padx=10,
                                        pady=10)
                self.panedwindow.add(self.right)
                
                
                # Second PanedWindow
                self.panedwindow2 = tkinter.PanedWindow(self.window,
                                                        bg="green",
                                                        showhandle=True,
                                                        orient=tkinter.VERTICAL)
                self.panedwindow2.grid(row=2)
                
                # Adding widgets
                self.top = tkinter.Label(self.panedwindow2,
                                        text="On the top pane, vertical shift",
                                        padx=10,
                                        pady=10)
                self.panedwindow2.add(self.top)
                
                self.bottom = tkinter.Label(self.panedwindow2,
                                        text="On the right pane",
                                        padx=10,
                                        pady=10)
                self.panedwindow2.add(self.bottom)                
                
                
                
                # Exit button
                self.exit1 = tkinter.Button(self.window,
                                           text = "Exit",
                                           command = lambda:self.window.destroy()) # Destroy toplevel window
                self.exit1.grid(row=3,
                                columnspan = 2)
        

# Run the program loop
root = tkinter.Tk()
root.title ("Tkinter Widgets Guide")
run = Main(root)
root.mainloop()

'''Format of each function:
def__init__(self):
     Toplevel_frame(self)
     self.text = tkinter.Label(self.window, <name of function>)
     self.text.grid(row=0, columnspan=2)
     
     
     <function code goes here, use self.window for master>
     
     
     self.exit1 = tkinter.Button(self.window,
                                text = "Exit",
                                command = lambda:self.window.destroy()) # Destroy toplevel window
     self.exit1.grid(row=1,
                     columnspan = 1)'''