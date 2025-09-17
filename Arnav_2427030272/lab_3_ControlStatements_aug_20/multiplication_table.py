# show multiplication table of a no given by user

n = int(input("enter n : "))
print("\ntable of", n, ":")
for i in range(1, 11, 1):
    print(n, "x", i, "=", n*i)