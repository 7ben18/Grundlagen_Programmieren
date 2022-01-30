with open("07data") as f:
    line = [int(x) for x in f.readline().split(",")]

fuel_list = []
for i in range(min(line),max(line)+1,1):
    fuel = 0
    for j in line:
        fuel += abs(i-j) * (abs(i-j) + 1) // 2
    fuel_list.append(fuel)

#print(fuel_list)
print(min(fuel_list))
