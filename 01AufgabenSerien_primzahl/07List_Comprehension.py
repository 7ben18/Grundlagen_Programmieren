lst1 = sum((x for x in range(10)))
print(lst1)

lst2 = [x for x in range(10)]
print(lst2)

lst3 = ((2 * x for x in range(10)))
print(lst3)

lst4 = tuple((2 * x for x in range(10)))
print(lst4)

lst5 = set((2 * x for x in range(10)))
print(lst5)

lst6 = {x * 2: x for x in range(10)}
print(lst6)

def add(n):
    return n + 10

lst7 = [add(x) for x in range(10)]
print(lst7)
