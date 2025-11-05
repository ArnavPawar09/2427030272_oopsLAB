"""
method overloading : 
create a class grade with method calculate() using default args to handle single/multiple marks
"""

class grade:
    def calculate(self, m1=50, m2=0, m3=0):
        print("total marks =", m1+m2+m3)

s1 = grade()
s1.calculate(90)
s1.calculate()
s1.calculate(20, 90)
s1.calculate(60, 70, 80)