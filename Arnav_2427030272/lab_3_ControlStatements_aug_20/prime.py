# check if input no is prime or not

n = int(input("enter n : "))
count=0
for i in range(2, n, 1):
    if n%i==0:
        count+=1
    else: pass
if count==0:
    print("prime")
else:
    print("not prime")
    