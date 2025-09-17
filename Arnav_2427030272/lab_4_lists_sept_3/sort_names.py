# 2) sort 5 names (input) in a list

l=[]
for i in range(0, 5):
    name = input("enter name : ")
    l.append(name)
l.sort()
print(l)