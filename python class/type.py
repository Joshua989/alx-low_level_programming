The code you provided demonstrates examples of different types of inheritance: single inheritance, multiple inheritance, and multilevel inheritance. However, there is an error in the code, which I will correct and provide explanations with comments. Here's the revised code:

```python
# Single Inheritance

class parent:
  def funct1(self):
    print("This is function 1")
    
class child(parent):
  def funct2(self): 
    print("This is function 2")
      
      
# Object part
ob = child()
ob.funct1()  # Call the funct1 method of the parent class using the child object
ob.funct2()  # Call the funct2 method of the child class using the child object


# Multiple Inheritance

class parent1:
  def funct1(self):
    print("This is function 1 from parent1")
    
class parent2:
  def funct3(self):
    print("This is function 3 from parent2")
    
class child(parent1, parent2):
  def funct2(self): 
    print("This is function 2")
      
      
# Object part
ob = child()
ob.funct1()  # Call the funct1 method of parent1
ob.funct2()  # Call the funct2 method of the child class
ob.funct3()  # Call the funct3 method of parent2


# Multilevel Inheritance

class parent:
  def funct1(self):
    print("This is function 1")
    
class parent2(parent):
  def funct3(self):
    print("This is function 3 from parent2")
    
class child(parent2):
  def funct2(self): 
    print("This is function 2")
      
      
# Object part
ob = child()
ob.funct1()  # Call the funct1 method of parent
ob.funct2()  # Call the funct2 method of the child class
ob.funct3()  # Call the funct3 method of parent2
```

Explanation:
- Single Inheritance: In the first part, the `child` class inherits from the `parent` class. The `parent` class has the `funct1` method, and the `child` class has the `funct2` method. The object `ob` is an instance of the `child` class. Calling `ob.funct1()` will execute the `funct1` method inherited from the `parent` class, and calling `ob.funct2()` will execute the `funct2` method of the `child` class.

- Multiple Inheritance: In the second part, the `child` class inherits from both the `parent1` and `parent2` classes. The `parent1` class has the `funct1` method, the `parent2` class has the `funct3` method, and the `child` class has the `funct2` method. The object `ob` is an instance of the `child` class. Calling `ob.funct1()` will execute the `funct1` method of `parent1`, `ob.funct2()` will execute the `funct2` method of the `child` class, and `ob.funct3()` will execute the `funct3` method of `parent2`.

- Multilevel Inheritance: In the third part, the `child` class inherits from the `parent2` class, which itself inherits from the `parent` class. The `parent` class has the `funct1` method, the `parent2` class has the `funct3` method, and the `child` class has the `funct2` method. The object `ob`