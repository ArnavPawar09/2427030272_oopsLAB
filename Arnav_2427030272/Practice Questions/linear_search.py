l = [1, 2, 3, 4, 5] # can be sorted or not sorted
s = int(input("search element : "))
for i in l:
    if (i==s):
        print(s,"found at index",l.index(i))
        found = True
        break
    else: found = False
if found==False: print("not found")