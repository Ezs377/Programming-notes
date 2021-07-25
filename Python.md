# Python
### Generally useful info:  
Boolean expressions (eg. `If`, `While`, `And`) can take in a `True` or `False` value, which determines if the expression is initiated or not. Aside from `True` and `False`, other characters can be used as replacements. `True` and `False` are constants, and will always mean yes or no by Python.

* Characters that are considered `True` are:
  - Integers that are not zero
  - Lists, dictionaries, arrays that aren’t empty
  - Strings that aren’t blank
  - The string `True`

* Characters that are considered `False` are:
  - Zero as an integer
  - Empty lists, dictionaries, arrays
  - Strings that are blank ( “ “ )
  - The string `False`, ‘None’

This also lets variables be used directly for boolean expressions as variables can be any of these characters, allowing them to be used directly without any operator.  
Eg. Instead of using `If x != 0:` it is possible to instead use `If x:` as if `x` is not zero, then it must be `True`, considering that non zero integers are considered `True`. To reverse the expression use a `not` operator, which basically returns the opposite of the state of the character.  
Eg. `If x:` will return a `True` statement if `x` is not zero, and execute the program. However, if we want the program to not run when `x` is not zero, we can use `if not x:` instead, as if `x` is not zero, then it will return a `True` statement, which is reversed by the `not` operator, rendering it `False` (`not True` = `False`). So the program reads the statement as `False` and will not execute it.

### Technical Python terms:
An argument is a value that goes into brackets in a function/method. E.g. `writefunction(x, y)` means that a function called `writefunction` can take 2 arguments, `x` and `y`. An argument can be thought of as an input to a function. Python contains a lot of in-built functions and methods, such as `len(x)` which is a function that counts the amount of items in `x` (a data structure) and returns an integer value that is the full count of items within `x`. `x` is an argument for `len(x)`. Usually if you put a list in the brackets, that list is an argument for the function, and printing `len(list)` will give you a number that tells you the amount of items in the list. Some functions/methods don’t have arguments, such as `upper()`, which converts a string into all uppercase without an argument. When a function/method needs an argument, make sure that there is a valid argument in the brackets before running code otherwise error. However, some arguments are optional, and won’t become an error if they are not filled in the brackets. It depends on what you want your code to do.

A statement is a block of code that lets you run a set of code separately to the main program. `If`, `While`, and `For` loops are examples of statements. Basically, anything that is indented in the program is considered part of a statement. When running a statement, the program will usually read what kind of statement it is (e.g. A `While` loop), and proceed to run the indented code under the statement according to the statement. For example, the statement while `x >= 5:`  will cause the program to pause the whole program, and run any code that is part of the statement, while running the `While` loop until the conditions are met (which is, `x` is higher or equal to the number 5). A bigger example of a statement:

```Python
For a in [5, 2, 1]:
	print (a)
	number = a+1
	print (number)
print (‘done’)
```

In this example, the statement is the `For` loop, which causes the program to run a specific set of code until it stops looping, ignoring the rest of the code until the statement is finished. The program will not print ‘done’ until `For` loop is finished (the statement is done)(i.e. The program will not run anything that is after the `For` loop until the `For` loop is finished looping). 
A statement doesn’t have to be a loop, it is anything that allows the program to run a specific set of code within the program (such as `If` statements). There are many different types of statements. `For` is an example of a looping statement, while `If` is an example of a conditional statement.

A sequence/iteration is a repeated procedure that will repeat the same thing until it is told to stop. An example would be using a loop.

### File writing:
First, a variable needs to be allocated to the text file. Use `<variable1> = open(<filename>, <option>)`. Options include `r`, `w`, `a`, `x`.
`r` is for file reading only, cannot write to the file. `w` is write and read, can write to a file. `a` is used to add to a file without erasing its contents. `x` is used to create a new file. 
Once a variable is allocated to a text file via one of the modes, another variable has to be used if you want to read the file. 

