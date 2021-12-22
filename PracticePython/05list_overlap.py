l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

l3 = []
for i in l1:
    for y in l2:
        if i == y:
            l3.append(i)
print(l3)

print([i for y in l2 for i in l1 if i == y])
