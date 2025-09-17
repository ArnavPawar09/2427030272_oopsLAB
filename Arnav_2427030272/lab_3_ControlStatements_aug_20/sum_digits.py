# wap to calculate sum of digits of a number

n=int(input("enter n : "))
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum+=rem
print("sum of digits =", sum)