**!!! Using `w`mode on a file completely deletes its contents !!!**  
You can also use `w` mode to create a new textfile in the program folder, but this also means that if you mistype the text filename then the program will create a new file instead of reading the text file

For example: `<variable2> = <variable1>.read()`
Then to edit text use `<variable2>`. The `<variable1>` is only used to take out the contents of a text file so Python can receive it. 

### Data structures/sequence:
A data structure is a form of storage used by a program that can store several data in several forms (this is also called a sequence in Python). Python has 4 in-built data structures: Lists, dictionaries, sets, and tuples. Data structures become very important for complex programming, as there are multiple ways you can write a program to call data from a data structure, and the method used can impact your program in many different ways. Variables are NOT data structures, they can be used to hold a data structure, but variables are only a name for a set of code. They exist to make life easier for programmers by becoming a temporary storage for something else that would otherwise take up more space in the program, such as a line of code.
- **Lists:** A list is an array of values that can be modified. Elements are used to refer to the position of a value. Lists can hold any type of data, and can add or remove elements as needed. An example of a list is `Car_info = [“cars”, 5, “colors”, “yellow”]`  
- **Dictionaries:** A dictionary contains key-value pairs as items within the dictionary. Each key is associated with its own value. An item is a key-value pair within a dictionary. Calling a key will allocate its value to the variable. For example, `<variable> = <dictionary>[<key>]` will allocate the value of the `<key>` to the variable. Items in a dictionary can be any data type, remember to use apostrophes/speech marks to indicate strings. Dictionaries cannot have duplicate keys. You cannot have two of the same key, such as having the keys `"home:here”` and `“home:there”`, but you can have two different keys with the same value, such as the keys `“time:60”` and `“days:60”`. Dictionaries are defined with curly brackets `{ }`, with items using a semicolon ` : ` to define a key-value pair, and commas to separate items. Most of the time a variable has to allocated to a dictionary in order to be able to use it. An example of a dictionary is:  
`Car_info = {“cars”:5, “colors”:”yellow”, “tires”:”round”, “factory”:”Daihatsu”}`  
Using square brackets `[ ]` allows the program to search for the key that is in the square brackets. For example, using `print (Car_info[“tires”])` will print out the value that is associated with the key `tires`, which is `round`. 
- **Tuples**: Similar to a list, except you can’t remove or add elements in a tuple. A tuple uses brackets instead of square brackets, and once a tuple is made you can’t delete or add new elements to the tuple. It is basically a single variable that can hold multiple things in it. Tuples cannot be altered once set, which makes them useful as a constant in programs. An example of a tuple is:
`Car_info = (‘cars’, 5, ‘yellow’)`  
Another aspect of tuples is that they can be used dictionary keys, or assigned to other variables. This makes it useful for setting multiple values to another (E.g. Assigning a coordinate to a name, like `location = (4, 5, 12)`).
- **Sets:** Similar to a dictionary, except without the key-value pairs. One useful aspect of sets is that they do not allow duplicate values, which makes it easier to check for duplicate values in a program instead of using a dictionary (the only other data structure that doesn’t let duplicates). You also cannot change them (add or delete elements) after a set has been assigned some values. A set uses curly brackets like a dictionary, but in the format of a list. An example of a set is:  
`Car_info = {‘cars’, 5, ‘yellow’}`

**Differences between data structures/sequence (Python):**  
Ordered: The order you add elements will stay the same in a list  
Changeable: Elements in the list can be altered, removed, or added  
Allow duplicates: Duplicate elements are allowed and considered 2 separate elements in a list  
No duplicates: Duplicate elements aren’t allowed and previous value will be overwritten by the newer value if there is duplicate

| Lists | Dictionaries | Tuple | Sets |
| :--- | :--- | :--- | :--- |
| Ordered | Ordered | Ordered | Unordered |
| Changeable | Changeable | Unchangeable | Unchangeable | 
| Allow duplicates | No duplicates | Allow duplicates | No duplicates |


