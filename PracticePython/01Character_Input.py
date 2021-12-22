age = int(input("Enter your age: "))
name = input("Enter your name: ")

yearnow = 2021
year_100 = yearnow + (100 - age)

print("Hi " + name + ", you will turn 100 in year: " + str(year_100))

nums = int(input("Enter a number: "))
cnt = 0
while cnt <= nums:
    print("Hi {0}, you will turn 100 in year: {1}".format(name, str(year_100)))
    cnt += 1