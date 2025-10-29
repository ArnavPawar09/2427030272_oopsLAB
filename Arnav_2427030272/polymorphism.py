class shape:
    def sides(self):
        print("not defined")
class color:
    def sides(self):
        print("red")
class square(shape, color):
    def sides(self):
        print("4 sides")

obj = square()
obj.sides()