Dictionaries are ordered as of Python 3.7 and onwards  
New values can still be added to sets, but cannot edit values or delete values  
Sets are in a random order everytime, so cannot manually locate a value in a set (you can use `If <variable> in <set>:` but not `<variable> = <set>[2]` like in a list).

### Integer, floats, and strings:
There are 3 main data types with Python: Integers, floats, and strings. An integer is a whole number, that can be used by Python to perform mathematical calculations. A float also acts the same as an integer, but can hold infinite decimal places, while an integer has to be a whole number. Integers can be the default data type for many Python functions and methods, such as `len()` and `range()` which returns an integer by default. A string however, can be any character. A string is treated as it is by Python, which means you cannot perform mathematical calculations with a string. You can print any character as a string as long as Python recognizes that character (an example of this is printing an apostrophe from a Word document, Python cannot recognize this character and it is printed as an encoded value). Strings can be manipulated with a variety of methods, such as `split(`) and `upper()`. Integers in a string cannot be used for math, and any methods that affect alhabetical characters are usually ignore with integer strings (e.g. Using `upper()` will uppercase normal letters, but numbers are ignored).

### Try & Except:
A Try and Except statement contains 2 statements: `Try` and `Except`. A `Try` statement tells the program to attempt running the code written within the statement; The `Except` statement provides the program with the backup code if the Try statement fails. A `Try` statement is always attempted first by the program, if the code raises an error, then the program will skip and move on to the `Except` statement, otherwise, if there is no error, the code in the `Try` statement is executed and the program continues, ignoring the `Except` statement. Try and Except statements are very useful for checking errors without breaking the program. 

### `for` loops:
This loop continues for a certain amount of times given. Usually, a `for` loop will count each item in a sequence (list, tuple, etc) and repeat for as many times it counts an item in the sequence. For example, the list `[‘car’, 5, ‘yellow’, 1]` has 4 items/elements in it, so the loop will repeat 4 times. A for loop usually requires a variable that will become the item that that the loop is currently counting. For example, `for x in <list>:` the `x` is a variable that will become whatever is being counted. If the list is `[‘car’, 5, ‘yellow’, 1]`, then for the first loop `x` will be `“car”`, then in the next loop `x` will be `5`, and etc. This lets us manipulate what happens each iteration for each item in the list, such as scanning whether `x` is an integer or not. If the loop is left alone as it is (`for x in <list>:`) then the program will loop for each item in the list. However, the range function (`range()`) can be used instead of a sequence. Using range() lets you manually decide how many times the for loop will go on for. 

### while loops:

### Functions:  
###### Lambda function:  
The `lambda()` function can be used to create an anonymous function in Python. An anonymous function is basically a simple function without a label; i.e. A function wihtout using the `def <function name>():` code. Usually the lambda function is given to a variable, then the variable can be used anywhere to use the function. A lambda function cannot du much except return a value. An example:  
```Python
greeting = lambda a, b, c:a + b + c
print (greeting("Hello ", "there ","friend!")
```  
This will print out `Hello there friend!`. As opposed to using a defined funtion, which would look like this:  
```Python
def greeting(a, b, c):
	sentence = a+b+c
	return sentence
print (greeting("Hello ", "there ", "friend!")
```  
This code does the same thing, but takes more lines and is more intricate. The uses of this function may be, for example, to create a sentence using any three words. By simply changing the values in the brackets, you can make a sentence using any word. Using lambda is much faster and easier that creating another defined function. However, a lambda function can only have one line of command. For example, this won't work:  
```Python
greeting = lambda a, b, c:x = a+b+c, print(X)
print (greeting("Hello ", "there ","friend!")
```  
as you're trying to do 2 things in one command. Lambda is only useful for replacing small quick functions, which can have a big impact when you're writing a big program.

