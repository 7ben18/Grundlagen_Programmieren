a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 100]

b = [x for x in a if x % 2 == 0]
print(b)

# Weitere Comprehensions
# comprehension obejct
comobject = ((5 * x + 1 for x in a))
print(comobject)
print(list(comobject))

# set comprehension
setcomprehension = set((3 * x for x in a))
print(setcomprehension)

# tupple comprehension
tupplecomprehension = tuple((2 * x for x in a if x % 2 != 0))
print(tupplecomprehension)

# dictionary comprehension
dictcomprehension = {x:y for x in range(len(a)) for y in a}
print(dictcomprehension)

# Comprehension with sum
a = [10, 10, 10, 20, 30, 40, 40, 10, 20]
summeunique = sum((x for x in a if a.count(x) == 1))
print(summeunique)