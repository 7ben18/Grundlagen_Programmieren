l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_l = []
for el in l:
    if el < 5:
        new_l.append(el)
print(new_l)

print([el for el in l if el < 5])

userinput = int(input("write a number: "))
print([el for el in l if el < userinput])
