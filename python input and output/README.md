Lecture: Python Input, Import, and Output

Introduction:
Welcome to today's lecture on Python Input, Import, and Output. In this lecture, we will explore the concepts and functionalities related to handling user input, importing external modules, and managing program output in Python. These are fundamental aspects of programming that are essential for building interactive and dynamic applications. By the end of this lecture, you will have a strong understanding of how to interact with users, extend your program's capabilities through external modules, and produce meaningful output. So, let's dive in!

1. Input Handling:

One of the most important aspects of programming is the ability to interact with users and accept input. In Python, we have a built-in function called `input()` that allows us to receive input from the user through the keyboard. 

1.1 The input() Function:

The syntax for the `input()` function is as follows:
```python
variable = input("Prompt message: ")
```
Here, the "Prompt message" is an optional text that will be displayed to the user before accepting input. The user's input will be stored in the variable specified.

Let's see an example:
```python
name = input("Enter your name: ")
```
In this example, the program prompts the user to enter their name, and the input provided by the user is stored in the `name` variable.

Task: 
Now, let's write a program that prompts the user to enter their age and stores it in a variable. Use the `input()` function to accomplish this task.

```python
age = input("Enter your age: ")
```

2. Importing Modules:

Python provides a way to extend the functionality of our programs by importing external modules. Modules are collections of functions, classes, and variables that are written to address specific tasks.

2.1 The import Statement:

To import a module in Python, we use the `import` statement followed by the name of the module.

The syntax for importing a module is as follows:
```python
import module_name
```
For example, if we want to import the `math` module, we would use:
```python
import math
```
This allows us to use the functions and classes provided by the `math` module in our program.

Task:
Let's write a program that calculates the square root of a given number using the `math` module. Import the `math` module and use the `sqrt()` function to calculate the square root.

```python
import math

number = 16
result = math.sqrt(number)
print(result)
```

2.2 Using Imported Functions:

After importing a module, we can use the functions and classes provided by that module in our program. To access these functions, we use the following syntax:
```python
module_name.function_name()
```
For example, to use the `sqrt()` function from the `math` module, we would write:
```python
result = math.sqrt(25)
```
In this example, we calculate the square root of 25 using the `sqrt()` function from the `math` module and store the result in the `result` variable.

Task:
Enhance the previous program to calculate the square root of a user-provided number. Prompt the user to enter a number, convert it to an integer, and use the `sqrt()` function to calculate the square root.

```python
import math

number = int(input("Enter a number: "))
result = math.sqrt(number)
print(result)
```

2.3 Importing Specific Functions:

Sometimes, a module may have multiple functions, and importing the entire module might lead to namespace conflicts. In such cases, we can import specific functions from the module using the `from` statement.

The syntax for

 importing specific functions is as follows:
```python
from module_name import function_name
```
For example, to import only the `sqrt()` function from the `math` module, we would write:
```python
from math import sqrt
```
Now, we can directly use the `sqrt()` function without referencing the module name.

Task:
Modify the previous program to directly use the `sqrt()` function without the module prefix. Import only the `sqrt()` function from the `math` module and calculate the square root of a user-provided number.

```python
from math import sqrt

number = int(input("Enter a number: "))
result = sqrt(number)
print(result)
```

That concludes the first part of our lecture, where we explored input handling and importing modules. In the next part, we will delve into managing program output.