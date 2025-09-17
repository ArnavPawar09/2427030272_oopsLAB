n = int(input("no of elements : "))
t=()
check=0
for i in range(n):
    e = int(input("enter element : "))
    t+=(e,)

for i in t:
    if(i==1 or i==0): continue
    check=0
    for j in range(2, i):
        if i%j==0:
            check+=1
    if check==0:
        print(i)
