# 4) list of marks -> avg 

import math as m
l=[]
n = int(input("enter no of subjects : "))
for i in range(0, n):
    m = int(input("enter marks : "))
    l.append(m)
print("Average marks = ", sum(l)/len(l))
