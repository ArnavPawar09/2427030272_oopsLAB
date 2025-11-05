"""
operator overloading :
create a class score with attribute marks 
overload the "+" operator using "add" to sum two score objects
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
