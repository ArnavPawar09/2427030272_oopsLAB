#5 check palindrome

s = input("enter string : ")
rev = s[::-1]
if (s==rev):
    print("palindrome")
else:
    print("not palindrome")