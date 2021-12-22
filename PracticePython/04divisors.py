usernum = int(input("Write a number: "))

l = list(range(1, usernum + 1))

print([el for el in l if usernum % el == 0])
