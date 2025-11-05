"""
list element access :
input list of int and an index no
prints element at that index
handles exceptions : indexerror, value error, type error, generic exceptions
"""

try:
    n = int(input("Enter length of list : "))
    l=[]
    for i in range(n):
        e = int(input("Enter element : "))
        l.append(e)
    index = int(input("Enter index : "))
    print("element at index", index, "=", l[index])
except IndexError:
    print("Index Out of Bounds")
except ValueError:
    print("Please Enter Integer Value")
except TypeError:
    print("Unsupported Data Type Entered")
except Exception as e:
    print("An Unexpected Error Occured")
finally:
    print("Program Completed...")