The code you provided demonstrates the use of the `super()` function to access and call a method from the parent class. Here's the corrected code with comments:

```python
class parent:
  def funct1(self):
    print('This is function 1')
    
class child(parent):
  def funct2(self):
    super().funct1()  # Call the funct1 method from the parent class using super()
    print("This is function 2")
     
     
ob = child()
ob.funct2()  # Call the funct2 method of the child class using the child object
```

Explanation:
- The `parent` class has a method called `funct1` that prints "This is function 1" when called.
- The `child` class inherits from the `parent` class using the statement `class child(parent)`. This means that the `child` class can access and use the methods and attributes of the `parent` class.
- The `child` class defines a method called `funct2` that overrides the method with the same name in the `parent` class.
- In the `funct2` method of the `child` class, `super().funct1()` is used to call the `funct1` method from the parent class. The `super()` function returns a temporary object of the parent class, allowing us to access and call its methods.
- After calling `super().funct1()`, which prints "This is function 1", the `funct2` method of the `child` class continues executing and prints "This is function 2".

In the object part:
- An instance of the `child` class is created using `ob = child()`.
- To call the `funct2` method of the `child` class, you should use `ob.funct2()`, not `ob.fuct2`. The parentheses `()` are necessary to invoke the method.