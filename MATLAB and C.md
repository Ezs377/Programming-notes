# ENGGEN 131  

---  
[Skip to C](#c-language)

## MATLAB stuff:   
MATLAB has 4 main interfaces:  
1. Workspace on the right, this tracks all variables and displays them for us  
2. Files on the left, shows all the files in the current folder
3. Command window in the bottom middle, this is where we can write code separately one by one, or displays stuff from our code
4. Script editor window in the bottom top, this is where we can code scripts (like classes) which can be run within other scripts to create efficient code

The workspace displays all current variables that have been used/created by the script. Useful to keep track of variables.  
Files just shows the list of files in your current folder, so you can quickly go back and forth between projects.  
Command window can accept single line code (like an IDE) and it is also used to display (i.e. 'print') values and text from a running script. You cna run a script by simply typing the name of the script in the command window, as long as the file has an extension of .m.
Script editor window is for writing the main code, once it is named it can be saved as a file with .m extension, this allows it to be run using command window or by other scripts.  

A script is some code that does something. Scripts are just individual programs that can be run either by themselves or in another script.

Variables are simply allocated by doing `<variablename> = <value>`. E.g. `time = 4` gives a variable with value of 4. Variables are trcked and displayed in the workspace column.

Some variable names are built in MATLAB, such as `pi`. Calling these variables will use the built in value, HOWEVER we can overwrite them by using the same variable name on another value. When cleared, the built-in variable reverts back to the built-in value.  

The `clear` command is used to clear all variables in the workspace. It's recommended to call this command at the start of each script which clears out all current variables to prevent any accidental overwrites. Note that this will remove all variables and revert built-in variables to their original values. So if a variable can't be found error, then probably it got wiped by a clear command. ALso note that when editing using MATLAB editor (for script editing) using `clear` at the start will clash with MATLAB editor so comment it out when editing functions. You can also clear individual variables by simply typing `clear <variablename>`. 

The semicolon (`;`) can be used to hide variables in the command window. Usually the command window will display the values of variables as they are generated, since this can get messy real fast we can use semicolon at the end of a line of code to prevent it from displaying in the command window. E.g. `time = 4;`.  

Script files and variables can't have certain things in their name. Typically, no blank spaces and can't start with a number. Also try not to name any scripts and variables with the same name as other commands/functions/variables.  

Comments are written by starting the line with percentage (`%`). Comments are the same as Python. Comments with multiple lines are written using `%{` and `%}` for start and ending respectively.

There is also a help command, which can be followed by the name of another command to list the documentation for that command.  

We can also do header comments, which are comments at the start of the script. This will cause the command window to display them if we use the help command on the script, which displays the information in header comments on the command window display. Useful for identifying what a script does. This is how MATLAB uses the help command for all commands, each command has some header comments that is shown when we run the `help` command.  

`input` allows user input, while `display` displayes the value fo a variable on command window, like the `print` function.

## Basics of MATLAB:  
The command window lets us type single-line commands. The `ans` variable is called whenever we do a math operation, which stores the answer to the math equation. Clearing the worspace will clear the `ans` variable.  
Ctrl+C will stop the command. 
`'s'` sets the default values as string instead of integers, especially in input commands.  
- `input` can be used to have user input. Note that in MATLAB `input` and `display` only take one parameter, and can have attributes. The `display` command can join multiple parameters together by using (?)  
- When using `input`, using a semicolon at the end will hide the full output. THe input text shows up, but the result of the input doesn't show up like a normal variable.  
- `display` or `disp` is simply used to display text (AKA print).  
- You can concatenate multiple variables and text together on a single display by using square brackets `[ ]`. Note that these square brackets have to be inside the brackets for display, i.e. `x = disp([<some text>, <some text>])`. Use commas to separate. Use the `num2str` function to convert integer to string first for integer values, `num2str` works the same as `int(x)` in Python.
- `.^` performs operations on a matrix, but element by element instead of matrix manipulation  

Use dot variants of operations to ensure element by element calculations for arrays, otherwise they do matrix operation. E.g. `*` --> `.*`   

`num2str` and `str2num` convert between strings and numericals. The `disp(<text>)` displays text on screen, however integers and numbers should be converted to string first. `Var = input(<prompt>)` displays the given string on screen, and lets the user input a value that is allocated to the given variable.  

Splicing is done with :. 1:6 presents a list of numbers from 1 to 6. This can be used for loops, e.g.  
`for a = 1:6`  
Would loop 6 times.  

An `end` is needed for the end of every statement and loop  

`for` loops have basic notation of `for x = <range>` where x = variable, and `<range>` is usually an iterable object. An iterable object could be an array (goes through every element), string (goes through every phrase), character (goes through every character), or numerical, such as `2:10` which goes from 2 to 10, or `4:3:30`, which goes from 4 to 30 in steps of 3.  

REMEMBER: MATLAB starts counting from 1, so 1:6 is 1, 2, 3, 4, 5, 6. 6 values in total.

## Functions:  
Built functions exist in MATLAB. Use `help` command to see how to use each function. I/O (Input/Output) diagrams can be used to express functions and what they do.  
Functions can't have `input` commands, instead they are called like in Python.  

Variables in functions have their own unique workspace. A function has it's own unique workspace that doesn't interfere with the main workspace (local and global variables). 


A function generated by using the `function` code, followed by output arguments, equals, function name, and input arguments. It is recommended to have the same function name as the file name, but be careful not the make it the same name as a script. You can omit the output and input arguments, but the general notation is: 
`function <functionname>(x)`  
- To have a single output:  
`function <outputvariablename> = <functionname>(x)` (Note: X is an input variable, required as the function needs something to work with)  
- To have multiple outputs:  
`function [<firstoutput>, <secondoutput>, etc] = <functionname>(x)`  
- To have inputs:  
`function <variablename> = <functionname>(<inputvariable1>, <inputvariable2>, etc)`  

Finish function codes by using `end` at the end.  

When calling functions, the input variables are placed in the brackets of the funciton name, like `<functionname>(<value>)`, similar to Python. Functions return the value of the output variable automatically when it finishes, however the `return` statement can be used to return a value earlier.  

Functions are made by `function [<output var>, <output var>] = <Functionname>(<inputvar>, <inputvar>)`. Functions will return output variables, so output variables need to be given a value inside the function before function ends. Input variables is for variables directly used inside the function from the outside. You can omit the output variables or just leave one output variable, by removing the square brackets.   

The basic notation of a function is:  
`function <output vars> = <functionname>(<inputvars>)`  
Where output variables are allocated as the 'returned' values, and input variables are placed when the function is used in another script.  

Multiple output arguments from functions need to be put in square brackets, for example a function that returns 3 output variables using 2 inputs:   
`[a, b, c] = <functionname>(input1, input2)`  

## Planning and debugging:  
A simple framework for approaching problems:  
1. State the problem clearly  
2. Describe the input/output information  
3. Work out he problem manually for a simple dataset  
4. Develop the solution into a computer program  
5. Test the program with different sets of data  

**Debugging:**  
Coding errors happen frequently, usually syntax or logical errors. Obvious stuff. Debugging is diagnosing errors and finding out what's wrong with code. MATLAB has a very robust and extensive error detection system that tells you what's wrong, however logic errors are more difficult to find as MAGTLAB can't detect them.  

MATLAB can out breakpoints where the code runs until it reaches the breakpoint, allowing us to run a section of code bit by bit to check errors.  

## Logic:  
MATLAB uses ture and false logic, and assigns binary values of 1 and zero for each. The `logical` command can convert from values into logic. So each value in the values converts from values (e.g. Integers) into binary 1 and 0. Non-zero values are considered true, or 1.  

Boolean operators:  
- `==`: Equals to
- `~=`: Not equals to
- `>`: Greater than  
- `<`: Less than  
- `>=`: More or equal to  
- `<=`: Less or equal to  
Boolean oeprators return true or false.  

There are also logical opearotrs:  
- `~X` returns true if X is false  
- `X & Y` returns true if X and Y are true
- `X && Y` returns true if X and Y are true, but can't do arrays
- `X | Y` returns true if X or Y is true
- `X || Y` returns true if X or Y is true, but can't do arrays  

MATLAB opertes logic in this order: Arithmetic, relational, logical. So math operations are performed first, then it will do relational boolean operators first (comparison) and finally logic operators are performed.  

Note that doing `3 > 2 > 1` is false, because MATLAB goes left to right, so first it does `3 > 2`, which returns true, a value of 1. So it checks `1 > 1`, which is false.  

`if` conditions need an `end` comamnd at the end of the if statement to encapsulate it. `else` commands goe in-between.  

We can do `A == B` to compare elements the arrays A and B. This will return an array indicating either true or false for each element match. E.g. `A = [1, 2, 3]`, `B = [3, 3, 3]`. Doing `disp(A == B)` will cause MATLAB to cycle through each elements and compare them and check if they are equal. The result will be `[0, 0, 1]` as in index 3 both A and B have the value 3, so comparison will be true, and other elements aren't matching so they are false. We can do this to check if certain elemnts match a value, e.g. `A == 3` will cycle through A to check for a value of 3, and return `[0, 0, 1]` as well since the value 3 matches index 3 in array A.  




## Arrays:  
Arrays are similar to lists but they can be 2D. We have rows and columns for arrays in MATLAB. A list is basically a one-row array, or a 1D array. This also measn we can store vectors and matrices via arrays in MATLAB.  

We can loop through an aray using a `for` loop, similar to python. A `for` loop can take a range. E.g. `for a=1:5` loops through a range of 5.  
We can use `length(<array>)` to get the length of a 1D array, and use that in a range instead of hardcoding. Looping out of the array results in an error.  

A 2D array acts like a matrix. It can store data in rows and columns.  

With arrays, a COMMA adds a new column, and a SEMICOLON adds a new row. E.g.  
`array = [1, 2, 3]` creates an array of:  
`1, 2, 3`  

`array = [1; 2; 3]` creates an array of:  
```  
1  
2  
3  
```  
These can be combined in one line, e.g. `array = [1, 2; 3, 4; 4, 5]` creates:  
```  
1 2  
3 4
4 5  
```  
Note that arrays have to be even, you can't add mis-matched number of rows an columns, e.g.  
`array = [1, 2; 3; 4, 5]` creates:  
```  
1 2  
3  
4 5  
```  
But this makes an error because there is a missing column in the 2nd row. This is referred to as dimensional consistency, where the dimensions of an array have to match. We can think of array dimension as the amount of elements on the x/y axis, e.g. X = 5, Y = 3 means an array with 15 elements, with 5 rows and 3 columns (since a row goes left/right, and a column goes up/down).

Integers and string can't be mixed in one array, instead any integer becomes a string if there is any string in the array.  

Indexing through an array is simply done using `<arrayname>(<element number>)`. In Python we use square brackets, but in MATLAB we use normal brackets. Note that for 2D arrays, the indexing goes ROW BY ROW, not column by column. So indexing will go down first, then right if given one value. We can avoid this by specifying a row and column, since MATLAB goes by x/y rules. For example:  
`array = [1, 2, 3; 4, 5, 6]`  
Doing `array(4)` equals 4, since MATLAB tries to find fourth row, it's not there so it goes to next column. But if we do `array(2, 3)` we would get 6, becasue we give MATLAB the x/y coordinate for the array. In this case, it goes to 2nd row, then 3rd row.  

We can add elements to an array by doing `<arrayname>(<row>, <column>) = <value>`. If the row and column exceeds the current array, MATLAB will generate zeroes in place of empty elements. E.g.  
![image](https://user-images.githubusercontent.com/79125281/184267844-5a56bd27-1286-4a79-952c-e9275a981d92.png)  

When concatenating arrays, they have to be dimensionally equivalent on one axis. For example, we can combine a 2x3 array with a 2x1 array using a COMMA, because this just adds 2 new rows, and a comma adds rows. But we can't combine a 2x3 array with a 2x1 array using a SEMICOLON, because that means we try to add 2 rows as columns, which doesn't work because then we have 2 rows at the bottom, but each row has only 1 column, and the original array has 2 columns, so they don't match. E.g.  
![image](https://user-images.githubusercontent.com/79125281/184268796-5d659045-c000-4215-96b6-3497c12eb3f6.png)  

We can find the size of an array using `size(<arrayname>)`. This returns the amount of rows and columns, so we need to use `[<variable1>, <variable2>]` to store these values. `length(<arrayname>)` returns the length of the largest dimension, which could be the rows or columns depending on which has more.  

There are also many default functions that return certain arrays, e.g. `zeroes(3, 2)` returns a 3x2 array of zeroes. This can be used to preallocate data to minimize memory usage.  

We can use arrays to plot graphs and diagrams using plotting functions, such as `surf(<arrayname>)`. This involves vector and matrix techniques from ENGSCI 111.  

Any array manipulation such as addition, multiplication, etc have to be dimensionally equivalent.  

A dot operator, e.g. `.*` will perform the calculations element by element instead of the whole array, which is matrix manipulation. The dot operator can be added to any operator. Without the dot arrays will perform matrix calculations instead.  

Basic notation of an array is `A = [1, 2, 3]` produces one row with 3 columns. `A = [1; 2; 3]` produces 3 rows and 1 column. You can mix both.  

Indexing arrays are the same as python, but (x, y) means (rows, columns). Basic notation is `A(2)` finds 2nd element in array A. However, with 2D arrays this will go down rows and go to next column once bottom row is reached. For more accuracy, `A(2, 3)` finds the element in row 2, column 3. You can also use slicing.  

To create a matrix of zeroes for data allocation, use `var = zeros(x, y, parameters)`  

Arrays use commas (,) to make new columns, semicolons (;) to make new rows.  
E.g. `[1, 2, 3]` makes 1 2 3  
But `[1; 2; 3]` makes  
1  
2  
3  

Element indexing uses normal brackets (), but indexing goes by ROWS. We can specifcy row and column by using xy elements, e.g. `array(2, 3)` finds the element in row 2, column 3.  

Array slicing can use `A(1:end)`. `end` simply goes to the last element in the arrray whether it's 1D or 2D.  
2D array indexing uses `A(a:b)` and `B([a, b])`. Using colons (`a:b`) navigates through rows in the array, while using square brackets (`[a, b]`) navigates through columns in the array. Combining these two operators, e.g. `A(2:4, [1, 2])` will find a certain 'section' of the array that fits these coordinates. In this example, we pull out rows 2 to 4, and columns 1 to 2. The intersecting values for these columns and rows are the values we get from the 2D array A.  

Array indexing slicing can go backwards as well, by doing `a:-1:b`.  

Basic format of slicing is `a:b:c`, where a = start value, b = step, c = end value. b can be omitted.  

Arrays can be generated by doing `A[]`. You can add elements by simply force indexing (e.g. `A(4) = 12` will make the element 4 equal to 12. Note that adding elements that are beyond the current elements in the array will set the extra elements as zero, e.g. If we have an array `A = [1, 2, 3]` and we do `A(5) = 5` then this adds 5 to element 5 in the array, so we get `A = [1, 2, 3, 0, 5]`. We have a zero because the zero acts as a placeholder element to fill in the gap between element 3 and element 5.  

This is one way to addend elements to an array. Another way is to concatenate arrays, basically merge two arrays together. We can do slicing indexing to specify which elements we want to add/replace, e.g. `A(4:6) = 5` will make previous array A equal `A = [1, 2, 3, 5, 5, 5]`. We can merge arrays together this way as well, e.g. `A = [1, 2, 3], B = [4, 5, 6]`. If we do `C = [A, B]` this merges both arrays together, with A being the first in the row and B being the second set in the row. So `C = [1, 2, 3, 4, 5, 6]`. 

We can also do `A(4:6) = B`. This replaces elements 4 to 6 with elements in array B, so `A = [1, 2, 3, 4, 5, 6]`. However, this notation is very specific and if the array lengths don't match up then it will come up as error, e.g. `A(3:6) = B` = error, because 3:6 is 4 elements (3, 4, 5, 6), however array B only has 3 elements, so error.  

3D arrays can be used to create images. Basic notation is `A = (<row>, <column>, <layer>, 'uint8')`. The `uint8` is to ensure unit integer 8 values are used instead of double values which can bug out when making images. Combined layers will produce a cell in the same row/column that is the combination of all values in the same row/column from other layers, RGB uses values from 0 to 255 (256 values).  

Colons in array indexing selects everything in the given input. E.g. `A(:, 2)` means select ALL rows in column 2. This will set all values in a vertical column into a the set value. `A(5, :)` means select ALL columns in row 5, this will set all values in a horizontal row into the set value. Doing `A(:, :)` selcts ALL elements in the array. However, we can use this to select all values in a layer in a 3D array, e.g. `A(:, :, 1) = 200` means select ALL elements in the first layer, and set it to 200. This can be useful if we want to set a layer into one colour as a base palette for making images.  

You can remove elements from arrays using `[]`, e.g. `A(2) = []` would remove element 2 and re-order the array so that it becomes shorter (instead of just setting the element to zero, which keeps the array length the same).  

### Slicing:  
Slicing is just using ranges and manipulating lengths to get values. Slicing is similar to Python in that you use `:` to set a range and step. E.g. `1:3` means a range from 1 to 3. The only difference is that MATLAB counts from 1, not zero.  

With arrays, doing `<arrayname>([<element1>, <element2>, ...])` will get the respective elements from the array and put into a separate array. This is useful for picking out elements in an array.  

With 2D arrays, we can slice the rows and columns separately, by separating the slices with either comma or colon, e.g.  
`<arrayname>(<slicerows>, or ; <slicecolumns>)`.  

## Graphs:  
MATLAB can produce graphs and diagrams using a variety of functions. These graphs will often utilise arrays for values in the graph.  

`plot(x, y)` creates a 2D graph using x and y values. `xlabel`, `ylabel`, `title` set the respective axis and titles for the graph. `hold on` lets you plot points until you don't want to, at which point you do `hold off`. Otherwise the graph resets itself each time you change it.  

For x/y plots, you can use trigonotmetric values straightup (e.g. `sin(x)` generates the sin graph for values of x). You can also use `linspace(<start>, <end>)` to generate a straight vector from start to end, this can be used to create straight lines in a graph if we plot it as an x or y value.  

Note that the `plot(x, y)` needs at least a linspace value to make a graph, it can't just take a number by itself. E.g.  
![image](https://user-images.githubusercontent.com/79125281/186138487-3687f563-71f2-41ce-92e9-f9e001273b00.png)  
linspace basically makes a direction in either x or y, combining x and y directions in a graph creates graphs. You CAN do simple points by using numbers only, but it doesn't show up unless you use a line specification. `linspace` makes it easier to set evenly spaced points on a graph, as opposed to using `0:end` which has no control about the spacing of the points, and doesn't include endpoints. 

Think of the X values as the list of x values, when we usually do a function of x (e.g. Y = X<sup>2</sup>) we still need X values to input in so we know where to plot Y values. Same here on MATLAB, we need 2 variables, one is the list of values, and the other is a function of the other variable. In most cases we get a list of values for X (either using `linspace` or `start:end`) and we use a function of X for the Y values (e.g. X<sup>2</sup>).

General notation for `linspace` is `linspace(start, end, steps)` where steps is the number of evenly spaced points between start and end. 

You can also change the colors and styles of the lines in graphs by adding a line specification in the plot function. General notation is `plot(x, y, <specification>)`. Line specifications can use:  
Colors:
> r, g, b, c (cyan), m (magenta), y, k (black), w (white)  

Lines:  
- `-`: solid line ( ___ )
- `--`: Dashed line ( ---- )  
- `:`: Dotted line ( ...... )  
- `-.`: Dashed dotted line ( -.-.-.- )  

Markers (for points):  
Common characters are `o`, `+`, `x`, `*`.  

3D plots work similarly except we use `surf(x, y, z)` to plot the 3d graph.  

Subplots allow us to plot multiple graphs in one window. THe general notation is `subplot(<rows>, <columns>, <currentposition>)`, where rows is the amount of rows you want for graphs, columns is amount of columns for graphs (e.g. 2, 2 means 2 rows and 2 columns of graphs, 4 graphs total in a 2x2 grid). currentposition is the current plot you are plotting. You do the subplot function first, then do the plotting code. Then you do another subplot and switch currentposition to another, and plot again, and repeat until you fill out all graphs. E.g.  
`subplot(2, 2, 1)`, then do plotting code to do first graph. Then do  
`subplot(2, 2, 2)`, then do plotting code for second graph. And repeat 2 more times.  

## Strings:  
A string is an array of characters. By default, MATLAB uses type double variables, which takes up 8 bytes on the memory. A byte is 8 bits, so overall there are 64 possible length of binary (64 0's and 1's). Type unsigned 8 bit integers only take up one byte in memory.  

The char data type uses one byte, which has 2<sup>8</sup> bits, giving us 256 options. The ASCII table only has 128 characters, so one 8-bit byte is enough to hold the entire ASCII table.  

NOTE: There is a data type called string, but the official definition is that a string is an array of CHARACTER data type. A string data type uses double quotes, character data type uses single quote. A string by definition is just an array of characters, NOT a string data type.  

Strings are created by using single quotes for values in an array. E.g. `A = ['hello']`. The length of a string is the amount of characters in the array, INCLUDING blank spaces.  

### Representation characters as numbers
We mostly use ASCII values for this course in MATLAB. So we can convert between ASCII numbers and the characters. `char(<array>)` converts numbers into ASCII characters using the given numbers. Note that any number input works, even if it's in an array. E.g. `A = [72, 105]` can be converted by simply doing `char(A)` which gives `A = 'Hi`', where `Hi` is an array of `[72, 105]`, or `['H', 'I']`.    

Strings will try to calculate ASCII values if you add a character and number together. E.g. `A = '72'+1` will actually return `A = [55, 50]`. This is because MATLAB assumes you are referring to the ASCII values when you try to add characters with a number, so it will convert the string into ASCII values first (The ASCII for character '7' and ASCII for character '2'). This results in `A = [55, 50] + 1`,which becomes `A = [55+1, 50+1]` = `A = [56, 51]`. So performing maths with characters and numbers will make MATLAB convert characters into ASCII values first.  

Note that in a string, MATLAB counts each individual character. So `A = 'Hello'` is seen as an array with 5 elements, or an array of 5 ASCII values.  

We can convert between strings and numbers using `str2num` and `num2str`, or `int2str`.  
`str2num` will directly convert a string to a number if the character represents a number. E.g. `A = '45'`, `str2num(A) = 45`. The number can be directly used for calculations without considering ASCII values.  
`num2str` will convert a number into ASCII character array. Note that this DOES NOT convert a number into ASCII character, it simply converts a number into a string. E.g. `A = 45`, `num2str(A) = '45'`. This doesn't turn the number into ASCII characters (use `char` for that), it just turns mathematical numbers into string.  

`int2str` converts integer values into string characters. It doesn't convert numbers into ASCII characters, it literally converts the number into characters instead of integers. They would be classified as characters instead of integers, and can't be used for maths. Integers will also be rounded.  

`int2str` and `num2str` both do the same thing in that they convert numbers into a character array, HOWEVER `int2str` will round the numbers first to the nearest whole integer before converting to characters, and `num2str` will convert the number as it is into characters. E.g. `A = 3.45`, `int2str(A) = '3'`, `num2str(A) = '3.45'`.  

However, for long numbers, `int2str` will present the character as the entire number itself, while `num2str` will present the characters in scientific notation. E.g. `A = 3.4*10^34`, `int2str(A) = 30000000000000...` while `num2str(A) = 3.4e34`.  

### String arrays
Strings are just arrays of characters, so we can use indexing and slicing as usual to find elements in strings. E.g. `A = 'Hello'`, to find `e`, we can just do `A(2)` which gives us `'e'`. We can also repalce characters by simply assigning an element to another value, e.g. `A(2) = 'T'` will make `A = HTllo`. (need to tst what happens if we replace a character with multi-character string).  

Array rules apply to strings, including concatanation, slicing, columns/rows, etc.  

Uppercase and lowercase matter for strings, since uppercase and lowercase characters have different ASCII values. Use `upper(<string>)` or `lower(<string>)` to set all characters to uppercase or lowercase. E.g. `B = upper(A)` will set B to have uppercase charcters of string A.  

### Comparing
Comparing string is done with several functions. These functions return true if the compared string are exactly equal (including whitespaces):  
- `strcmp(<string>, <string>)` will directly compare the 2 strings, and return true if they are both exactly the same characters
- `strncmp(<string>, <string>, <number>)` does the same thing, except \<number> = any number that specifies the amount of characters compared. In this case \<number> resembles the first n characters in the string. Note that this function starts counting from the start of the string.  
- `strcmpi(<string>, <string>)` will directly compare strings but ignore lowercase/uppercase differences  

`strfind(<string>, <pattern>)` can be used to find a specific set of characters in a string. This function returns the POSITIONS of every matching character set within the string, with the first character as the returned position. \<string> is the string to be checked, and \<pattern> is the set of characters you want to find in the string. E.g. `A = 'hello'`, `strfind(A, 'h')` returns 1, because the character 'h' is in position 1 of the string. However, `strfind(A, 'l')` will return \[3, 4], because the character 'l' appears in these positions. `strfind` wil locate the positions of chracters, unlike `strcmp` which only returns true or false.  
![image](https://user-images.githubusercontent.com/79125281/187030619-adbfb667-b38e-4ca7-8a3d-736a4c45f4e0.png)  

`strfind` is case sensitive, however we can use `upper` or `lower` on the string input, e.g. `strfind(lower(A), 'h')`.  

`sscanf(<string>, <outputstring>, <amount>)` can also be used to find certain strings in a text and display them in a format. \<string> is the text to be scanned, \<outputstring> is the pattern to look for in the text, \<amount> is the amount of matching scans you want. We use percentage specifiers in \<outputstring>, which will be the returned value if the function finds the matching string. E.g.  
![image](https://user-images.githubusercontent.com/79125281/187072432-771715eb-8247-4939-b3e0-a86b0c1abdc9.png)  
Notice that the function returns the value of the given percentage specifier, not the whole string. So we can use `sscanf` to search for a specific value and return it based on the text. For example, if we had a text that listed number of items needed for shopping, we can scan it and return just the number of items needed without reading the whole thing, e.g.  
```  
list = 'Need 12 apples, 16 banannas, and 10 bread loaves' 
items = sscanf(list, 'Need %d apples, %d banannas, and %d bread loaves')  
items = [12, 16, 10]  
```  
Sometimes this can be useful if we know what the text contains. A similar function is `fscanf(<fid>, <outputstring>, <amount>)` which works the same except \<fid> is the id number of recent file opened. `fscanf` scans a file instead of a given text.  

### Formatting strings
`sprintf(<format>, <variables>)` can be used to format string outputs nicely. This uses percentages and symbols (e.g. %d), similar to string formatting in Python.  
![image](https://user-images.githubusercontent.com/79125281/187031065-44425dec-986a-46ad-8712-1d55292b2a5a.png)  
`sprintf` returns a string output, while `fprintf` writes the output to the given file ID, which is `fid`. The \<format> is just text that goes with the output, it is always displayed along with variables. E.g. `A = sprintf('Hi there %s', 'Mike')` will output "Hi there Mike". The "Hi there" is always outputted, while the variable %d can change depending on the given variable (in this example the given variable is a fixed string value so this will always be the same output).  

The percentage symbols can produce different results depending on the symbol following the percentage. Note that variables will be allocated to percentages in order. Common percentage symbols (specifiers) are:  
- `%s` = String variable output. Use for strings only  
- `%c` = Character variable ouput. Use for singular characters only, useful for looping through strings  
- `%d` = Integer variable output. It is an integer, so it will round values, and convert characters into ASCII  
- `%e` = Scientific notation variable output, e.g. '34e+100'  
- `%f` = Floating point decimal variable output, e.g. '0.0000000032'  
- `%g` = Will attempt to output using `%e` or `%f`, the shorter output will be produced  
Specifiers are inserted within strings in the `sprintf` function. They are not inserted outside of the stirng display, only the variables are outside the string display. E.g.  
`sprintf('There are %d ducks in %s', noofducks, cityname)` where `noofducks` and `cityname` are variables.  

You can also 'reserve' spaces when outputting variables to make things look neat. This is done by inserting a number between the % and specifier character, e.g. `%4s` means reserve 4 spaces infront of the output.  
![image](https://user-images.githubusercontent.com/79125281/187069961-800bd48b-4e02-4d8e-9201-52a8f562b173.png)  
Note that the blank spaces are placed in FRONT of the output variable. If the output variables takes up more space than the given reserved spaces, then MATLAB ignores the reserves so it can fit the whole variable output. Basically, the whitespace reserves have to be more than the length of output variable.  

There is also a method to control the amount of decimal places for numbers, by using dot+number between the % and specifier. This number specifies the number of DECIMAL places of an integer/decimal output.  
![image](https://user-images.githubusercontent.com/79125281/187071496-63782613-76b1-4256-a4e3-e6e0d166645e.png)  
Note this only controls the decimal places, not the whole number. However, MATLAB will round the last decimal value, e.g. 3.41156 with a specifier of `%.4e` will display `3.4116` as we specified 4 decimal places, MATLAB rounds the last digit.  

The whitespace reserves and decimal specifiers can be combined together. The whitespace reserves go first, followed by dot and decimal specifier, e.g. `%3.2e` will reserve 3 whitespaces and limit the output to 2 decimal places.  
![image](https://user-images.githubusercontent.com/79125281/187071574-efabdd78-a2b1-4264-8507-8d41461443ee.png)  

Special characters are similar to Python, e.g. `\t` will do a tab.  
- `\t` = Tab
- `\n` = New line
- `\\` = Cancels the backslash, leaving the character `\` displayed  
- `''` = Cancels the quote marks, leaving the character `'` displayed  

Double backslashes cancel out special characters, e.g. `\\n` will display `\n` instead of doing a newline.  

With everything:  
![image](https://user-images.githubusercontent.com/79125281/187071862-af92e711-3e12-4912-b6f3-e9007952f5ce.png)  

## 3D arrays:  
Can be used for graphics. Uses RGB colors, every color generated is a mix of red, green or blue. We can use unsigned 8 bit integers (uint8 in Matlab notation) which gives us 2<sup>8</sup> values, or 256 different values, which is 0 to 255.  

Typically, with a 2D array, we can only do single color cells, since a 2D array only has rows and columns, so each element only holds one value. So we usually just do grey scale images, where values from 0 to 255 give a shade of grey, where 0 = total black, 255 = total white. Anything in between is just a shade of grey. However, if we want color, we need a red, green, and blue value that will mix together to form a color. Each RGB value is 0 to 255, so we need to hold 3 values in one 'cell' of the array. 3D arrays let us do this. since 3D arrays allow us to do 'layers' of 2D arrays stacked on each other. So we have a 2D array for each RGB color basically, we have a 2D array for red, green, and blue, and each array holds values from 0 to 255. So each 'cell' in the 3D array is actually 3 2D elements stacked on top of eah other, i.e.  
![image](https://user-images.githubusercontent.com/79125281/186546011-38c60d10-f33e-4c8e-b5b1-38a496150ccf.png)  
3D arrays need 3 inputs, a row, column, and layer. E.g. `A = (1, 1, 1)` means row 1, column 1, layer 1. Hence, we can justify the values for each layer (AKA color) by this method. E.g.  
![image](https://user-images.githubusercontent.com/79125281/186546247-238efbed-0b21-4e63-bdf1-588a8a0c2854.png)  
This creates a cell with color pure green, since we justify the same column and row, but we only put 255 for the green layer, and leave other layers = 0 for that same cell (row/column). Note that cell means I refer to an element in the 3D array that is the result of all stacking 2D arrays.  

To force an array to have uint8 values instead of double integers, we can do `A = (1, 1, 3, 'uint8')` which makes all values unsigned 8 bit integer values which is more efficient when going to 256. This is important when working with images, make sure it is uin8 not double integers, which is the default.  

We can use colons to say we want all rows and columns to be the same value. E.g. `A = (:, :, 1) = 10` means put the value 10 in ALL rows and columns in LAYER 1. 

`imshow(<array>)` can be used to display images, whether grayscale or RGB. The function runs a different function depending on the array input, if it's 2D array then it will try to run a grayscale image, if it's a 3D array then it will try to run an RGB image. 

`rgb2gray(<image>)` can be used to convert an RGB image to grayscale. You can also directly show an image from file using `imshow(<filename>)`, OR use `B = imread(<filename>)` then `imshow(B)`. Another thing with this method is that we can analyze the image itself by 3D array indexing, e.g. `C = B(:, :, 2)` will put the second layer of image B into variable C. The second layer should be the green color part of the image, but because it's produced as a 2D array the iamge will be grayscale image of all the green RGB values.  

`size(<array>)` returns the size of the given array as vectors, e.g. `A = [1, 2, 3]`. `size(A) = [1, 2]` since A has 1 row and 3 columns. If we specify outputs such as `[a, b, c] = size(A)` then each variable becomes the value of the dimension of the array, e.g. `A = [1, 2, 3]`, `[a, b] = size(A)` would make a = 1 and b = 3, since A has one row and 3 columns, and these are allocated to the variables. THis lets us manipulate 3D arrays quite well especially with imported images.  

If we import an image first, then use `imread` on the image and allocate to a variable, we actually get a 3D array representing the image. Using `size(A)` we can get the dimensions of the 3D array, and then we can manipulate the 3D array by using the dimensions for each layer and chaning the values for each layer, changing the colors of the image.  

## Cell arrays:  
Cell arrays use curly brackets instead of square brackets. Cell arrays can contain arrays inside them, such as multiple strings (a normal array can usually hold one string because a string is a bunch of single characters that make up an element each, multiple strings get joined together instead of separate). 

Indexing cell arrays use curly brackets (\{}) instead of normal brackets. This will call the element, which is an array in itself. This is really useful because we can store multiple arrays in a cell array, then index them individually and separately (e.g. Index cell array using curly brackets and allocate to variable, then index the array using normal brackets). Allows for much more data storage, at the cost of longer runtime.  

Cell arrays work the same way as normal arrays, but use curly brackets for functions instead of normal brackets, such as adding new elements, which would be `A{3} = 'Hi'` instead of using normal brackets. 

Using normal brackets will take out another cell array of the chosen element when indexing, instead of the actual element.  

## Files:  
Files can also be imported/exported in MATLAB. `fcanf` and `fprintf` have been covered which will scan and print from a file.  
A MAT file is used to store variables and their values, useful for large values. MAT files don't store data as readable data, so it looks like gibberish until you open it in MATLAB.  
To save files to a MAT file (or create one), simply do `save <filename> <variable1> <variable2>...`. It will craete a new file if the filename is different or unregistered.  
To load a MAT file just do `load <filename>`. This loads ALL stored variables into MATLAB, which can be allocated to other variables. To call a specific variable from the MAT file (if known), do `load <filename> <variable1> <variable2>...`.  
Doing `save <filename> -ascii <variable1> <variable2>...` will store the data as readable data in the MAT file.  

`fopen(<filename>)` will return the file id (`fid`) which can be used for future referncing, e.g. `fscanf` function. The `<filename>` is a string, which is the full name of the file. If `fid` returns a negative number, that it means the file doesn't exist in the folder.  

Do `fclose(<fid>)` when done using a file. This prevents errors when multiple functions want to access the same file, as the file can only be opened by one script/function at a time.  

`fgetl(fid)` is used to get a whole line of text from a file, and return it as a string (it won't include the \n at the end of the line). A line is considered as some text that has a ]n at the end of it. Since we get a string output we can do the usual string functions on this. This function will select the first line in the text, subsequent uses will make the function select the next line (for the same fid), and etc until it reaches the end, where it wil return -1 to indicate no more lines.  

## C language  
**onlinegdb.com is an online compiler for C if needed, otherwise visual studio code can be used.**    

---  

We can run C code from command line or through a GUI (e.g. Visual Studio). C requires a compiler to run, so either method of running C can work. C differs from Python, in that C is a compiled and Python is interpreted. This means that we can write C using any text editor (e.g. Notepad), but we also need a compiler in order to run the code. Whereas Python requires installation, but afterwards we can use any code editor to run it. For C we only need to downlaod the compiler, which is Developer Command Prompt Visual Studio, which has the layout and commands of Windows command prompt. 

To compile a file using Developer VS, use `cl /W4 <filename.c>` to compile the code. This creates an exe file of the code. Then simply run the exe file by selecting it in the command prompt menu.  
- `cl` means compile
- `/W4` means set the warning levels to level 4, which displays all warnings up to level 4. Recommended setting.  
- `<filename.c>` is a file with the .c extension

Comments are either written single line using `//` or use `/*` to start a multiline comment and `*/` to end a multiline comment.


The basic format of basic C code is:  
![image](https://user-images.githubusercontent.com/79125281/190274792-9639995e-ff6f-4ac6-8c5a-6b5103f29ce5.png)  
`#include <stdio.h>` is for the preprocessor to collect all the 'functions' for the program. It's like calling modules in Python, although in C we are calling the labels of the functions, which is contained in the system files, instead of the functions themselves. Note that the `<>` specifies the default system library of files and will scan those first, if we remove the `<>` then the preprocessor scans the current directory instead. `stdio.h` contains basic functions such as `printf`.  

`int main(void)`: This has several components:  
- `int` states an integer value
- `main()` marks the start of the program execution. It is essential to the compiler. Everything other variation is a function definition of `main()`  

`int main()`  simply states that the returning value should be an integer. We do this by adding a `return 0` at the end of the program to ensure that the program returns an integer, even though the program will return 0 by default, it is good practice to ensure the returned value is an integer. Returning a value marks the end of the program for the compiler.  

- `void` means null, AKA nothing. Adding this in place of the `int` in the `int main()`  means the returned value will be null. This means we don't have to do the return code, but this program doesn't work with C++ or Unix systems.  

Doing `int main(void)` means that NO arguments are passed to the `main()` function. This is helpful when we don't want to input anything from outside the function. On the other hand, `int main()` means that the function will accept ANY arguments, including none. These notations perform similar processes, however if we don't want to pass any arguments then `int main(void)` is preferable since it ensures no arguments are passed.  

Variables can be declared on one line by separating with commas, e.g. `int a, b, c;`.  

`const` can be used while declaring variables to make it a constant. Constants caanot be altered in the code and C gives an error when trying to alter a constant, hence protecting it from accidental edits. Another advantage is that constants are stored elsewhere instead of RAM memory which can speed up a program.  



Apparently command prompt is used sometimes to find files for C. You can run C files through DEVELOPER visual studio command prompt.  

Escape characters lets us print out characters that would usually be interpreted as a function character (e.g. `"`). Doing just `""` will make C think that we are trying to print a blank string. TO print the quotation marks directly, use `\"` to print out the quotation marks.  

Like MATLAB, semicolons are needed at the end of each line.

`printf` is for printing out strings. Printing syntax is similar to `sprintf` from MATLAB, using the percentage formats. Percentage xyntax is similar to MATLAB, e.g. `%.2d` will print out a decimal value to 2 decimal places.

THere are 3 main types of data in C:  
- `int`: Integers, whole numbers
- `double`: Floating point numbers, i.e. decimals
- `float`: Extended versions of `double`, is longer
- `char`: Characters 

`#define CRT_SECURE_NO_WARNINGS` tells the compiler to ignore any warnings related to `scanf` function which we can ignore.  

`scanf` is for user inputs.  
`\n` does newline for printing.  
`/` division operator will discard remainder if we specify the output as int.  
 
However, to directly convert a variable during oeprations, the syntax is `(<type>) <variablename>`. To specify a new variable, you do `<type> <variablename>` which creates a new variable.

C has fixed storage sizes for data types.  
(picture)  
C can't store very large numbers with accuracy unlike Python. So numbers that exceed the storage size, will loop back into the negatives, dangerous!  

Put `#include <stdio.h>` at the start of every program, specifies an input/output thing.  

Doing `int x` then `x = 4.5` will cause the variable to become an integer, but because we specified a decimal value C will remove the decimal point and we can potentially lose data.  

Operations can be done within the `printf` statements directly.  

Note that C uses BEDMAS, but left ot right for equal operations (e.g. Plus and minus). 

For percentage syntax, we can use `%lf` in `scanf` to store double values. For printing we use the `%f` syntax which is for both doubles and floats.  

`int` calculations, espcially division, will always round down no matter what. So `int 119/10` will equal 11 no matter what. 

## Statements:  
`if`, `while`, `for` statements share the general notation:  
```C
<statement> (condition) {
      <code>  
}
```

For example:  
```C
if (a > 4) {
 printf("hello");
}  
``` 

Be careful though, adding a semicolon to the statement will not cause an error, but code will not run properly, e.g.  
```C
if (a > 4); {
 printf("hello");
}  
``` 

The conditions have to be put in brackets otherwise we get error.  
`else` is implemeneted like this:  
```C
if (a > 4) {
 printf("hello");
} else {
 printf("123");
}
```   

However, `for` statements require different parameters, separated by a semicolon in brackets:  
`for` loops need 3 parameters: `<init>`, `<condition>`, `<increment>`  
- `<init>` is the starting variable and value. You designate a variable to use for the loop here
- `<condition>` is the conditions of the `for` loop  
- `<increment>` is the increment for the loop control; variable (the one stated in the `<init>`)  

We can increment a variable using `X += 1`, OR `++X` or `X++`. Decrement uses `X--` or `--X`.  

An example of a `for` loop:  
```C
for (a = 10; a <= 20; a++) {
 <code stuff>
}
```
Note that the `a++` is the same as doing `a = a + 1`.  
This notation also lets us decrement values in the `for` loop, which may be useful when cycling through arrays.

Loops can use `break`, and `continue`, which does the same thing from Python.  

## Arrays:  
Arrays are created by doing `<arrayname>[<arraylength>];`. E.g. `int array1[7]` creates a 7 integer element array. Note that arrays start at zero when counting.  
However, to actaully generate the array, we need to give it values, e.g. `int array1[3] = {2, 3, 1};`. We use cruly brackets to define the values in the array. We can still leave the array length only to preallocate the length, and assign values later, e.g. `int array1[30];` will create a 30 element array that can only hold integers, which we can put in later.

Remember that an array needs square brackets to be declared as an array.

We can't have the amount of values exceed the given array length, BUT we can set the length to undefined so that the array will resize itself based on the given values, e.g. `int array1[] = {32, 4, 12, 55, 12};` will create an array with these values. To assign single elements in an array, we do `<arrayname>[<element>] = <value>;`. E.g. `array1[2] = 12;` will set the third position (since arrays start from zero) to value of 12.  

We can do several things to array elements. We can change the value of an element by accesing the element index, e.g. `array1[3] = 10` will change element 2 (since indexes count from 0) into value of 10, although be careful that you don't change an element that is within the array length (i.e. If array length is 3 don't change element 7).  

Declaring an array length to one value will make all the elements that value, e.g. `array1[4] = 2` makes all elements the value of 2.  

Assigning elements to a variable is just `var1 = array1[2]` which assigns the 3 elemenet in array1 to a variable.  

Remember that arrays need a type (e.g. `int`) when being declared, and can only store data of that type only. 




**2D arrays:**  
2D arrays are called using `<arrayname>[x][y]`, where `[x]` is the row element and `[y]` is the column element, like MATLAB. However, C starts counting from zero so be careful of that.  

To specify 2D arrays, we can use normal brackets to enclose rows, and curly brackets for the whole array, like `<arrayname>[x][y] = { (<row1val>, row1val...>, <row2val>, <row2val>...) ... };`.  

The syntax is neater when we write it in the form of  
```C  
int array1[3][5] = {  
 {1, 2, 3, 4, 5},  
 {6, 7, 8, 9, 10}, 
 {11, 12, 13, 14, 15}  
}  
```  
As it lets us see the rows and columns easily. It is also possible use `array1[2][5] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}` where C will automatically assign values to a row until it reaches the end of the first row, then move to the next row and keep going.  

With 2D arrays, we have to declare the size of the ros and columns beforehand, in the `[x][y]` brackets. Whereas in 1D arrays we can just leave the brackets `[]` and C will fill them out depending on the given values automatically.  

While a 2D array looks like rows and columns to us, the computer actually stores 2D arrays as a single line. However, because C treats a 2D array as a collection of 1D arrays, the pointer address always points to the first element in a 1D array. E.g. `<pointer>[0]` is the first element in the first row, `<pointer>[1]` points to the first element in the SECOND row. 

Storing values in a 2D array is done by designating the row and column, e.g. `[2][5]` goes to row 2, column 5, but remember that C starts counting from zero.  

Doing `int array1[10][10] = {0};` will make a 10x10 2D array that has elements of 0 only. USeful for preallocation.  





## Functions:  
Basic notation:  
```C
<datatype> <functionname>(<inputvar>, <inputvar2>...) 
{
 <code>
} 
``` 
`<datatype>` and `<inputvar>` can be replaced with `void`, which means nothing so it will make the function ignore inputs/outputs.  
Functions should be placed before the `int main(void)` call, i.e. Functions should be called first. Technically, `int main(void)` is also a function, however, since we generally ruin our main code in the `main()` function, we need to declare the previous functions first.  
 
Using a data type for `<datatype>`, will return a data type that has to match the same data in the return statement within the function. So `int sumofnumbers(one, two)` requires a return value of `int` data type, otherwise error. 

NOTE: When passing arrays as arguments, we can't pass the whole array so we need to use a pointer, which is basically `<inputarray>[]`. This basically tells the program to consider the input variable as an array. However, it cannot tell the properties of the array, it only knows that it is an array. So uoften we also pass the length of the array as an input integer alongside the array input in a function so we can use it to find elements in array.

With functions, passing a variable will pass a COPY of the variable into the function, creating a local variable that can't be altered outside the function. However, passing a pointer will pass the address of a variable, allowing global variables since the address in a program neven changes, because the address is the memory location used by a variable. When we pass arrays, C will automatically use the pointer as the input, since the pointer to an array points to the first element in the array.  





## Pointers:  
C is designed to be more memory efficient, which leads to more complex programming. Every variable denoted in a C program is stored in a memory location. The memory location of a particular data variable can be accessed in the form of an address, which tells the program where the variable is in memory. Using the `&` operator on a variable will return its address. e.g.  
```C  
int a = 1;
return %a;
```  
will return something like `bff5a400`.  

A pointer is a variable that has a value of a hexidecimal value. Tpically a point will hold the address of another variable, which means it holds the exact memory location of another variable. However, the variable address the pointer is referencing has to match the data type, e.g. If we are pointing to an integer variable, then the point needs to be defined as an int type, even though the actual value of the pointer is not int.  

The general notation to declare a pointer is `<datatype> *<variablename>;`. E.g. `int *indexval;` would be a pointer to the memory location of any integer variable we allocate it to. Note that this is just for declaring, not using for using the pointer.  

To use a pointer, we can use the `&` operator to set the pointer to the address of another variable. E.g:  
```C  
int a = 3;
int *point;
point = &a;
```  
Now the pointer `point` has the address of variable `a`.  

We can also access the value of a variable using the pointer instead. `return *point` will return the value of the variable that in the same address as the pointer, which would be 3. Note that the asterisk is used to declare a pointer, and return the value of the variable of the current address of the pointer.  

Setting a pointer to `NULL` will render the pointer equal to value of zero, essentially pointing to nothing. Since it is equal to zero we can easily check if a pointer is null or not using an `if` statement.  

Since an addres is a hexidecimal value, we can do numeric operations on it. Doing `++` and `--` will increment/decrement the address to the next memory location, without affecting the riginal location (i.e. The pointer just switches address without changing values of the data at each address). 

By allocatong a pointer to an array, incrementing the address will move the ponter to the next element in the array. This is sueful because this allows us to loop through an array easily by using the pointer, since C has no function for finding the length of an array, which would usually be used to loop through the array in Python or MATLAB. For example:  
```C
int array1[] = {1, 2, 3, 4, 5};
int *pointer;
int i;

pointer = array1;

for (i = 0, i < 5, pointer++) {
    printf("%d", *pointer);
}
```  
Prints 1 2 3 4 5. Since We allocated the entire array to the pointer first, the pointer points to the memory location of the array. Incrementing the pointer goes to the next memory locations, which happens to be the first element of the array, and so on.  

Note that we use `%x` to print an address.  

We can also compare pointer address using the usual comparison operators (e.g. `>=`). This lets us do simpler loops using pointers since we can compare 2 addresses using a pointer and `&` operator.  

An array can hold pointer addresses as their elements. Then we can use each pointer to get the value the pointer is pointing towards, by reversing the address. Since a pointer can point to an array, this means we can hold an array inside a pointer array. Hence, we can store strings in an array. E.g.  
```C  
char *strings[] = {  
 "hit", 
 "yo", 
 "Hello", 
 "eek"
}
```  
Usually we can't store an character array in an array, but because a pointer will hold the address for the first element of an array (and hence, the whole memory location for the array) the pointer can find all elements in an array. So we can simply store the pointer of the string array, in another array. Then we can retrieve the whole array by simply using the pointer. Note that we can only hold string arrays in a pointer array (i.e. Uses pointer notation).  

The main usages of pointers:  
- Pass by reference: Usually we have a variable, it goes into the input of a function, and the function will do something to the variable and return a new value. However, the input variable still exists unchanged sometimes (e.g. We allocated the input variable to local variable in the function), which can increase memory of the program especially with larger values. Instead we can use a pointer to as an input, which points to the address of the variable. allowing us to use the pointer to directly alter the variable. Since the variable will always be located in the same memory location, hence no new variables were made.  
- Arrays: Since a pointer will point to the address of the first element in an array, we can allocate it to a memory location. Then to add elements to the array, we can increment the pointer instead of adding it to the array directly which can have an error as we usually can't change array length once it has been declared  

Note that declaring an array (e.g. `array1[];`) actually sets a pointer towards the first element of that array.  

## Memory:  
C runs a program using this memory model:  
![image](https://user-images.githubusercontent.com/79125281/191619589-2210a4e8-af23-4531-a03a-ffd5bcd6c23d.png)  

## Strings:  
A string is just an array of `char` values. The end of the string is indicated by a null character, which is `\0`, which should be the last elemenet in array.   

Every printable character in C can be expressed as ASCII values. This can be done by converting a `char` value into an `int` value.  

`scanf` can be used to input strings. `fgets` can accept multiple words. Note that using `scanf` we don't need to use the `&` operator to assign the input variable to an address, since a string is an array, hence C will automatically assign an address to the first element of the array.  

Adding `#include <string.h>` will allow us to access special string functions, such as `strcpy`, whihc lets us copy characters from an array to another array.  

Because strings are character arrays, they have to be declared the same way as arrays. So `char array1[5] = "hello"` is the same as doing `char array2[5] = {"h", "e", "l", "l", "o"}`. We can use `array1[]` format to get undefined length, but then we won't know the length of the string which may be useful for alter. 

Rememebr that `%s` will accept whole strings (i.e. An array) and `%c` is for individual characters in a string.  

A string always ends with a `'\0'` character. A character uses single apostrophes, while strings use double apostrophes. The `\0` charcter is useful for looping through the string.

## Structures:  
We can create our own custom data types using structures. The notation for creating a structure is:  
```C
typedef struct {
 <variables>;
} <structurename>;
```
Note that a semicolon is needed at the end of the structure creation. Structures can act as variables themselves, we can assign a variable to use the custom structure datatype. The notation is `struct <structurename> <variablename>;`.  

Each variable in the structure is now a member of the structure. To access a member, use the dot `.` to locate the member in the specified structure (like Tkinter modules). E.g. `structure1.var1 = 4;` would assign the value 4 to the `var1` member in the structure. THis way we can store values in a structure which can hold multiple value of different datatypes.  

However, strings can't be directly added to a member of a declared structure. Instead it has to be copied using `strcpy` into the member.  

We can also assign values to the structure varibale as it is being declared, e.g.  
```C  
typedef struct {
  int myNum;
  char myLetter;
  char myString[30];
 } myStructure ;

int main() {
  struct myStructure blahs = {13, 'B', "Some text"};
}

Output example: blahs.myNum = 13
```  
This method also allow sus to assign string directly into the structure without using `strcpy`, but if we want to change it we would need to use `strcpy`. Also, the order of assigned values has to match the order of variables in the structure.  

## Recursion:  
Recursion is the use of the same function in itself to break down a problem into simpler steps. Usually this is done by using the function itself with it's own returned value, e.g. 
```C  
int add(int x) {
 if (x > 0) {
  return (x + add(x - 1));
 } else {
  return 0;
}
```  
Running this function results a loop where the function keeps decrementing the input number until it is above zero, and return the addition of all those numbers. FOr example, with an input of 5, the iterations would be:  
5 + (add(5 - 1)) --> 5 + (add(4)) --> 5 + (4 + (add(4 - 1)) --> 5 + (4 + (add(3)) --> 5 + (4 + (3 + (add(3 - 1))) --> 5 + (4 + (3 + (add(2))) --> 5 + (4 + (3 + (add(2 - 1)))) --> 5 + (4 + (3 + (2 + add(1)))) --> 5 + 4 + 3 + 2 + 1 + 0 = 15.  
This method can be very efficient, however it is very easy to create an infinite loop with this method.  











## Other notes:  
- Using the link https://homeweb.auckland.ac.nz accesses the H drive in university computers
- You can test whether a variable name clashes with a built in variable or not by using `help <variablename>` (MATLAB)
- You can use up and down keys to cycle through previous commands (MATLAB)
- You can use `...` at the end of line of code to extend it to multiline. Note that the `...` text is omitted as used as the line break, so any other code might be separated improperly (MATLAB)
- MATLAB defaults inputs to integers, not string.
- Euler's number is called by using `exp(1)`, since the `exp` command returns the exponential of *e* to the power of the given value (MATLAB)
- Use `clear` when working on code, but REMOVE the `clear` command when submitting to MATLAB grader (MATLAB)











