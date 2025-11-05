# Selection Sort

l = [5, 4, 3, 2, 1]
n = len(l)
for i in range(0, n-1):
    min_index = i
    for j in range(i+1, n):
        if l[j] < l[min_index]:
            min_index = j
    min_value = l.pop(min_index)
    l.insert(i, min_value)
print("Selection Sort :", l, "\n")
