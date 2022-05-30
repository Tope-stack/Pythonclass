# section 1 & 2
# position, name, age, level, salary
se1 = ["Software Engineer", "Max", 24, "Junior", 5000]
se2 = ["Software Engineer", "Tomiwa", 24, "Junior", 5000]
se3 = ["Software Engineer", "Ounas", 33, "Senior", 15000]
se4 = ["Software Engineer", "Lisa", 28, "Junior", 3000]

# class


class SoftwareEngineer:

    # class Attribute

    alias = "Keyboard Magician"

    def __init__(self, position, name, age, level, salary):
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method

    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # using return
    #special methods/dunder method

    def __str__(self):
        information = f"name = {self.name} age = {self.age} level = {self.level}"
        return information

    def __eq__(self, other):
        return self.age == other.age and self.salary == other.salary

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
            if age < 30:
                return 7000
                return 20000


# instance

se1 = SoftwareEngineer("Software Engineer", "Max", 24, "Junior", 5000)
print(se1.position, se1.name, se1.age, se1.level, se1.salary)
se2 = SoftwareEngineer("Software Engineer", "Tomiwa", 24, "Junior", 5000)
print(SoftwareEngineer.alias)
print(se2.position, se2.name, se2.age, se2.level, se2.salary)
se3 = SoftwareEngineer("Software Engineer", "Ounas", 33, "Junior", 15000)
print(se3.position, se3.name, se3.age, se3.level, se3.salary)
se4 = SoftwareEngineer("Software Engineer", "Lisa", 28, "Junior", 3000)
print(se4.position, se4.name, se4.age, se4.level, se4.salary)

se1.code()
se2.code()
se3.code_in_language("Python")

print(se1)

print(se1 == se2)

print(SoftwareEngineer.entry_salary(24))

# recap
# create a class(blueprint)
# class vs instance
# instance attribute defined in __init__(self)
#class attribute


#section3
# inherits, extend, override
class Employee:
  
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def work(self):
    print(f"{self.name} is working...")


class SoftwareEngineer(Employee):

  def __init__(self, name, age, salary, level):
    super().__init__(name, age, salary)
    self.level = level

  # To override the debug function we can do this
  # uncomment to use override function
  # def work(self):
  #   print(f"{self.name} is coding...")
    
  
    
  
  #This function is only specific to this base class
  #Extends the functionality of the base class
    
  def debug(self):
    print(f"{self.name} is debugging...")
      
  

class Designer(Employee):

  # To override the debug function we can do this
  # uncomment to use override function
  # def work(self):
  #   print(f"{self.name} is designing...")
  
  #This function is only specific to this base class
    
  def draw(self):
   print(f"{self.name} is drawing...")
  

se = SoftwareEngineer("Max", 25, 6000, "Junior")
se.work()
print(se.level) 
se.debug()



d = Designer("Philip", 27, 7000)
d.work()
d.draw()

# Polymorphism


employees = [SoftwareEngineer ("Max", 24, 6000, "Junior"), 
SoftwareEngineer ("Tomiwa", 24, "Junior", 5000),
Designer("Philipp", 27, 7000)]




def motivate_employeees(employees):
  for employee in employees:
    employee.work()


motivate_employeees(employees)


# Recap of section 3
# inheritance: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# concept of polymorphism


# Section 4
# Encapsulation

class SoftwareEngineer:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # To create a private attribute
    # To create internal function
    # These are private attributes
    self._salary = None
    self._num_bugs_solved = 0

  def code(self):
    self._num_bugs_solved += 1

  # getter
  def get_salary(self):
    return self._salary

  # setter
  def set_salary(self, base_value):
    # if value < 1000
    # self._salary = 1000
    # if value > 20000
    # self._salary = 20000
    self._salary = self._calculate_salary(base_value)

  def _calculate_salary(self, base_value):
    if self._num_bugs_solved < 10:
      return base_value
    if self._num_bugs_solved < 100:
      return base_value * 2
      return base_value * 3



# instance
se = SoftwareEngineer("Max", 25)
print(se.name, se.age)



for i in range(70):
  se.code()
  
# this is applying abstraction principle
se.set_salary(6000)
print(se.get_salary())

# end of section 4
# encapsulation
# mechanism of hiding data implementation
# used private sections


# section 5

class SoftwareEngineer:
  def __init__(self):
    
    self._salary = None
    

  # getter
  @property
  def salary(self):
    return self._salary

  # setter
  @salary.setter
  def salary(self, value):
    self._salary = value
    
  @salary.deleter
  def salary(self):
    del self._salary



se = SoftwareEngineer()

# this is applying abstraction principle
se.salary = 6000
# del se.salary
print(se.salary)

