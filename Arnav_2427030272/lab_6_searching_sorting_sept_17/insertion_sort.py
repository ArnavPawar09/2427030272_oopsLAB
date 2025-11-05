# insertion sort

l = [5, 4, 3, 2, 1]
n = len(l)
for i in range(1, n):
    insert_index = i
    current_value = l.pop(i)
    for j in range(i-1, -1, -1):
        if l[j] > current_value:
            insert_index = j
    l.insert(insert_index, current_value)
print("Insertion Sort :", l, "\n")