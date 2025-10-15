"""
1.
create a base class person with attributes : name, age.
create a derived class employee that inherits from person and adds attributes : emp_id, sal.
implement multi-level inheritance with a class manager derived from emplyoee with dept attribute.
implement multiple inheritance with a class trainer that inhabits from employee and certification.
write appropriate method to display all details for each type of employee.
"""

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(self.name)
        print(self.age)

class emp(person):
    def __init__(self, name, age, emp_id, sal):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.sal = sal
    def print_emp(self):
        super().print_person()
        print(self.emp_id)
        print(self.sal)

class manager(emp):
    def __init__(self, name, age, emp_id, sal, dept):
        super().__init__(name, age, emp_id, sal)
        self.dept = dept
    def print_manager(self):
        super().print_emp()
        print(self.dept)

class certification:
    def __init__(self, cert):
        self.cert = cert
    def print_cert(self):
        print(self.cert)
class trainer(emp, certification):
    def __init__(self, name, age, emp_id, sal, cert):
        emp.__init__(self, name, age, emp_id, sal)
        certification.__init__(self, cert)
    def print_trainer(self):
        emp.print_emp(self)
        certification.print_cert(self)

obj1 = manager("Arnav", 19, 12345, 1000000, "CSE")
obj1.print_manager()
print()
obj2 = trainer("Aryan", 25, 67890, 50000, "IT")
print("triner :")
obj2.print_trainer()