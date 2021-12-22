num = int(input("Enter a number: "))

if num % 2 == 0 and num % 4 == 0:
    print("Your number is even and a multiple of 4")
elif num % 2 == 0:
    print("your number is even!")
else:
    print("Your number is odd")

num1, num2 = int(input("Enter a number: ")), int(input("Enter a second number: "))

factor = num1 / num2
if factor % 1 == 0:
    print("Your second number {1} divides evenly into the first number {0}".format(num1, num2))
else:
    print("Wtf")