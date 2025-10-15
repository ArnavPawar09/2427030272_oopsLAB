"""
a school has a person, teacher and a class_teacher. 
Each level has its own property and method.
Make a school management system
"""

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(self.name)
        print(self.age)

class teacher(person):
    def __init__(self, name, age, teaches_classes):
        super().__init__(name, age)
        self.teaches_classes = teaches_classes
    def print_teacher(self):
        super().print_person()
        print(self.teaches_classes)

class class_teacher(teacher):
    def __init__(self, name, age, teaches_classes, class_teacher_of):
        super().__init__(name, age, teaches_classes)
        self.class_teacher_of = class_teacher_of
    def print_class_teacher(self):
        super().print_teacher()
        print(self.class_teacher_of)

obj1 = class_teacher("arnav", 25, ["A", "C", "K"], "K")
obj1.print_class_teacher()
print()
obj1.print_person()
print()
obj2 = teacher("aryan", 40, ["G"])
obj2.print_teacher()