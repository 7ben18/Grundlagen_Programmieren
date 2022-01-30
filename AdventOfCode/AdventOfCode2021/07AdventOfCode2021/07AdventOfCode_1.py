with open("07testdata") as f:
    line = [int(x) for x in f.readline().split(",")]
#print(line)
# [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

fuel_list = []
for i in range(min(line),max(line)+1,1):
    fuel = 0
    for j in line:
        fuel += abs(i - j)
    fuel_list.append(fuel)

print(min(fuel_list))


fuel_list2 = min([sum([abs(i - j) for j in line]) for i in range(min(line),max(line)+1,1)])
print(fuel_list2)