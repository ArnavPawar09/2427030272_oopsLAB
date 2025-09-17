#1 distance b/w 2 points

x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))

dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
print("distance b/w points =", dist)