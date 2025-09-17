t=(1, 2, 3, 4, 5)
s = int(input("enter search element : "))
found=0
for i in range(len(t)):
    if i==s:
        print(s,"is at index",i-1)
        found+=1
if found==0: print("not found")
    