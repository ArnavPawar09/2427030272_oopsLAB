#4 count vowels

s = input("enter string : ")
count = 0
for i in s:
    if (i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
        count+=1
    else:
        pass
print("no of vowels =", count)