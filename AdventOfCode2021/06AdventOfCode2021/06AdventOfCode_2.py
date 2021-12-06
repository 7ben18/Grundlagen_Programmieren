def einlesen(daten):
    with open(daten) as f:
        return [int(x) for x in f.readline().split(",")]

testdata = (einlesen("06testdata"))
data = einlesen("06data")

print(testdata)

start_day = 0
endday = 18



