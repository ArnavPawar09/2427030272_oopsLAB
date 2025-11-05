"""
A uni wants to develop a program for stu result processing
a) take input of marks obtained and total marks
b) calculate percentage of student
c) handle exceptions like : ValueError, ZeroDivisionError, FileNotFoundError, Generic Exception to handle any other unexpected errors
"""

try:
    m = int(input("Enter marks obtained : "))
    t = int(input("Enter total marks : "))
    percentage = m*100/t
except ValueError:
    print("Please Input Integer Value")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
except FileNotFoundError:
    print("Result File Not Found")
except Exception as e:
    print("An Unexpected Error Occured")
else:
    print("percentage :", percentage)
finally:
    print("Program Completed...")