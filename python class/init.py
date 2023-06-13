class parent:
  def __init__(self, fname, fage):
    self.name = fname
    self.age = fage
    
  def view(self): 
    print(self.name, self.age)

class child(parent): 
  def __init__(self, fname, fage): 
    # Call the parent's __init__ method to initialize the inherited attributes
    parent.__init__(self, fname, fage)
    self.lastname = "CJ"
  
  def view(self):
    # Override the view method in the parent class to add lastname
    print(self.name, self.age, self.lastname)

ob = child("23", "python")  # Creating an instance of the child class and passing arguments to the constructor

ob.view()  # Calling the view method of the child class using the child object
