"""
Create 2 employees and print their salary slips. 
Methods:
calculate_salary() → Returns total salary after adding DailyAallowance (20%) and HouseRentAllowance (15%).
display() → Prints employee details with total salary.
"""

class salary_slip:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        da = self.salary*0.2
        hra = self.salary*0.15
        total_sal = self.salary + da + hra
        return total_sal

    def display(self):
        print("name :", self.name)
        print("emp if :", self.emp_id)
        print("total salary :", self.calculate_salary())
        print()

e1 = salary_slip("arnav", 12345, 100000)
e2 = salary_slip("aryan", 67890, 12000)
e1.display()
e2.display()