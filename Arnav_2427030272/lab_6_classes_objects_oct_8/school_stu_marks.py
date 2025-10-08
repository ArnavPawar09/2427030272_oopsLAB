"""
You are designing a program for a school.
Create a Student class with the following attributes:
name, roll_no, marks (out of 100)
Scenario:
Create 3 student objects.
Display their details.
Add a method grade() that prints "Pass" if marks ≥ 40, otherwise "Fail".
"""

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def Display(self):
        print("name :", self.name)
        print("roll no :", self.roll_no)
        print("marks :", self.marks)
        print()
    
    def grade(self):
        if self.marks>100 or self.marks<0:
            print("invalid marks")
        elif(self.marks>=40):
            print("Pass")
        else:
            print("Fail")

s1 = Student("arnav", 123, 90)
s1.grade()
s1.Display()
s2 = Student("aryan", 456, 555)
s2.grade()
s2.Display()
s3 = Student("rahul", 789, 39)
s3.grade()
s3.Display()
