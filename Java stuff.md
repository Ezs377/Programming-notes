# SOFTENG 281  

---  

## Introductions:   
Test if assignments can be compiled with Java by using resources tab.  

We utilize command terminal to navigate and compile Java stuff.

Assignments are submitted by pushing to a Github repository.  

For resources:  
https://softeng281.digitaledu.ac.nz/resources/faqs/  

VS code keyboard shortcuts/bindings:  
https://softeng281.digitaledu.ac.nz/resources/vscode-keybindings/  

To compile and run a Java script use java \<filename> where the file has java extension.  

Usually assignment files have a pom, xml, mvnw files in them.  

Maven wrapper is a build tool that gets Java stuff done automatically (?).

## Maven:  
Usually a compiler is needed to compile Java code into bytecode, where javac is the java compiler. Then an interpreter is needed to run the code, which is java for Java code. For Java, we use the following tools:  
- Java SDK (Software Development Kit, comes with interpreter and compiler), used to allow us to write, compile, and run Java code 
- Testing framework (JUnit) to ensure the code runs properly
- Build tool (Maven) to automate the previous tools instead of us doing the compiling/interpreting/etc manually  
- IDE (VS code) to help us write code more easily  
- Version Control System (Git) to keep a history of our code
- Remote service (Github) to store code remotely

