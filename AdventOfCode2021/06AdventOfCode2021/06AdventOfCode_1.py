def einlesen(data):
    with open(data) as f:
        return [int(x) for x in f.readline().split(",")]


testdata = einlesen("06testdata")
data = einlesen("06data")

day_counter = 0
end_day = 80

while day_counter <= end_day:
    print("After {0} days: {1}".format(day_counter, data))
    print("Numbers of lanternfish: {0}, after {1} days".format(len(data), day_counter))

    sublist = []
    for x in data:
        if x != 0:
            x -= 1
            sublist.append(x)
        elif x == 0:
            x,y = 6, 8
            sublist.append(x)
            sublist.append(y)
    data = sublist
    day_counter += 1


