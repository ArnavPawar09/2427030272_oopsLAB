"""
emp salary calculation :
input salary, hra, da
calculate gross salary = salary + hra+ da
handles exceptions : value error, type error, keyboardinterrupt, generic exception
"""

try:
    salary = int(input("Enter base salary : "))
    hra = int(input("Enter hra : "))
    da = int(input("Enter da : "))
except ValueError:
    print("Please Enter Integer Value")
except TypeError:
    print("Unsupported Data Type Entered")
except KeyboardInterrupt:
    print("Program Interrupted")
except Exception as e:
    print("An Unexpected Error Occured")
else:
    gross = salary+hra+da
    print("gross salary =", gross)
finally:
    print("Program Completed...")