The Maven build tool automates a lot of the stuff for us so we don't need to manually compile/interpret/etc the code.  
![image](https://user-images.githubusercontent.com/79125281/222622868-7dcc27b3-bd60-48ee-bb7a-dea476b734f0.png)  
We mainly use 3 commands with Maven: `mvn compile`, `mvn test`, `mvn clean`.  
1. Obtain project files by cloning from Github. These files are mainly going to be edited, particularly `.java` files contained in `src/main/java`. `.java` files in `src/test/java` are test cases for the project.  
2. While working on files we compile them in order to be able to run them for testing. `.java` files can't be executed by themselves so we compile them to generate `.class` files which can be executed by the computer.  
3. `.\mvnw.cmd compile` for Windows to run `mvn compile`. This automatically compiles `.java` files and creates `.class` files automatically. If `BUILD SUCCESS` then compilation was successful, if `BUILD FAILURE` then something went wrong, usually error in code SYNTAX.
4. `.\mvnw.cmd test` for Windows to run `mvn test`. Maven uses the JUnit framework to test the code with a variety of scenarios, usually based on the testing cases in `src/test/java`. If `BUILD SUCCESS` then code will work properly, if `BUILD FAILURE` then something in the code logic is wrong. It will give you the line werhe error occured and etc for fixing the error.  
5. `.\mvnw.cmd clean` for Windows to run `mvn clean`. Cleans up temporary files used during testing and compiling. These files are usually dupmed under the `target` folder, and they can be generated easily so we can delete them to clean up the program. Often it is good to clean before compiling again to ensure compiling runs properly. `mvn clean` is also run before submitting files so it doesn't clutter up files in submission.  
  
---  

## Notes:  
A simple JUnit test script will use an actual value vs an expected value test, i.e.  
![image](https://user-images.githubusercontent.com/79125281/222721693-5eca9bed-ab15-4f55-975a-b55661728ae8.png)  
JUnit files are typicall stored in the test folder.

Computers use binary code to process data. Humans use readable stuff. An assembler converts assebly code into binary code, where assembly code is human-readable code. However, assembly code is very raw and basic, so to be more efficient, we use compilers to convert easier code into either assembly code or machine code (binary bits). A compiler will convert the whole code into machine languange or assembly code, which can then be run anytime. Pros:  
- Higher perfomance for repeated processes
- Less memory required, as a compiled program can remain as is, so we can delete the compiler itself and can still use the compiled program

An interpreter will run code line-by-line and 'interprets' the code one line at a time. This means that the program can only be run by the interpreter, which means we can get standalone programs. Pros:  
- Greater flexibility
- Easier debugging, as as we can acces source code without having to compile it again
- Faster development time

---  

## ACP:  
ACP is used to try class exercises. It is accessed either over website or through VS code. The ACP layout:  
![image](https://user-images.githubusercontent.com/79125281/223634957-a2594ba2-9957-43a7-abdb-a39999605401.png)  
1. Course select  
2. Select project 
3. Select version project  
4. Select file to view  
5. Click run button  
6. View the output  

The editor is in the middle, output is in the small window underneath (like Wing).  

Using VS code requires the ACP extension. Navigating to explorer tab (on the side) will show ACP projects at the bottom of the list. After logging on it can be sued to navigate files.  
![image](https://user-images.githubusercontent.com/79125281/223635481-3972252e-b7ec-4716-9e2b-90168084654c.png)  
Use the download icon to swtich between file versions. 



## Java:  
Java, however, is both a compiler and interpreter. Java code is first compiles the java source files into bytecode, which is then run via the Java Virtual Machine (JVM). Basically Java runs a compiled program via an interpreter, so debugging is easier, but we still need to compile again to fix mistakes.

Make sure code is indented properly.  

CNAME class names: It should be written in UpperCamelCase. UpperCamelCase notation is basically no spaces, and every word has 
the first letter capitalised. Usually a word is defined as a word separated by either a space or hyphen in the original text. Remove all punctuation.  
E.g. "hello world" becomes "HelloWorld" in UpperCamelCase. Also note acronyms are also ignored, e.g. "USB" = "Usb".  

Class names should be nouns or noun phrases. Adjectives can be added.  

A JUnit test class (a method in a class used for testing) is usually defined by ending the name with Test, e.g. "CarTest".  

MNAME method names: it should be written in lowerCamelCase. The notation is similar to UpperCamelCase except the first letter is always lowercase. No puncutation.  
E.g. "hello world" = "helloWorld".  

Method names should start with a verb, e.g. "runSuperMario"

VNAME variable names: Should be written in lowerCamelCase. Shouldn't be single-character names except for throwaway variables (e.g. Loops). 
Variable names representing fixed (variables initialized once) and static (variables in a class that don't change with a new instance) variables. 
Names for these variables should be all capitals and separated with underscore. e.g "MAX_VALUE".  

Plural names are used to describe a collection of data (e.g. Objects), such as lists.  

COMM code comments: Comments are done using `//` for single line and `/*  */` for multiline. COmments should not be too much or too little  

When declaring instance fields (variables), use `private` instead of `public` as this adds extra security. Then you can use `public` for instance variables instead of directly declaring instace fields and using publicly. E.g.  
``` Java  
private double x;  

public double getx() {
  return x;
}
``` 
This method is using a getter/setter to obtain variable values instead of declaring publicly. 

PNAME package name: Put Java-related classes in the same package (similar to folders). Packages should only be named with lowercase only, e.g. `mypackage`. Packages follow the directory path, e.g. To find the class A.java in `src/main/java/nz/ac/auckland/se281/A.java` path, for package we use `package nz.ac.auckland.se281;`. Remember that the package should be located in the Java folder so that is ommited from the package path. Basically collect all Java classes and put in the same package, which is located in Java src folder.  

ORDER of elements in a class:  
Elements in a class should be ordered in a specific way:  
1. Package, imported via `import`
2. Imports, imported from packages
3. Class declaration, creating the class(s)
4. Inner classes
5. Static fields
6. Static methods
7. Instance fields
8. Constructors
9. Instance methods  

Javadocs are code comments that describe secitons of the code, typically multiline. For methods (for 281 only) the JavaDoc will have some sentences desribing the method's function, and describe all parameters (@param), returns (@returns), and throws (@throws) for the method (which are the variables contained in the method). VSCode can automatically a JavaDoc template that has a blank comment with a list of parameters, returns, throws which can be filled out. AN example of JavaDoc:  
![image](https://user-images.githubusercontent.com/79125281/223259949-ee8e54a3-1289-4b7f-a7bc-a8041b43b00a.png)  

**Java basic structure:**  
The basic structure of a Java program:  
![image](https://user-images.githubusercontent.com/79125281/224213016-e747ea01-1892-470c-b142-6f1e9e9edf49.png)  
We need at least:   
- At least 1 source file (\*.java files)
- At least 1 class defined in the source file
- At least 1 method defined in the class
- At least 1 statement in the method

For a simple `hello world`:  
``` Java  
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }  
}  
```  
Some notes:  
- The source file is `Main.java`  
- The only class is defined as `Main`, uses curly brackets {} to close the class    
- The only method is defined as `main`, uses curly brackets to close the class
- The only statement is `System.out.println`  
- System is a built-in Java class and `out` is an instance of the `System` class, rendering it a member of the `System` class. Then we can acces the `println` method from the `out` instance  
- 

### Basics:  
Apparently the syntax for Java is very similar to C in syntax.  
All statements have to end with a semicolon `;`
The class name should match the filename, as the compiler converts a java file to a class file.  

Classes are 'blueprints' that contain instructions on how to create an object. 'objects' have the properties built by the 'class', i.e. An object is a class instance. A method defines the operations/instructions within the class, that the object uses as its properties.   

`System.out.print("string")` can be used to print to display, but `System.out.println("string")` moves the cursor to a new line each time it is run.  

A variable in a class is referred to as a class attribute. A function in a class is referred to as a method.

When printing out numbers, it is not necessary to put them in quotation marks. It is also possible to perform calcualtions directly within the `println()` method, e.g. `System.out.println(4 + 2);` prints out 6.  

Java can use different types of variables (note that Java is case sensitive):  
- `String`: Text and characters, uses double quotation marks to identify `String` values
- `int`: Whole numbers
- `float`: Numbers including decimals
- `char`: Stores single characters, uses single quotes to identify `char` values
- `boolean`: Stores either `true` or `false`, doesn't use quotation marks

To create a variable, use `type <variablename> = <value>;`. It is also possible to declare the variable type first, then the value later, e.g. `int x;`. THe most important part is the type.  

The `final` keyword is used to 'lock' a variable, so that trying to assign a new value to that variable results in error.  

Keywords can be applied to classes, methods, constructors, attributes to define their properties, or simply by themselves. Keywords are reserved by Java and cannot be used to name other things. Keywords can also be statements.  
- `abstract`: Is used for classses and emthods. Prevents a class from creating an object, and only abstract methods work in abstract classes. An abstract class must be inherited to use it to create objects.
- `assert`: is used for deugging purposes
- `boolean`: For variables, can only store true or false
- `break`: Breaks out of a loop, used by itself within a loop
- `byte`: For variables, can only store values between -128 to 127
- `case`: Marks a block of code in a `switch` statement
- `catch`: Runs if a `try` statement fails (i.e. try and except --> try and catch)
- `char`: For variables, can only store a single character
- `class`: Defines a class
- `continue`: Goes to the next iteration of loop, used by itself
- `default`: Specifies the default case for a `switch` statement if no cases match
- `do`: Used with a `while` loop, it makes the loop run at least once before checking `while` conditions
- `double`: For variables, can only store double values (decimal values)
- `else`: Used in `if` statements and etc, used by itself
- `enum`: Creates a special 'class' that holds public, static, final variables, essentialy creating a 'class' with constants
- `exports`: Export a packgae with module (something to do with modules)
- `extends`: ALlows a class to inherit attributes and methods from another class, e.g. `class <classinheriting> extends <classtoinheritfrom>`
- `final`: Will 'lock' the value so that trying to assign a new value will cause an error  
- `finally`: Used with `try` exceptions, executes code regardless if there was an exception or not. Used along `try` and `catch` statements
- `float`: For variables, can store decimal values, greater accuracy than `double`
- `for`: Create a `for` loop
- `if`: Creates `if` statement
- `implements`: Implements an interface with class, i.e. `class <classname> implemenets <interfacename>` 
- `import`: Imports a package, class, or interface
- `instanceof`: Checks if an object is an instance of a specific class or an interface, returns `true` or `false`
- `int`: For variables, can only store whole number values
- `interface`: A special abstract `class` that can hold methods with empty 'bodies' (i.e. No code in methods). Difference between abstract classes is that abstract classes can only be inherited once, while you can implemenet multiple interfaces
- `long`: For variables, stores whole numbers only at a greater range than `int`
- `module`: Declares a module
- `native`: Specifies that a method is not in the Java source file and potentially written in another programming language 
- `new`: Creates a new object
- `package`: Declares a package, which is a group of classes
- `private`: Only allows the declared class to use the attributes/methods/contructors, prevents other classes from using them
- `protected`: Only allows the declared package/subclass to use the attribute/method/constructor
- `public`: Allows other classes to access this value
- `requires`: Specifies requried libraries for a module
- `return`: Returns value from a method, indicates the end of a method
- `short`: For variables, only stores whole numbers at a smaller range than `int`
- `static`: Allows methods and attributes to be accessed without creating an object of the class, i.e. Variables are shared globally instead of being reset for each new instance
- `strictfp`: Restricts the precision and rounding of float calculations
- `super`: Refers to a superclass object, i.e. Parent class
- `swtich`: Statement, allows to have different conditions run different code blocks, basically a better version of doing multiple `if` statements
- `synchronized`: Used to prevent multithreading
- `this`: Refers to the current object/constructor
- `throw`: Creates a custom error
- `throws`: Indicates what exceptions can be thrown by a method
- `transient`: Specifies an attribute is not part of an object's persistent state (whatever that means)
- `try`: Statement, attempts to run code, if exception is caused, then run the alternative code using `catch`
- `var`: Declares a variable
- `void`: Specifies that a method should not have a return value 
- `volatile`: Indicates an attribute is not chached in thread, instea dit is read from main memory
- `while`: Creates a while loop

Note that `String` is not considered a keyword in Java, because it is actually an object.  

To combine variables and text to print, use `+`, e.g. `System.out.println("Hello" + <var1>)`.  
It is also possible to assign multiple variables in one line, like `int x = 5, y = 7, z = 10` assigns `int` values to these variables.  
`int x, y, z`, then `x = y = z = 50` assigns the same value to all variables  
Java uses the same data types for programming. A primitive data type only specifies the size and type of variable, e.g. `int`.  
Note that for `long` type, the number should end with an `L`, e.g. `long x = 10003L;`. For floats, end with a `f`, and for doubles end with a `d`.  
You can also use `e` to describe a power of 10, e.g. `double x = 2.4e12f;` will give 2.4\*10<sup>12</sup>. Lowercase or uppercase doesn't matter.  
A `char` uses single quotes (' ') and `String` uses double quotes ("  ")  

A non-primitive/reference data type generally refer to objects. Primitive data types are already defined by Java (e.g. `int` is whole numbers only) while non-primitive data types (i.e. Reference type) are created by the programmer (except for `String` which is a special case). Examples of non-primitive data types are `Class`, `Interface`, `Array`, etc.  
Also, primitive data types use lowercase letters, non-primitive data types start with uppercase.  

Note that a class is a reference type, so it can be for code that uses a type, such as ArrayList.

Type casting is converting a primitive data type to another. Widening casting is going from smaller to larger data type (which can be done automatically) and narrowing casting is going from larger to smaller data type (has to be done manually).  
![image](https://user-images.githubusercontent.com/79125281/226099135-00ca80b4-e23c-49b1-9532-5716fe3256d0.png)  
Widening casting is simply done by assigning the new keyword to the variable, e.g. `int x = 0;`, then `double y = x;`.  
Narrowing casting is done by putting the keyword in brackets before the variable, e.g. `double x = 9.78d;` then `int y = (int) x;`.  
Note that when converting from `decimal` to `int`, Java just drops the decimal, so any values after decimal is ignored and no rounding, e.g. 6.999 = 6.  

Java operators are the same as usual, e.g. `++` = increment, `%` = modulus. There are also some trickier assignments such as `x >>= 10` which not yet.  
Remember that `&&`, `||`, `!` are AND, OR, NOT operators as well  

### Strings:  
The length of a string can be found using `length()` method, e.g. `x.length()` gives length of string `x`.  
`toUppercase()` and `toLowercase` convert stirngs to uppercase and lowercase respectively.  
`indexof("<string>")` returns the index of the first occurence of the specified text within the string (the index given is for the first character)  
Further string methods:  https://www.w3schools.com/java/java_ref_string.asp  

String concatenation is done using `+`, e.g. "icky" + "dicky" = "ickydicky". The `concat()` method is also available, like `<string1>.concat(<string2>)`.  

Note that using `+` to combine a string and number will result in a string overall, e.g. `4 + "hello" = "4hello"`.  

Backslash cancels effects as usual. `\n` and the like are the same, with additional stuff. `\b` performs a backspace, `\r` moves cursor to back to the start of the line, `\f` is rarely used, it prints onto a new page (for old printers). `\r` and `\f` are barely used. 

### Math:  
Java has a `Math` class that holds useful methods, e.g.  
- `Math.max(x, y)` returns the highest value between `x` and `y`  
- `Math.min(x, y)` returns the lowest value between `x` and `y`
- `Math.sqrt(x)` returns the square root of `x`
Full lsit of math methods:  https://www.w3schools.com/java/java_ref_math.asp  
Note that since they are methods they have to be called from the `Math` class.  

## Statements:  
**if**:  
The `if` statement is written like:  
``` Java  
if <condition> {
  <code>
}
```  
`else` is implement like in C, between the curly brackets, i.e.  
``` Java  
if <condition> {
  <code>
} else {
  <code>
}
```  
Same with `else if`  

However, there is a thing called ternary operator, which can be used to shorten `if else` statements. The syntax:  
`<var1> = (condition) ? (runifconditionistrue) : (runifconditionisfalse);`. Essentially, you can assign a value to a variable based on a condition (`if` statement). It is possible to extend this infinitely (although it gets messier). The important part is that the `?` separates the condition and the output, the `:` separates each output. It can thought of as that the `?` stands for the `if`, and each `:` stands for `else`. Stacking `if else` looks like:  
![image](https://user-images.githubusercontent.com/79125281/226101343-2372cc07-65fe-48d4-a12f-b86bcadff29c.png)  
Basically, `?` is the `if`, and `:` is the `else`.  

**Switch**:  
The `switch` statement can be used as an alternative to ternary operators and multiple `if else` statements. The syntax:  
``` Java  
switch(expression) {
  case <value>:
    <code>
    break;
  case <value2>:
    <code>
    break;
}
```  
Often the `break` is added at the end of each case for efficiency, to prevent checking other cases. It is also due to fall-through, where if we don't include a `break;` then if a case is matched it will also run all cases after that case as the condition is now true.  
The expression value can be most data types, but the cases have to match the data type of the expression.  
`default` is the code that is run if no cases match, optional.  

**Loops:**  
`while` loop:  
``` Java  
while (condition) {
  <code>
}
``` 
The `do while` loop is a variant of the while loop that will run the code once before checking conditions, so it will run at least once.  
``` Java  
do {
  <code>
}
while (condition);
```  
Note that the `while` is now simply a condition and has no curly brackets.  

`for` loop:  
``` Java  
for (<initialcondition>; <condition>; <conditionafterloop>) {
  <code>
}
```  
Just like in C. Note that the `<condition>` is the same as `if`, and `conditionaafterloop>` keeps the loop going until it meets `<condition>`.  

The `for each` loop is used specifically with arrays to cycle through each element.  
``` Java  
for (<type> <variable>:<array>) {
  <code>
}
```  
Essentially an easier way to use the for loop to go through an array, similar to `for i in <list>` in Python.  

**Arrays:**  
Declaring an array:  
`<type>[] <arrayname> = {<item1>, <item2>, ...};`  
Accessing using index is done using square brackets, e.g. `x[0]` gives first element in `x`.  
Array elements can be directly changed using index.  
`length` is used to find length of array, e.g. `x.length`. Note that `length` is a property, not a method here.  

To loop through an array use `for` using array length or `for each` loop.  

A multidimensional array is created by adding an array in an array, e.g. `int[][] x = { {1, 2, 3}, {4, 5, 6} };`  
To index through a multidimensional array treat it as a matrix, i.e. 
``` Java  
{ {1, 2}, {3, 4}, {5, 6, 7} }

    1 2
=   3 4
    5 6 7
```  
And the index uses `[x][y]` where `x` = row, `y` = column. Note that the arrays do NOT have to match length, the index notaiton simply finds the x row first then the y element of that array in row x.  

Note that because we need two saure brackets to index through a multidimensional array, we need to pass values to both brackets, so looping through a multidimensional array requires 2 values (usually done by using 2 `for` loops).  

### Methods:  
Methods are now used to refer to 'functions' in Java. Since Java uses Object Oreitned Programming system (OOP) then by default we use classes for everything, so functions within classes are called methods (since they cannot run by themselves now). A function can run by itself, but a method can only be called from the class. Methods a similar to functions in the way they work but because they are in a class there are some differences. 

Methods are commonly declard in a class using   
``` Java  
<keywords> <methodname>(<parameter1>, <parameter2>, ...) {
  <code>  
}
```  
E.g.  
``` Java  
`static void myMethod(int x) {`
  System.out.println(x);
}
```  
Like functions, the returned value of a method can be stored into a variable, e.g. `int x = addermethod(1, 4);`  

Method overloading involves declaring the same method name but with different arguments/keywords so instead of declaring multiple methods that do similar functions we ovelroad one method. This allows us to use 1 method for the same tasks, but with different input arguments. Methods can have the same name if the number of parameters, or type of parameters, is different.  
![image](https://user-images.githubusercontent.com/79125281/226173096-992ff352-3575-4628-b272-474997a781c6.png)  
Instead of doing another method that adds `double` values together, we overload the `int` adder method to allow `double` input/output so we can add `int` and `double` values using the same method.  

The scope of variables refers to the code 'region' they can be accessed. Generally, a varibale declared in a method can be accessed anywhere within the same method. A block of code (code inside some curly brackets), tyypically used in statements, if a variable is created in a block of code then it can only be accessed within the same block of code, i.e.  
``` Java
{ 
  x = 12; 
}
System.out.println(x);
```  
This cannot print out `x`. Note that it is possible to just use curly brackets to create a block of code, but usually not recommended (might have potential for testing).  

Recursion involves calling a method in itself. Be careful as this could create endless loops, something like  
![image](https://user-images.githubusercontent.com/79125281/226219171-dcb1ebf3-ae2c-4d62-baf1-6ed76e9aa6bf.png)  
Where the `sum` method will call itself if `k` is more than zero. Note that in the recursed `sum` method, our input is `k - 1` so that it decrements `k` and ensures that there is no endless loop. The `else` statement ensures the recursion loop stops if `k` is 0. This method will add up all the numbers in a range, i.e. Factorial.  
When doing recursions a halting condition is needed to prevent infinite loops.  

**Memory:**  
The stack is where temporary values are stored, such as variables in a method. Method variables are discarded once the method finishes execution (e.g. Reaches a `return` statement). However, object instances are located in the heap, and can be shared across methods. 

When dealing with equality, primitive types (`int`, `String`, etc) are easy to compare, same types will be exactly the same if the values are the same. But reference types (objects) are different when dealing with equality. 

Identity (or reference equality) is when two instances have the same reference pointer, so utilise the 'same' memory spot in the heap. But even if the values are the same it will not be considered identity equal as each instance is located in different spot in the heap even if the values are exactly the same and same type. Basically identity is when we have reference variables pointing to the exact same instance in the heap. The same address of the instance is stored in different variables. This usually occurs when you check 2 reference variables using `==`, it checks for identity not value of variables. 2 variables don't have the same identity when they do not share the same address.  

In order to compare value equality, which is referred to as simply equality, we have to develop a connection between values of instances that we could treat as 'equal', such as translation between two strings, e.g. "red" and "merah" are different values, but based on human thinking they meant he same thing in different languages. Equality, or object equality, can be determined by the programmers themselves via instance methods.  

An instance method is a method that belongs to instances (objects) of the class, not the actual class. In order to use an instance method it must be accessed through the object, e.g. `object1.method1();`. Static methods on the other hand can be accessed directly through the class, e.g. `class1.method2();`.  
For creating an instance method for comparison, we can craete a method that takes an object as a parameter (using type `Object`(?)). Also, a hashcode improves the data structure of a Java program, and 'equal' values of objects should also return the same hashcodes (more on this later).  

## Object Orientated Programming (OOP):  
A class acts as a 'template' for objects, which instances of a class. E.g. An apple (object) is an instance of a fruit (class).  

Attributes are variables within the class, and methods are functions within the class. Often creating an instace of a class, the instance will inherit these attributes and methods, so they can use the same variables and functions from the class, although this depends on the attributes and functions.  

To create a class:  
``` Java  
<keywords> class <classname> {
  <code>
}
```  
Note that a class have the same name as the filename, and typically only 1 class every file  

An object (or instance of a class) is created by `<classname> <object name> = new <class>`. THus now we can use the object for stuff, such as calling methods from the object or values.  

To use multiple classes we use multiple files, ideally located in the same folder. Usually this is done for better class management, such as combining attributes in one class and all methods in another, and creating the objects in another class. If done correctly, all that's simply needed is to use the same create object notation to create an object from another class.  

**Class attributes:**  
An attribute is a variable in a class. Because this value is 'passed' down to an object, the variable is inherent to the class hence it is an attribute. Fields is another term for attributes. Accesing attributes uses dot on object, e.g. `object1.x` gets the attribute `x` from the object `object1`.  

Once an attribute is inherited it can be modified by the object itself, but it is unique to that object only. The class can have an attribute, or an attribute with value, but when object is created you can modify the attribute in the object to whatever.  

However, the `final` keyword on class attributes prevents them from being overriddin in objects, and throws an error when attempting to do so.  

Remember that attributes in an object are only unique to the object. Class attributes serve as templates for object variables, they aren't fixed values unless you specify them to be fixed constant values.   

**Class methods:**  
A `static` method can be accessed without creating an object first. Some uses are calling the method from another class or calling method in another method.  
A `public` method can only be accessed by creating an object of the class first, then calling the method from the object.  

**Class contructors:**  
A constructor is a special method (and thus same notation) that is used to initialize objects. A constructor has to have the same name as the class it belongs in. A constructor can be used to set initial attributes of an object when creating an object. Note that this occurs only if the attribute is defined as a variable type only in the class, e.g. `int x;` which sets the variable to any value, which is where the constructor sets the initial value of `x` for any objects created using the class.

Basically a constructor sets initial conditions of a class without having it set by its instance, i.e. The object comes with its own attributes.  
Constructors can also be passed with arguments allowing users to set initial values of the object, done by adding parameters to the constructor.

The notation of constructor is `<classname>(<parameters>) { <etc code> }`. Constructors must be void have no return value. 

Arguments inserted into parameters of a constructor can be used to initialise values of the constructor, e.g.  
![image](https://user-images.githubusercontent.com/79125281/227386291-dd2b446b-3846-45b9-9637-efe6b01fb352.png)  
Which has useful properties such as setting different initial attributes of objects depending on input.  

Multiple constructors can be used in a class, but they have to differ by their arguments. Multiple constructors either need different names or different arguments to differentiate from each other. The constructor called when creating an instace depends on the arguments used, e.g.   
![image](https://user-images.githubusercontent.com/79125281/232030538-3dc82dbd-2eb7-4564-8b38-01bc2ca2ba86.png)   
Calling `Colour3()` when creating object uses the no parameter constructor, using `Colour(<value>)` when creating object uses the 1 parameter constructor, and etc.  




**Modifiers:**  
Modifiers are special keywords used to modify classes, methods, attributes, constructors. There are 2 types, access and non-access modifiers.  
Access modifiers:  
- `public` = For classes, it allows other classes to access this class. For methods/attributes/etc, it makes it available to all other classess
- `default` = The code is only accesible in the same package. `default` is automatically used when a modifier isn't specified  
- `private` = For methods/attributes/etc, can only be accessed in its own class  
- `protected` = For methods/attributes/etc, can only be accessed in the same package and subclasses (more on this later)

Non-access modifiers:  
- `final` = For classes, it means it cannot be inherited by other classes. For methods/attributes/etc, it means they cannot be overriden/modified once set, and instead outputs error    
- `abstract` = For classes, it means that the class cannot be used to create objects (inheritance related). For methods, can only be used in abstract class (inheritacne related), cannot be sued on attributes and etc  
- `static` = For methods/attributes/etc, belongs to the class rather than the object, so it is shared across everything (i.e. Global value) regardless of how many instances created   
- `transient` = For methods/attributes/etc, they are skipped when doing serilization of objects, which is similar to 'saving' them for export or etc. `transient` stuff is not serialized  
- `synchronized` = Methods are only accessed one thread at a time. Usually used to stabilise code that involves multithreading  
- `volatile` = The value of attribute is not cached on thread and is read from the 'main' memory instead (don't use) 

Note that `static` stuff can be accessed without making an object of the class first. WIthout `static` we can only use a method if an object is created first.  

**Encapsulation:**  
Encapsulation is the act of mkaing code secure by hiding stuff from the user. This is done by setting stuff using `private` modifier and using `get` and `set` methods to obtain and update the `private` stuff.  

This is mainly used to allow classes to access `private` stuff from other classes, which usually wouldn't be possible without getter and setters.  

A getter method allows us to obtain a value from a private attribute/method from a class. The syntax is `<modifier> <type> get<namecapitalised>`. Note that the attribute/method name we want to get has to be CAPITALISED. E.g. If `private String var1` then the get would be `public String getVar1`.  

A setter method allows us to modify a private attribute/method in a class. The syntax is `<modifier> <type> set<namecapitalised>(<type> <vartoset>)`. Using the `this` keyword  allows us to set an attribute on the object instead of the class, e.g. `this.var1 = <vartoset>`. 

Using `this` as a classname for attribute/method calling refers to the object instead of the class itself. Since classes usually represetn blueprints for objects, this allows us to generalise code that works for each object instead of hard-coding. It also lets us differentiate between vairbales with the same name within the class. E.g.  
![image](https://user-images.githubusercontent.com/79125281/228080590-631a50a9-da1a-49f9-9ed2-b1a460a7691a.png)  
Here the class attribute `x` is shared across the whole class (`default` attribute). The constructor takes input `x` as well, but this isn't the class attribute. Using `this.x = x;` lets us tell the difference between the class attribute `x` and the constructor parameter `x`. The same example with rewording:  
![image](https://user-images.githubusercontent.com/79125281/228081121-8350da69-211e-4bcf-9703-8daf390827c6.png)  
Note that creating an instance of class Main (object) gives it the attribute of `y = 5`, which is set by the constructor by using the parameter input `5`. Basically, this code creates class attribute (which becomes an object attribute for created objects), uses a constructor to set the class attribute, and creates an instance of the class (object) with input parameter 5, which is set as the object attribute value of the created object. 

Basically, `this` refers to the created object itself, not the class.  

The setter method can use `this` to set the value of an object without directly accessing the class attributes of the object.  
![image](https://user-images.githubusercontent.com/79125281/228082257-1d3d8497-3888-4562-ab1e-05e8c0b60d5b.png)   
If we created an object with this code then the `this.name = newName;` would set the class attribute `name` for that object only., not the whole class so the class is unafffected, e.g. Using another file to call this code:  
![image](https://user-images.githubusercontent.com/79125281/228083192-79d35007-d05e-46a1-b181-865d3d5c96d6.png)  
Note that the `setName()` code was called in the main program to set the value of `name` and `getName()` method was used to print the value of `name`.  

**Packages:**  
A package in Java is a group of related classes, can be thought of as a folder (package) containing class files (classes) within an entire directory (project folder). Packages make organization simpler within a project. Java has multiple in-built packages that can be imported via `import`. The `import` command can import a single class from a package by specifying its name (e.g. `import package1.subpackage1.classname;`) or the whole package by using '\*', i.e. `import package1.subpackage1.\*;`  

These can also apply to custom packages as well. Using the `package` keyword at the start of the file defines the package name, allowing us to create our own packages. 

**Inheritance:**    
Inheritance is using a 'base' class (also referred to as an abstract class) to create similar classes with the same attributes and methods. The subclass is the class that inherits from another class, while the superclass acts as the parentclass that subclasses are inherited from.  

`extends` is used to inherit from a superclass, i.e. `class <subclass1> extends <superclass1>`. Note that the `protected` modifier can be used to only allow access to an attribute/method by subclasses as well as package.

`final` keyword modifier is used to prevent inheritance on a class, i.e. `final class <classname>`. 

**Polymorphism:**  
Polymorphism is similar to inheritance, in which polymorphism is using inherited methods to perform different tasks. We can make inherited methods do different things in each subclass, even if they share the same name as the method in superclass.  

**Inner classes:**  
Classes can be defined with another class for better organization. They can be called by using dot to refer to the inner class. However inner classes can be private or static. An advantage of inner classes is that they can access attributes and methods from the outer class. 

**Abstraction:**  
Abstraction is hiding certain details of the code to the user and only showing desired information to the user. Abstraction is achieved by using abstract classes or interfaces. An abstract class cannot be used to create objects, it must be inherited (basically the same as getter/setter for attributes). An abstract method can only be used in an abstract class, and doesn't have a body. The abstract method body is provided by the subclass that inherits from the abstract class.  

Basically, an abstract method has no body, the body is instead defined in the subclass that inherits frmo the abstract class. So we can utilise the same named method for different purposes, i.e. Polymorphism.  
![image](https://user-images.githubusercontent.com/79125281/231347995-5ce1b1a7-ac44-4490-a83c-6189de3173a0.png)  

**Interfaces:**  
An interface is a completely abstract class that only contains empty methods, using `interface` instead of `class` to define itself. These are inherited by a subclass and defined within the subclass using `implements` instead of `extends`.  
![image](https://user-images.githubusercontent.com/79125281/231350450-de05c20d-8202-41eb-a22b-e4996d2ca859.png)  
Interfaces cannot be used to create objects, interface methods don't have a body, and implementing an interface requires you to override all of its methods in the subclass (basically define every method from the interface).  

You can't inherit from multiple superclasses, but it is possible to implement from multiple interfaces, e.g.  
![image](https://user-images.githubusercontent.com/79125281/231350781-39e7dafa-4521-4e17-b802-e6c38b56af7f.png)  

**Enums:**  
Enums are a special class that only hold constants. Constants are similar to `final` variables, in that they cannot be changed after definition. Use `enum` to defin an enum class. The constants in an enum class don't hjave to be defined with specific keywords, instead they can be expressed as is, e.g.  
![image](https://user-images.githubusercontent.com/79125281/231443182-ceb6314a-810c-4e50-ad9e-a1e96fd64919.png)  
Calling `Level.MEDIUM` will get the value `MEDIUM`.  

Enums are usually used in `switch` statements as cases. Since the constant is expressed as is we don't need to worry about using strings or etc.  

The `values()` mehtod returns an array of all enum constants in the enum class, which can be used to loop through the contents of an enum. Notation is `<enumname>.values()`.  

Enums are similar to classes in the way they function but all declared attributes and methods in an enum class are defaulted to public, static, and final. Enums can't be used to create objects or extend classes, but can be used to create interfaces. 

Constants are denoted with full capitals. They can either be variables with the `final` keyword (should be defined with all capitals) or using `enum`.  

We can create a constructor within the enum class that defines a value to each constant, e.g.  
``` Java  
enum Transport {
  PLANE(200), CAR(100);
  int speed;
  Transport(int s) {
    speed = s;
  }
}
```  

Which allows us to get values of `s` for each constant `PLANE` and `CAR` by doing `Transport.CAR.speed` which retrieves the value of `speed` from constant `CAR`.  

The `ordinal()` method gieves the 'index' of the constant based on the order they are declared. In the previous example, `PLANE` would be 0 as it was the first constant declared. 

**User input:**  
User input can be done using the `Scanner` class, which is imported via `java.util` package. Create an object using `Scanner` class and utilise the object for user input shenanigans.  

The `nextLine()` method in `Scanner` is used to read a String type from the user input. It can be binded to a variable to allocate the read string into the variable, e.g.  
![image](https://user-images.githubusercontent.com/79125281/231446659-0d9750ff-5f5b-472e-b157-e877146b2f10.png)  
Other methods include `nextBoolean()` and `nextFLoat()` which read Boolean and FLoat inputs respectively. Note that if input cannot be read using the specified read method then error occurs.  

**Date and time:**   
The `java.time` package can be imported to utilise date and time API. There are multiple classes within the package, including `LocalDate` which represents a date in YYYY-MM-DD form, and `LocalTime` which represents time in HH-mm-ss-ns form.  

The `LocalDate.now()` method from `LocalDate` class can return the current date using the local date on device. Using `now()` method from `LocalTime` class brings up the current time instead.  

`DateTimeFormatter.ofPattern("<desiredpattern>")` is a method using `DateTimeFormatter` class that formats the output date/time based on the given string, e.g. `"HH-mm-ss"` will omit nanoseconds from the time output.  

**Arraylist:**  
Arraylist is a resizable array in Java. Typically Java arrays are fixed and cannot add/delete elements once made. Arraysize allows modular expansion/deletion. Arraylist is imported via `java.util` package.  

Notation is `ArrayList<Type> <arrayname> = new ArrayList<Type>();`  

A single Arraylist can only store the same defined type (note that classes can also be a type, so it can store objects of that class).  

Methods:  
- `add()` is used to add elements to the arraylist. It is done by doing `<arrayname>.add(<element>);` where `<slement>` is the same defined type as the arraylist contents  
- `get()` is used to retrieve elements from arraylist using index number. Same as `add()`, it is `<arrayname>.get(<index>)`  
- `set()` is used to modify an element based on index number, notation is `<arrayname>.set(<index>, <element>);`  
- `remove()` deletes an element by index number, same notation as `get()`  
- `clear()` removes all items from arraylist, no arguments required, usage is `<arrayname>.clear();`
- `size()` gives number of elements in the array, useful for looping. Same notation as `clear()`

Note that ArrayList only accepts objects as Types, so to define an int or float arraylist you need to use equivalent wrapper clases for those types, e.g. int = Integer type.  

### OOP notes:  
**Inheritance:**  
We can use `extend` on classes that are located in the same directory as the parent class. Using the `super` keyword allow us to 'copy' all constructors from the parent class into the subclass, so all we need to do in the subclass is define methods. However, `private` attributes and methods won't be inherited, only `public` ones. 

`protected` allows subclasses to acces the parent fields without allowing access for other classes, essetnaily containing the attributes/methods within the parent/subclasses.  

With subclasses we can choose to override atteributes/methods from the parent class or inherit them as it is by specifying the method/attribute. The `super` keyword basically means call from parent class. E.g. `super.method1();` will use `method1()` from the parent class, inheriting it into the subclass. However, we can also write our own `method1()` in the subclass which overrides the `method1()` in the parent class, so the subclass can do something different. It is also possible to override a method while also using the original method, e.g. Using `super.method1();` in `method1()` of the subclass lets us 'override' the `method1()` of the parent class, but also allows us to use the `method1()` from the parent class, yet we can add extra things to `method1()` of the subclass, 'extending' the method from the parent class.


The `Object` class is a implicit (hidden) class that is the parent class of all classes in Java by default. It can be used to refer to an object where we don't know the type, e.g. `Object obj1 = returnmethod1();`.  

`Object` class has methods as well, most of which are commonly used in common scenarios, such as the `equals()` method. Essentially, if we create a class that isn't used to extend other classes, then that class is inheriting the `Object` class by default. Every created class is a `Object` type.  

An abstract class can hold either abstract or non-abstract methods, but any abstract methods will have to be defined in the subclass in order for it to work.  

You can customize subclass constructor with other variables along with the `super()` construction as long as they are not defined in the parent class and have been initialized in the subclass itself. Typically this also means that the parent class will have custom values for these particular varables instead of simply doing `this.var1 = var1;`, instead we use `this.var1 = 0;`.  

## Design patterns:  
Software design patterns are certain formats to arranging code that can make it easier for various things, such as team collaboration or implementing updates. 

Creational patterns create instances while hiding creation logic (e.g. `<instance> = new <classname>`) instead of directly using the `new` operator. Gives more flexibility when deciding which instances to be created.  
Structural patterns utilises inheritance to compose interfaces and define ways to create objects with new functionality.  
Behavioural patterns deal with communication between objects.  

### Creational patterns:  
**Factory (Creational) design pattern:**  
One of the most used design patterns. For example, if we want to 'add' more instances that have similar functions, instead of creating a new instance of that specific class each time and binding to a `case` statement, we can utilise an interface to define the class that makes the instance. implement the interface for each additional ibject you want (that has similar code to each other but different properties). Then we can use `case` to return a new instance of a specific instance that had implemented the interface. Essentially, going from this to this:  
![image](https://github.com/Ezs377/Notes/assets/79125281/b5a832e5-d544-4dce-856e-7fa2ee5dc9c2)  
This one means we need to repeat the same code over and over for each new coffee type.
![image](https://github.com/Ezs377/Notes/assets/79125281/b6957074-1e34-461b-b7ce-aa918402099b)  
This one is similar but less code used to repeat the coffee type creation. 

**Builder (Creational) design pattern:**  
This deals with the issue of creating many prerequisite variables when initialising, and when setting the constructor of a class, e.g.  
![image](https://github.com/Ezs377/Notes/assets/79125281/aea49766-4b88-4e82-8349-d6e3275ce0f2)  
Can be easy to mix up variable names and adding more variables gets tricky.  

Instead we can separate essential variables with optional variables (variables that might not be used in some instances that use the same class). Use a 'builder' class that is a `static` inner class which holds the construction logic, to separate essential and optional variables. The builder class has a constructor only for essential variables, and setter methods for optional variables. A `build()` method combines everything and returns as an instance.  
![image](https://github.com/Ezs377/Notes/assets/79125281/a2e4a8a9-df81-4914-b7be-0d5fe6e1f74b)  
![image](https://github.com/Ezs377/Notes/assets/79125281/43ce83e3-1d43-4500-9757-c367f38c8841)  
In this example, we set the optional variables only via the methods (setter methods). For the `size` variable, this is essential, so it is defined by passing an argument into the builder method (this is also the same for other essential variables). Otherwise for optional variables, we have set default values for them, the builder method only changes this value for later. Note that all builder setter methods (optional variables) return `this`, i.e. The builder itself. In the main class, we can define constructor:  
![image](https://github.com/Ezs377/Notes/assets/79125281/4470dfeb-e881-4881-a715-2f8e182602c2)  
Note the consutrctor is set to `private`, but because it's an inner class it can be called by the main class. Then to create instances, we can do:  
![image](https://github.com/Ezs377/Notes/assets/79125281/b3cc4884-ca0f-40fa-837b-03da277f3bfc)  
This is a series of methods joined by dot, e.g. `Pizza.builder(10).add(3).Plane().Hi("aa")`. Overall, the code looks like:  

```Java  
import java.util.StringJoiner;

public class Pizza {
    
    // Set variables
    private int size; // mandatory
    private boolean onion; //optional
    private boolean cheese; //optional
    private boolean olives; //optional
    private boolean tomato; //optional
    private boolean mushroom; //optional
    private boolean ham; //optional
    private int sausageCount; //optional

    // Main class constructor, uses builder class to set variables. Note that for optional variables they already have a default value set in builder class.
    private Pizza(Builder builder) {
        this.size = builder.size; // E.g. Use size() from builder class
        this.onion = builder.onion;
        this.cheese = builder.cheese;
        this.olives = builder.olives;
        this.tomato = builder.tomato;
        this.mushroom = builder.mushroom;
        this.ham = builder.ham;
        this.sausageCount = builder.sausageCount;
    }
    
    // Method for joining words together in 1 string, overrides default toString(), only for this example (in real example this would be bad cause adding more variables means this needs to edited as well)
    @Override
    public String toString() {
        return new StringJoiner(", ", Pizza.class.getSimpleName() + "[", "]")
                .add("size=" + size)
                .add("onion=" + onion)
                .add("cheese=" + cheese)
                .add("olives=" + olives)
                .add("tomato=" + tomato)
                .add("mushroom=" + mushroom)
                .add("ham=" + ham)
                .add("sausageCount=" + sausageCount)
                .toString();
    }

    // Builder class
    public static class Builder {

        private int size; // mandatory
        private boolean onion = false; //optional with default value
        private boolean cheese = false; //optional with default value
        private boolean olives = false; //optional with default value
        private boolean tomato = false; //optional with default value
        private boolean mushroom = false; //optional with default value
        private boolean ham = false; //optional with default value
        private int sausageCount = 0; //optional with default value

        // We set size in the constructor because we want to enforce the client setting it, being a mandatory field. This does not set a variable, so doesn't need return.
        public Builder(int size) {
            this.size = size;
        }

        public Builder addOnions() {
            this.onion = true;
            return this;
        }

        public Builder addCheese() {
            this.cheese = true;
            return this;
        }

        public Builder addOlives() {
            this.olives = true;
            return this;
        }

        public Builder addTomato() {
            this.tomato = true;
            return this;
        }

        public Builder addMushrooms() {
            this.mushroom = true;
            return this;
        }

        public Builder addHam() {
            this.ham = true;
            return this;
        }

        public Builder sausageCount(int sausageCount) {
            this.sausageCount = sausageCount;
            return this; // This allows us to return the whole Builder class, allowing to chain method commands (e.g. Pizza.addOnions().addCheese() and etc)
        }

        public Pizza build() {
            /* Returns a Pizza object with 'this' parameters, where 'this' refers to the Build class, where we have set the options. The Pizza 'this' constructor uses the values obtained from build 
            class (the Pizza constructor still needs all variables defined). However since the build class sets default values then we don't have to set these values if we don't want to (optional variables) */
            return new Pizza(this);
        }
    }
}

```  
And to use the class:  
```Java  
public class Main{
      public static void main(String[] args) {
          // Note we call builder class to define parameters, since builder class has defualt values the ones we don't define don't need to be included in parameter, making it easier
          Pizza pizza = new Pizza.Builder(10).addCheese().addOlives().sausageCount(2).addTomato().build();
        System.out.println(pizza);
  }
}
```
Notes:  
- We can also simply do `new Pizza.Builder(5).build()` to simply make a pizza of size 5 and no options, the essential vairables are set (size) and `build()` called  
- Method chaining works by having the first method return an object (with other methods), calling one of the object's methods in the enxt method, which returns an object that contains other methods, and etc. Basically, a method reutrns an object that has other methods that we can use, which can be directly called via method chaining. E.g. `Pizza.addCheese().addSausage()`, `Pizza` has several methods to add toppings onto pizza, `addCheese()` returns the object again (which still has the topping methods), `addSausage()` is called from the return object.   
- If we want to add more optional variables, we would only need to add initial variable, constructor `this` variable, and corresponding builder method

**Prototype (Creational) design pattern:**  
This design can be used when having to create multiple instances/objects of similar attributes (e.g. Game sprites). This usually means each instance is defined by its attributes, which we want to be able to adjust for each instance. Create an interface called `Prototype` that holds a method for 'copying'. FIrstly:  
```Java  
public interface Prototype {
    Prototype copy();
}
```  
Then:  
```Java  
public class Avatar implements Prototype{
    private int size; // Set variables
    private int walkingSpeed;
    private int walkingDirection;
    public Avatar(int size, int walkingSpeed, int walkingDirection) {
        this.size = size; // Set variables for each instance
        this.walkingSpeed = walkingSpeed;
        this.walkingDirection = walkingDirection;
    }

    public int getSize() {
        return size; // Getter for size variable
    }


    @Override
    public String toString() {
        return "Avatar [size=" + size + ", walkingSpeed=" + walkingSpeed + ", walkingDirection=" + walkingDirection
                + "]";
    } // Override over Java's default toString() method to instead print out what we want. Note that the toString() method is called by default when we use println()

    @Override
    public Prototype copy() {
        return new Avatar(size, walkingSpeed, walkingDirection); // Return new instance of itself
    }

}
```  
To use:  
```Java  
Avatar avatar = new Avatar(50, 30, 6); // Parameters define the variables
  System.out.println(avatar); // Since we override the toString() method, this prints out the new toString() return
  Avatar clone = (Avatar) avatar.copy(); // Create new instance by using the copy method
  System.out.println(clone); // Copy has same stats as other instance
```  
The instance returns itself via a method, so calling the `copy()` method frmo the instance essentially creates a new instance that is a duplicate of the copied instance. 

Typically speaking in Java any class autoamtically contains a `clone()` method which we can use to create an instance of itself, so we could actually just call `<classname>.clone()` 

### Structural design patterns:  
**Adapter (Creational) design pattern:**  
The adapter design pattern behaves similarly to a power adapter, it allows a 'conversion' between two interfaces and acts as the 'translator' between sides. 

A class (referred to as `Adapter`) will translate a request from one class to another. For example, if we create an interface:  
```Java  
public interface Sorter {
     int[] sort(int[] numbers); // Sort out arrays of integers
}
```  
And we also want to use a default method from Java library:  
```Java  
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// library class that we cannot change
public class ListSorter {
    public List<Integer> sortList(List<Integer> numbers)   { // Method that sorts List of integers
        //copy the list number into another list
        List<Integer> copyList = new ArrayList<>(numbers); 
        Collections.sort(copyList,  Collections.reverseOrder()); // Note that this sorts List types
        return copyList; // return the sorted list
    }
}
```  
The `ListSorter` default class can only sort `List` types, not arrays. We can't change the original class because it was a default class, and hence we don't know exactly what the code does and could risk bugs. If we want to use this class to sort integer arrays then we need to create `Adapter` class. In this example, `Adapter` class is called `SortListAdapter` and it implements our original interface for the integer array sorter.  
```Java  
public class SortListAdapter implements Sorter {

    private int[] convertList2Array(List<Integer> numbers) { // Generates int array that has same values as Integer List type input
    // Basically converts an List<Integer> type to int[] array type
    	int[] array = new int[numbers.size()];
    	for (int i = 0; i < numbers.size(); i++) {
       	    array[i] = numbers.get(i);
    	}
    	return array;
    }
    
    private List<Integer> convertArray2List(int[] numbers) { // Generats Integer List type that has same values as a int array input
    // Basically converts an int[] array type to List<Integer> type
    	List<Integer> list = new ArrayList<>();
    	for (int number : numbers) {
        	list.add(number);
    	}
    	return list;
	}

    @Override
    public int[] sort(int[] numbers) {
        List<Integer> numberList = convertArray2List(numbers); // Convert int[] type input to List<Integer> type input via conversion method

        ListSorter sorter = new ListSorter();
        List<Integer> listSorted = sorter.sortList(numberList); // Sort elements in List<Integer> type using Java default method
        int[] arraySorted = convertList2Array(listSorted); // Convert the sorted List<Integer> back to int[] array type

        return arraySorted;
    }
}
```  
What this code does is basically define 2 helper methods that can convert between 2 types, then overidded the sorting method to utilise conversion methods instead, and run a fixed method (i.e. Method that we can't change the code of) and if needed convert types again. In this example we converted between `List<Integer>` and `int[]` types by looping through each element and collecting it to form the new type, since both types are iterable. If we wanted to change between other types (e.g. `String` and `int`) then we could utilise default conversion methods. In any case, the adapter class can convert between the types easily.

**Composite (Structural) design pattern:**  
Used for programs that utilise a 'tree' structure (e.g. Folders and files, a folder can extend to another folder which extends to some files, basically going deeper and deeper). This design pattern can deal with the many repeated code of creating such structure. For example, we made a program that can create a folder and files, by using simple attribute fields for a file and an adding.removing function for files and folders for a folder. But if we want to get the total number of files and folders within a folder, we need to count every file inside every folder first, then add up the size of each smaller folder together to find total size (basically we would need 2 loops minimum). We would also need to alter the file and folder classes themselves if we want to make extra functions, such as getting title of a file/folder (currently these files/folders only contain a return size function which is located in the file and folder classes themselves, we would need to add extra method to the folder/file classes for more functions). This design pattern treats individual objects and groups of objects the same way  

It is composed of three things:  
- Element: A base interface/class for manging child composites, it should be abstrsact/interface
- Leaf: Implements the default behaviour of the base component
- Composite: Implements the base component methods

For example, the Element:  
```Java  
interface FileSystemElement {
    void display(); // Method to display
    int  getSize(); // Method to get size
}
```  
The Leaf:  
```Java  
class File implements FileSystemElement { // Implements the Element class
    private String name;
    private int size;

    public File(String name, int size) { // Set own variables
        this.name = name;
        this.size = size;
    }

    @Override // Override display method with its own thing
    public void display() { 
        System.out.println("File -> " + name);
    }

    @Override // Overrides the getSize method to its own thing
    public int getSize() {
        return size;
    }
}
```  
And the Composite:
```Java
class Folder implements FileSystemElement { // Implements the same Element class
    private String name;
    private List<FileSystemElement> components = new ArrayList<>(); // Arraylist of Element types (interface)

    public Folder(String name) { // Set own variables
        this.name = name;
    }

    public void addComponent(FileSystemElement component) { // New method, adds an Element type into the arraylist. Note that the File class implements the Element type (FileSystemElement) so we can pass a File class into this input as well)
        components.add(component);
    }

    public void removeComponent(FileSystemElement component) { // Same as above but removes from arraylist
        components.remove(component);
    }

    @Override
    public void display() { // Override the display method
        System.out.println("Folder -> " + name);
        for (FileSystemElement component : components) {
            component.display(); // Except now we can put the loop here to display each File type in the arraylist in Folder
        }
    }

    @Override
    public int getSize() { // Override getSize() method
        int size = 0;
        for (FileSystemElement component : components) { // Loop through arraylist and get size of each File (using it's own method)
	// Note the for loop is a simplified version, for each FileSystemElement variable (component) in Arraylist components do something, in this case utilise the getSize() method of the current component to get total size
            size = size + component.getSize();
        }
        return size;
    }
}
```  
This way, both the `File` and `Folder` classes implement the `FileSystemElement` interface, so they can all be identified as a `FileSystemElement` type. Hence we can add either folders or files into a folder since they are both considered as the same type.  


### Behavioural design patterns:  
**Command (Behavioural) design pattern:**  
This deals with the issue of multiple `if-else` statements that set the receiver to run based on a condition. An invoker is the condition giver, receiver uses the invoker to run certain response, e.g.  
![image](https://github.com/Ezs377/Notes/assets/79125281/e4b054d2-89c8-4e24-88d7-70c10ae23001)  
This is difficult when we have to create more receivers or create more invokers, as this results in a long chain of `if-else` statements. For example, in a restaraunt, we have customer makes order, and a waiter delivers order to a chef directly. However, this means we need to code what the waiter does, which chef to go to, and what information needs to be given to that specific chef. If we have more chefs/waiters, we need additional code for each of them, and more chefs means extra conditionals (e.g. For soups, got to chef 1, for bread got to chef 2, etc)>

Alternatively we can separate the invoker object with the receiver object, which means that the classes for each can be edited separately. For the same restaurant example, the waiter writes down the customer order on paper, then drops it off to the kitchen and rings a bell. Depending on the bell a specific chef will come along and pickup the paper and cook it. The waiter and chef never directly communicates to each other.  

The command design pattern has 5 main components:  
- `Command` declares an interface for abstract commands (e.g. `execute()`)  
- `ConcreteCommand` are classes that implement the `Command` interface. They contain the reference of who is going to be the receiver of the implemented command  
- `Receiver` contains code on how to run a specific command  
- `Invoker` holds the `ConcreteCommand` to be executed  
- `Client` creates a `ConcreteCommand` to be given to the `Invoker`  

This separates `Invoker` from `Receiver`. `Invoker` has the full `ConcreteCommand` which knows which `Receiver` to run.

For example, a remote controller for a smart home to control the lights (`Light`) and garage door (`GarageDoor`) where both of these are `Receivers`.  
```Java  
// Receiver
public class Light {
	private String location;

  // Location of light
	public Light(String location) {
		this.location = location;
	}
  
  // Turn on light method
	public void on() {
		System.out.println(location + " light is on");
	}
  
  // Turn off light method
	public void off() {
		System.out.println(location + " light is off");
	}
}

// Receiver
public class GarageDoor {
  
  // Ooens garage door method
	public void up() {
		System.out.println("Garage Door is Up");
	}
  
  // Closes garage door method
	public void down() {
		System.out.println("Garage Door is Down");
	}
  
  // etc
 	public void lightOn() {
		System.out.println("Garage light is on");
	}

	public void lightOff() {
		System.out.println("Garage light is off");
	}
}
```  
The command interface simply declares the `execute()` method:  
```Java  
// Command
public interface Command {
	void execute();
}  
```  
4 concrete command implementations determine the receiver of the command, an example:  
```Java  
//Concrete Command for turning on light
public class LightOnCommand implements Command { // Implement Command interface

	private Light light; // Set variable, has type Light (from receiver class)

	public LightOnCommand(Light light) { // Constructor, note that it takes an input of instance of Light, the receiver class
		this.light = light;
	}

	@Override // Override Command method, i.e. Change what the execute() method does
	public void execute() {
		light.on(); // Turn on light, on() method from Light class (receiver class). This can be done since our constructor input was a Light type
	}
}
```  
Other concrete commands have similar code, basically contains a variable and overrides the `execute()` method.  

The remote controller is implemented as our invoker:  
```Java  
//Invoker
public class RemoteController{

  private Command command; // Command type variable (from Command interface)

  public void setCommand(Command command){
    this.command = command; // Sets variable
  }

  public void pressButton(){
    command.execute(); // Runs execute of the command
  }

}
```  
Using this code looks like:  
```Java  
//Client
public class Main {

  public static void main(String[] args) {
    RemoteController invoker = new RemoteController(); // Create new remote called invoker
    Light lightBedroom = new Light("Bedroom"); // Sets name of a new light with Light type
    Command lightsOn = new LightOnCommand(lightBedroom); // Sets command for lights for given Light type defined earlier
    Command lightsOff = new LightOffCommand(lightBedroom); // Same
    Command garageUp = new GarageDoorUpCommand(new GarageDoor()); // Garage doesn't need name so invoked directly
    Command garageDown = new GarageDoorDownCommand(new GarageDoor());

    // light switch on
    invoker.setCommand(lightsOn); // From remote, call setCommand method with lightsOn Command type
    invoker.pressButton(); // Run execute() of remote, which is from lightsOn (LightsOnCommand type), which implements the Command interface
    // light switch off
    invoker.setCommand(lightsOff); // Same
    invoker.pressButton();
    // garage up
    invoker.setCommand(garageUp); // Same
    invoker.pressButton();
    // garage down
    invoker.setCommand(garageDown); // Same
    invoker.pressButton();
	}

}
```  
Basically, for example:
- Create receiver class (`Main_Receiver1`) which contains some methods, e.g. `Main_Receiver_method1())  

- Create interface for commands, called `Main_Command`, and a blank method `execute()`  

- Create concrete command that implement `Main_Command`, e.g. `Concrete_Command1`). These take `Main_Receiver1` type variables as constructor inputs variables (called `Concrete_Main_Receiver1`), and an `execute()` method that overrides the method from `Main_Command`, and runs a method from `Concrete_Main_Receiver1` which is also the same methods in `Main_Receiver1`, AKA `Main_Receiver_method1()`. Basically, add the receiver method in the `execute()` method in the concrete command

- Create invoker called `Main_Invoker`. This has a method that defines `Main_Command` type variables (called `Invoker_Command`). A method takes `Main_Command` type varibales as input variables and binds to a `this` variable (similar process to constructor but we define it as a regualr method). Also a method that runs `execute()` from `Invoker_Command` (which is of type `Main_Command` which already contains a `execute()` method. Note that this uses the interface type, since concrete command implements interface they have the same type as interface. Bascially, the `Main_Invoker` class should set a `this.Main_Command` variable in one method and be able to run `execute()` from that variable in another method.

- Code usage would be something like creating new `Main_Invoker` instance (called `Invoker`) and new `Main_Receiver1` instance (called `Receiver1`). Then create new `Main_Command` (called `Command`) BUT make it an instance of a concrete command, i.e. `Concrete_Command1`. Since `Concrete_Command1` implements `Main_Command`, it is of `Main_Command` type as well. Input the receiver instance `Receiver1` into the `Command` variable (that holds an instance of `Concrete_Command1`, with `Receiver1` as input).  

- Finally to run receiver methods call the `this` setter in `Invoker` and input a `Command` type variable that was defined earlier (that holds a concrete command instance, i.e. `Concrete_Command1`). Then we can run the method in `Invoker` that runs the `execute()` method within the `Main_Invoker` class. Basically, set a `Command` variable in `Invoker`, then run `execute()` from `Invoker` using the `Invoker` method. The `execute()` method should run the corresponding overriden `execute()` in the `Concrete_Command1` which runs a method from `Main_Receiver1`. 

Diagram:  
![image](https://github.com/Ezs377/Notes/assets/79125281/387f68ad-9357-481f-bb0e-f7535cb5087d)  

**Strategy (Behavioural) design pattern:**  
This pattern is useful for multiple, similar algorithms that work slightly differently to each other but similar function (e.g. Printing out receipt based on payment type). Usually the inputs to each algorithm would be the same type. The process is:  
1. Create interface (e.g. `PaymentType`) that each algorithm will implement (set the input variables, methods, etc)  
2. Implement the interface for each algorithm needed (e.g. `Visa`, `Cash`, `ASB`). Each algorithm class (strategies) overrides the methods form `PaymentType` interface 
3. Create `Order` class that utilises strategies, by taking `PaymentType` type `this` variables, and a method that can call methods from the given `PaymentType` object (i.e. Current strategy). We can also add a setter method in the `Order` class that changes the `PaymentType` `this` variable in the `Order` class so we can switch which strategy is used anytime  

### Exceptions:  
An exception is basically an error in Java. Exception errors can occur during runtime, whereas compilation errors (i.e. Syntax) occur during compilation (before running). An exception is actually an object in Java. THrowing an exception means declaring an exception and stopping program, typically the exception is attempted to be caught to a `try` and `catch` statement, if no matching statement is found then stop program.  

An exception usually contains information about the error (i.e. Exception type, such as `NullPointerException`), and the class, method, and line number that triggered the exception. It will also give the current state of the program variables when the error occured (e.g. `Index 3 out of bounds for length 3`).  

We can use `try` and `catch` statements to 'catch' exceptions and prevent them from breaking program. `try` and `catch` is done by doing:  
```Java  
try {
    <code>
} catch (<exceptionType <variable>>) {
    <exceptiont>
} finally {
    <code that runs regardless>
}  
```  
Bascially a `try` and `except` from Python. However this time we need to specify the exception type. Some exceptions are located in other modules and so we need to import those modules to utilise those exceptions. Also note that we use a variable with the type `ExceptionType` where `ExceptionType` is an exception type, e.g. `NullPointerException`. The variable assigned can be used to reference the exception so we can utilise methods for that exception.  
The `finally` section runs the code regardless if the `catch` was triggered or not. Note that this also means it will run alongside the `try` section.  

We can catch multiple exceptions by either adding more `catch` statements or by writing in one line, e.g. `catch (<exceptiontype1> | <exceptiontype2> <variable>)`. Since `|` stands for OR condition. We can also utilise general exceptions (e.g. `RuntimeException`) which holds many exceptions, however this also means a lot of the exceptions will be unknown and we could accidentally catch an exception that could cause problems later.  

Checked exceptions are caught during compiling, and force the develiper to fix them before they can compile code, i.e. They have to be fixed. `java.lang.Exceptions` are checked.
Unchecked exceptions are caught during runtime, but still allows the code to be compiled, i.e. Issues relating with the programming compiling. `java.lang.RuntimeExceptions` are unchecked.

To create our own exceptions, we need to create exception class (since exceptions are objects, declared from default Java `java.lang`). By convention, an exception must end with `Exception`.  
- Create a class that describes an exception (remember it must end with `Exception`)  
- If the exception is checked, it must extend `Exception` Java class, otherwise if unchecked it must extend `RuntimeException` Java class  
- Define contructor(s) that call `super()`  

For example:  
```Java  
public class InsufficientBookCopies extends Exception { // Extends Exception, so checked
    private final String bookTitle;

    public InsufficientBalanceException(String bookTitle) { // Constructor, uses super to input string output
        super("Trying to sell a sold-out book: " + bookTitle);
        this.bookTitle = bookTitle;
    }

    public String getBookTitle() {
        return bookTitle;
    }
}
```  
To choose whether exception is checked or unchecked, if a user can fix an exception then make it checked, otherwise if the user cannot fix the exception easily make it unchecked. (ask Ed)

## Collections:  
A collection is a framework that allows storage and editing of groups of objects. The framework:   
![image](https://github.com/Ezs377/Notes/assets/79125281/06316967-2922-4225-a7b6-9cd6f758301e)  
Bascially, an `Arraylist` is a type (class) that implements the `List` interface, which itself extends the `Collection` interface. `Set` is also an extension of `Collection`.  
A framework provides a hierarchy of interfaces and classes for managing groups of objects. The Collections Framework is a popular framework. We focus on `Collection` and `Map` interfaces to study. Also note that items used in `Collection` or `Map` need to be an object type (e.g. Integer) instead of being a primitive type (e.g. int).  

**Set interface:**  
A `Set` is a `Collection` of unique items. There can be no duplicate elements in a set, and elements are unordered. They are denoted as type `Set<<type>>`, where `<type>` could be any object type, such as `Integer`. `Set` itself is an interface for the type, so can be used to classify any type that implements the `Set` interface, such as `HashSet`. `new HashSet<Integer>()` gives a new `Hashset` with `Integer` types held inside.  
We can utilise `.add()` to add element to set,  
`.contains()` to check if a set contains the element,  
`.equals()` to check if two sets have the same elements.  
Sets use curly brackets, e.g. `setA {1, 2, 3}` BUT creating sets is like ArrayList and utilises `add()` to add elements.

The intersection of two sets (setA and setB) is the elements that are present in both sets, i.e. `setA.contains(x) = true AND setB.contains(x) = true`. The intersection is presented as a set itself that contains the elements present in both sets.  

The union of two sets is the elements that are either in setA or setB, i.e. `setA.contains(x) = true OR setB.contains(x) = true`. Union is presented as a set that contains the elements that are either in setA or setB, however note that duplicate values are combined into 1 element, e.g. `setA = {1, 2, 3}` and `setB = {3, 4, 5}`, the union will be `{1, 2, 3, 4, 5}`. Note that 3 in in both sets but only appears once in union set.  

The difference in setA and setB is a set that contains elements that don't exist in other set, i.e. `setA.contains(x) = true AND setB.contains(x) = false`. Note that the difference set will be different depending on the order of setA and setB. E.g. `setA = {1, 2, 3}` and `setB = {3, 4, 5}`, difference of setA and setB is `{1, 2}` and difference of setB and setA is `{4, 5}`. Basically the elements in first set that doesn't exist in second set.  

The subset is a if all elements in a set is present in another set, i.e. `for x in setA, setB.contains(x) = true`. If setA is a subset of setB, then `setA.equals(setB) = true`. Note that the order of sets compared matters, as we compare for each element in the first set, hence the second set can be longer that the first set and it would still be valid. For example, `setA = {1, 2, 3}` and `setB = {3, 4, 5}` are not subsets as setA has `{1, 2, 3`} and setB does not have `{1, 2}`. By these rules, a set is a subset of itself, and an empty set is a subset of any set (since it has nothing, and any other set can have nothing without changing the set). 

The powerset is a set that contains all the subsets of a set. For example, if setA = `{2, 8 ,1}`, then powerset is `{<emptyset>, {1}, {2}, {8}, {1, 2}, {1, 8}, {2, 8}, {1, 2, 8}}`. All these elements are subsets of setA.  

The cross product is a set of all possible pairs between two sets. E.g. setA = `{a, b}`, setB = `{c, d}`, then cross product is `{(a, c), (a, d), (b, c), (b, d)}`.  

It is possible to create our own sets utilise `List`.  

Since sets can only contain unique elements, if duplicate elements are added/implemented then the set doesn't change and discards the duplicate element.  

**Map interface:**  
Similar to dictionary in Python, the `Map` data structure creates key-value pairs, where the key is a unique identifier.  
Each key part has to be unique, and maps to a distinct value, so map is actually a mathmatical function.  
Some methods of the `Map` interface are:  
- `.size()` returns number of entries in map (i.e. Pairs)
- `.isEmpty()` returns true if map is empty
- `.get(<key)` returns the value of the specified key, returns `null` if key doesn't exist
- `.put(<key>, <value>)` replaces the value of the specified key with the specified value
- `.keyset()` returns a set view of the keys in the map, i.e. An array of the keys in the map (not values)
- `.values()` returns a Collection view of the values contained in map, i.e. An array of the values in the map (not keys)

Every object in Java has an associated hashing function. This allows objects to be 'mapped' to 'buckets'. When two objects are mapped to the same bucket this is a collision.  
A hash table is a way of mapping key-value tuples (pairs). If we set the keys as integers in a range of 0 to N-1, then we can create a bucket array, where the entry for each key is inserted in corresponding elements of the array based on key integer value. Problem is if array size doesn't match number of key-value pairs, and we can't always utilise integers for keys.

Instead, we can use hashing function `h(k)` (or hashcode) which takes a key `k` as a specific object, and an index into the bucket array. I.e. Input to `h(k)` is a key `k` and output is an index in the array range 0 to N-1.  
Ideally `h(k)` should be injective, i.e. Two different elements cannot be mapped to the same value. This doesn't always occur though and we can get a collision.  
Hashcode function essentially converts a key to a integer value that allows it to be allocated in an array. 

A Hashmap is a collection/data storage that allows items to be identified with a key rather than an index. For example, Lists use an integer index as 'keys' to each value (element) in the list. A hashmap utilises a unique key to identify each value, which can lead to faster recall/allocation of values as instead of utilising numerical index, a key can be immediately used to identify the value. However, this also means all keys need to be unique, if 2 keys are identical then we get collision.  

To ensure we are optimizing memory to accomodate for all unique keys, without infinitely generating them, is to utilise hashing function to generate hashcode for keys. In Java, we have the `hash()` method, which is called by `Object.hash(<var>)`. Note that `Object` is the parent class of all classes in Java, i.e. All other classes extend `Object` class.  

A hash table is an efficient way of mapping key-value pairs. But since in Java array size is determined at compile time, i.e. Fixed size, unless using arraylist. So if we set an array during compile time then we could end up making inefficient storage as not all indexes are used up. 

A hashcode is generally a mathmetical function that utilises a prime number to generate a unqiue key, and the `.equals()` method can check if a key is equal. 

The Java hascode contract simply states that objects that are equal must have the same hashcode DURING the same run. Hashcodes of objects can be different everytime the program is executed, but during exectuion the same hashcode must refer to the same object. The 3 contracts (conditions) of hashcodes:  
1. During execution, the hashcode of an object has to be unique, yet remain constant during execution. Different executions can have different hascodes for that object, but during runtime the hashcode must remain constant
2. 2 objects are equal if the hashcode is equal, which is confirmed via the overriden `.equals()` method  
3. Different objects can have differently unique hashcodes, and doing so will improve the perfomance of the program, as different objects that have the same hashcode will cause a collision, which may not necessarily break the program, but forces the program to resolve the collision (e.g. Separating the objects) which reduces perfomance

## Data structures:  
Arrays and Arraylists are examples of static and dynamic data structures respectively.  

Arrays/Arraylists are more efficient as they have their size determined before runtime (for Arraylist, it can change size during runtime), and data elements are arranged next to each other in memory (cache prefetching is better performance). However inserting/deleting elements from an array incurs bigger resource costs. 

An abstract data structure (ADT) contains data elements and definitions of operations that can be done on the ADT, BUT the implementation depends on code. Typically the implementation of operations is not specifically coded in the ADT (hence abstract), it only tells you the possible oeprations on the ADT.  

Linked List is a data structure that utilises nodes (from graphs). Each data element is associated with a node, and adding new elements means creaitng more nodes. To manage the data, nodes are linked together, so that we can trace every element through a single node, since all nodes are linked together. However, nodes can be located anywhere in memory, so this way we don't need tor rearrange data in memory when adding new data elements, as we can just create a node then link it, it doesn't have to be next to other data elements in memory. The linking of nodes can either be singly linked (only linked to the next node, can only go forwards) or doubly linked (linked to previous and next node, allowing two-way traversal).

**Singly linked list:**  
![image](https://github.com/Ezs377/Notes/assets/79125281/f93fd00a-14f2-4ca2-9972-af4bb4306c3b)  

A singly linked list has a `head`, which contains reference to the first node in the list, and hence all other nodes in list (since all other nodes can be located through the first node). THe `next` pointer only refers to the next node in the list, so cannot go to previous node. Operations are typically done on the `head` reference. Typical operations for singly linked list:  

- `insert()`, `append()` for adding new element at current position (node)
- `remove()` to remove element at current position (node)
- `fetch()` to get a value from current position
- `size()` to get current size of list

We can also have a `tail` reference for the last element in list.  

**Doubly linked list:**  
![image](https://github.com/Ezs377/Notes/assets/79125281/245d4ff9-ba32-409d-a548-b64f20ccb44e)  
A doubly linked list is similar to singly linked list, except each node also has a pointer to the previous node as well as the enxt node. We also have `head` and `tail` references that point to first element and last element respectively. Some specific doubly linked list operations inlcude `insertToTail()`.  

**Stack:**  
A stack data streucture has a last in, first out policy (LIFO). Essentially acting like a real life stack, the first item placed will become the item at the bottom as more items are stacked on top, and the top items will be taken out first when removing items. Typical operations include:  
- `push()` to add a new element to the top of stack
- `pop()` to remove the top element
- `peek()` to view the top element (without doing anything to it)  
- `clear()` to clear all elements
- `isEmpty()` to check if stack is empty

**Queue:**  
Similar to stack, instead we have first in, first out policy (FIFO). Items added first will go out first, like a real queue. Typical operations include:  
- `enqueue()` to add a new element to the edn of queue
- `dequeue()` to remove first element in front of queue
- `peek()` to view the first element in front of queue (without affecting any elements)
- `clear()` and `isEmpty()` operations as usual

**Binary tree:**  
Utilises connected nodes (graph stuff) to form parent nodes and children nodes, similar to linked likst. The root node has no parent root, instead it is the parent root of all othe rnodes (i.e. Top of the tree). A leaf node is a node by itself with no children (a childrne node could be a leaf node).  

### Comparing data structures:  
We can compare data structures via their operations. These can be defined as the O term.  
O(1) means a constant number of operations, e.g. A simple `if` statement that contains a set number of operations, such as add two variables, or set variable to a value. Regardless of a given 'input' to the operations, the operation number of operations performed remains the same.
O(N) means an N number of operations which is a linear increase, e.g. A `for` loop that loops N times performing an operation each loop.  
O(N<sup>2</sup>) means the number of operations is N<sup>2</sup> times, which is a quadratic increase, e.g. `for` loop inside another `for` loop, this causes N\*N operations, i.e. N<sup>2</sup>.  

Other variations exist, such as O(N<sup>3</sup>log(N)) which involes running functions inside `for` loop and etc.  

For arrays simple operations like adding and removing elements are O(N) operations, since we use `for` loop and cycle through each element. We can 'calculate' the complexity by utilising the logic, for example, O(N) operations can be described as repeating )(1) oeprations N times.  

For a linked list, we know adding/removing element at the front is a O(1) opeartion (since we don't need to cycle through the linked list), but other operations unknown.

## Linked list:  
An example of a linked list data structure:  
```Java  
public class Node {
    private Object val;
    private Node next;

    // constructor

    public Node() {

    }

    public Node(Object v) {
	val = v;
	next = null;
    }

    // getters and setters

    public void setNext(Node n) {
	next = n;
    }

    public Node getNext() {
	return next;
    }

    public Object getValue() {
	return val;
    }

    public static void main(String args[]) {
	Node n1 = new Node(0);
	Node n2 = new Node(200);
	Node n3 = new Node(-50);
	n1.setNext(n2);
	n2.setNext(n3);
	n3.setNext(null);

	Node n = new Node();
	n = n1;
	Double sum = 0.0;
	while (n != null) {
	    System.out.println("The value of the next node is: " + n.getValue());
	    sum = sum + ((Double) n.getValue());
	    n = n.getNext();
	}
	System.out.println("The sum of the values: " + sum);
    }
}
```
Note this utilises the `object` type, which can store any object type rather than a specific type (e.g. `int`). It is basically getter, object input, and a setter for the `Next` reference which is set externally by other code.  

Ideally we use generic types (e.g. `Object`) which allows us to only define the data structure once and apply it to many scenarios.  
![image](https://github.com/Ezs377/Notes/assets/79125281/5289b264-c324-4b35-8431-c64f0419b8df)  

### Type safety:  
Using generics gurantees type safety. A generic type could be `List<T>`, where `T` is a formal parameter type.  
Using `Object` allows the use of non-primitive (reference) types, such as `String` (note that default types like `int` are primitive).  
Using 










### Java useful stuff:  
- `System.out.println("string")` = Print out   
- A method is called by doing `<object/variable name>.<methodname>(etc)`
- Comments use `//` or `/*  */`  
- `main(Strings[] args) {` is used as the starting method, the parameters are for command line arguments, so if we run the Java program from comand line we can input stuff and it goes into an array (`Strings[]`) which is passed to the `main` method
- A class that extends/implements an abstract/interface will share the SAME type as the abstract/interface! So we can use the abstract/interface type to define all extended/implementations of the abstract/interfaces, instead of using specific types.

















