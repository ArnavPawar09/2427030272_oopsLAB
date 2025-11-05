"""
create objects and demonstrate all types of polymorphisms
"""

class Score:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Score(self.marks + other.marks)

    def display(self):
        print("Total Marks:", self.marks)

s1 = Score(75)
s2 = Score(85)
s3 = s1 + s2
s3.display()