### Methods: 
Methods are like functions, except they take data from an object in order to return a value. Most methods don’t have arguments as they do not require other data.

### Objects: 
An object is a certain type of data used by a program to organize different data values into each data type which makes it easier for the computer to run a program. For example, integers are considered an object, and is an integer data type. Integers are a different data type to string, which displays characters that may include numbers, but cannot use these numbers to calculate as they are not an integer data type. An object instance is an object generated from a class with specific attributes that are determined by the class. Instances of objects are just different versions of objects generated from the same class.

### Classes: 
A class is basically a blueprint for creating instances of objects. String, integers, are part of a class (strings belong to the str class, integers belong to the int class). This way it lets Python classify values as certain ‘objects’ which makes it easier for a computer to run the program. Classes are often called using `class: <class name>:`. `self` is the parameter that a class uses to access other variables within the class. It does not have to be named `self`, but it is always the first variable referenced in a class `init`. `self` contains the instance of the class (the current version of the class) which can be manipulated to provide different objects.

- ##### Instance variable:  
A variable made in the `__init__` function of a class (e.g. `self.cars = 5`). They apply to the current object of the class and not the whole class, letting you manipulate individual aspects of objects instead of the same thing over and over again.

- ##### Class variable:  
A normal variable made inside a class (e.g. `cars = 5`). Can be called by using `<classname>.<variablename>`. 

The variables in play can affect the class in different ways. For example:

```Python
class Car:
    wheels = 4    # <- Class variable
    def __init__(self, name):
        self.name = name    # <- Instance variable
```
Wrting this code lets you do manipulate the name of the class, but `wheels` stays the same as it is a class variable. For example:  
```Python
> car_type = Car(Ferrari)
> print (Car.wheels)
> print (Car.name)
```  
This code prints out `4` and `Ferrari`. `Wheels` stays the same but `Car.name` can be changed depending on what you put in the brackets when calling the class. If you don't allocate the class to a variable (`car_type = Car(Ferrari)`) then you cannot use the variable as this would create an error because just doing `print (Car.name)` wouldn't put anything inside the class, thus `Car.name` becomes nothing which raises an error. The class variable `Car.wheels` is used to change the value of the `Wheels` variable, and unlike the instance variable `Car.name` it can be called without using another variable (i.e. `print (Car.wheels)` would print out 4). You can also have 2 instances of objects using the same class, but `Wheels` would staty the same of each object instance. For example:  
```Python
> first_car = Car(Ferrari)
> second_car = Car(Honda)
> print (first_car.name)
> print (second_car.name)
```  
This prints out both `Ferrari` and `Honda`. Now if we:
```Python
> print (first_car.Wheels)
> print (second_car.Wheels)
```  
This will print out `4` for each one. Thus, class variabels remain constant for every instance, while instance variables differ from each instance. BE CAREFUL! An instance variable takes priorty over class variables, so if an instance and class variables have the same names it can replace your variables without you knowing and can break your program. E.g. `Car.Wheels = 5` and `first_car.Wheels = 10` will make `print (first_car.Wheels)` equal `10` instead of `5` as typing `first_car.Wheels = 10` creates an INSTANCE variable for that object instead of using the CLASS variable.

### __name__ variable:
The `__name__` variable is an inbuilt variable in Python that lets programs tell the difference between imported modules and modules inside other modules. `__name__` always defaults to `__main__` if `__name__` is being used in the program. However, if you make another program and import that program as a module in your original program, the `__name__` in your imported module will match the name of the module, instead of `__main__`. For example, take program 1 and program 2.

```Python
# Program1
print (__name__)
```

```Python
# Program2
import Program1
print (__name__)
```

