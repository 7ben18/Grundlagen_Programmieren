"""
they need you to find the two entries that sum to 2020 and then multiply those two numbers together
"""

numbers = []
with open("expense_report") as f:
    numbers = list(map(int, f.readlines()))
print(numbers)

def get2num():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[j] + numbers[i] == 2020:
                return numbers[i], numbers[j], numbers[i] * numbers[j]

num = get2num()
print(num)

def get3num():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[j] + numbers[i] + numbers[k] == 2020:
                    return numbers[i], numbers[j], numbers[k], numbers[i] * numbers[j] * numbers[k]

num2 = get3num()
print(num2)