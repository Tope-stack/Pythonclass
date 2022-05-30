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
