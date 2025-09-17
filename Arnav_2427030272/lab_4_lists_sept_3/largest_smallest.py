# 1) input 10 integers in list and find largest and smallest

l=[]
for i in range(0, 10):
    n = int(input("enter int : "))
    l.append(n)
print("largest = ", max(l))
print("smallest = ", min(l))

