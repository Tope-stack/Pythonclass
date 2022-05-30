
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
    super{}.__init__(name, age, salary)
    self.level = level
  

class Designer(Employee):
  pass
  

se = SoftwareEngineer("Max", 25, 6000, "Junior")
se.work()

d = designer("Philip", 27, 7000)
d.work()