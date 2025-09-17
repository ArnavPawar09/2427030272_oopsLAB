"""
6. Design a function stuRecord(course, *subjects, **details) that :
   Stores the course name
   stores multiple subjs using * arg
   stores details like name, age, grade using kwargs
   WAP that demonstrates all 3 cases in 1 function call
"""

def stuRecords(course, *subjects, **details):
    print(course)
    print(subjects)
    print(details)
stuRecords("btech", "math", "oops", "dsa", name="arnav", age=19)