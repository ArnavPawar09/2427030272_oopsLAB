"""
1. school maintains student grades in 3 subjects. WAF to caclulate the avg marks.
   show how default parameters could be used if a student has missed a test
   assuming missing marks = 0
"""

def avg(sub1=0, sub2=0, sub3=0):
    avg = (sub1+sub2+sub3)/3
    return avg
print("avg marks of student 1 :", avg(50, 60, 70))
print("avg marks of student 2 :", avg(50, 70))