import datetime
my_date = datetime.date(2018,12,1)

print("Hello")

class Employee:
    # Class variables
    sal = 500

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def make_email(self):
        return self.first + "." + self.last + "@leeco.com"

    def pay(self):
        if len(self.last) > 10:
            return self.sal
        else:
            return self.sal / 2
    # Class methods
    @classmethod
    def lower_pay(cls, sal1):
        cls.sal = sal1

    @classmethod
    def from_string(cls, emp_str):
        # CLS is that instance of the class
        first, last = emp_str.split("-")
        return cls(first, last)
    # Reglar methods pass in the insrance itself as first argument, while class method pass the class as the first argument
    # Static Methods do not pass anything

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 4:
            return True
        return False

emp_1 = Employee("lee", "nduati")
print(emp_1.make_email(), emp_1.pay())
emp_2 = Employee("Nanny", "MajorWhiteHouse")
print(emp_2.pay())
emp_2.lower_pay(1000)
print(emp_2.sal, emp_1.sal, Employee.sal)

new_str_1 = "Jonson-Mathews"
new_Str_2 = "Jane-Smith"
print(emp_1.is_workday(my_date))

var = Employee.from_string(new_str_1)
print(var.__dict__)

class Developer(Employee):
    def __init__(self, first, last, language):
        # super().__init__ passes variables from parent class
        # Like in other object-oriented languages, it allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.
        super().__init__(first, last)
        self.language = language
    def return_lang(self):
        return f"language sed during coding is {self.language}"

dev_1 = Developer("Paul", "Kip", "Python")
# dev_2 = Developer

print(dev_1.make_email())
print(dev_1.return_lang())

# Add Attributes to the child class
# In the above,


class Manager(Employee):
    def __init__(self, first, last, employees=None):
        super().__init__(first, last)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, em):
        if em not in self.employees:
            self.employees.append(em)
        return self.employees
    def rem_emp(self, em):
        if em in self.employees:
            self.employees.remove(em)
    def print_emp(self):
        for em in self.employees:
            print(em.make_email())

mgr_1 = Manager("John", "Karumba", [dev_1])

print(mgr_1.make_email())
mgr_1.print_emp()
