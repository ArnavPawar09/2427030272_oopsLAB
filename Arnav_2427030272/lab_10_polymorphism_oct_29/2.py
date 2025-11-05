"""
method overriding :
person -> getrole()
derived classes : student & staff that override getrole()
"""
class person:
    def getrole(self):
        print("I am a person")

class student(person):
    def getrole(self):
        print("I am a student")
        
class staff(person):
    def getrole(self):
        print("I am a staff member")

p = person()
p.getrole()
stu = student()
stu.getrole()
staf = staff()
staf.getrole()