If you run `Program1` by itself, `__name__` will equal `__main__`, as the `__name__` variable is being used in the same program. However, if you run `Program2`, you will get `Program1` and `__main__` as your outputs. This is because `__name__` becomes the name of the imported module if it is being used inside that module (`Program1`). Since `Program1` runs the `__name__` variable while being imported into `Program2` (which is your 'main' program) then the `__name__` in `Program1` becomes the program's name so Python can tell the difference between the original program (`Program2`) and the imported programs (`Program1`). Basically, `__name__` is an inbuilt variable that lets Python tell the difference between an original program and an imported program. THis is useful for making a program do different things depending on whether it was imported or not.

### Modules: 
A set of extra codes, functions, methods, objects that are kept separate from Python’s base programming to reduce unnecessary resources, as generally not all functions of Python are useful in a program. Certain functions are packed into modules, which then need to be called via import to be able to be used in Python. Modules are continuously updated and being added into Python, to expand Python’s use in modern times. You can also call a module by using <module_name>.<module_function>() if you don’t need to whole module and just a specific function from a module. It will only be called once though if you use this method to call the module, so with repeated uses it’s better to use import. There are different ways to import a module. For example, pretend there is a module called `Maths`. Module `Maths` has 3 classes inside that can be used when imported: `Addition()`, `Multiply()`, and `Powers()`.  
- `import Maths`: This will import the module and its contents into your program allowing to use the classes. To use a class in the module you have to sepcify the module and the class, e.g. to use the `Addition()` class, you have to type `Maths.Addition()`.
- `import Maths as numbers`: This will import the module and give it a different label to make it easier to type in (usually for complicated module names or long module names). It works the same as the previous method, except instead of typing `Maths` you use `numbers`, like `numbers.Addition()`. 
- `from Maths import *`: Like the presious methods, except you don't need to specify the module used. Instead, this import gathers all the classes in the module, and imports them as available in-built classes/functions/objects/methods etc. For example, you don't need to do `Maths.Addition()` anymore, you would just use `Addition()`. This usually hides the name of your modules which may be confusing when using multiple modules.

### Datetime module: 
The datetime module allows Python to convert strings into a to format, and vice versa. It must be imported first before being used as it is a module. The datetime module is mostly used when dealing with time formats and strings. `X = datetime.datetime()` is the general format of a datetime function. This function needs 3 arguments: A year, month, and date. You can also add hours, minutes, and seconds, microseconds afterwards but these are optional. An example of using this function is `X = datetime.datetime(2020, 4, 12)` which will print out the date `2020-04-12`. Another function from the module is the `strftime()` method (string format time method). This method formats the output of a datetime string in a specific format. DO NOT confuse this with `strptime()`, `strptime()` converts a string into a datetime using the format, while `strftime()` lets you print out specific time elements using formats. 
`strptime()` = Converts a string into datetime. 
`strftime()` = Lets you pick out which parts of a datetime object you want to print. 
For example, you type a string `2020/03/12`. Using `strptime()`, it converts the string into an actual datetime object that Python recognizes as a time. You want to find the month only, so using `striftime(%B`) month is printed out in full name, `March`. 

A table of accepted arguments (eg. `%B`) can be found by looking it up.

Datetime can be used to express a time or find the current time. `Datetime.now()` will provide the current time registered on your device, while `datetime(<int>, <int>, <int>)` will present a specified time. Datetime orders time formats as `<year>, <month>, <day>, <hour>, <minute>, <second>, <microsecond>`.

`Timedelta()` is another object in the datetime module that can tell the difference between two time values. For example, `difference = time - timedelta(hours=13)` will minus 13 hours from `time` (which is a variable that has a datetime value). `Timedelta` requires a specific value followed by an integer, and uses string values to specify the format. For example, `hours=5` means 5 hours. `Years=2` means 2 years. 

### Tkinter module:  
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
- `Label`
- `Listbox`
- `Menubutton`
- `Menu`
- `Message`
- `Radiobutton`
- `Scale`
- `Scrollbar`
- `Text`
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

#### Toplevel window management:  
Window Manager (WM) is used by tkinter to manage toplevel windows with Python. 

### String formatting: 
