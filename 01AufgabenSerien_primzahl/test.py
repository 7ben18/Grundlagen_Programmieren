names = ['John', 'Danny', 'Tyrion', 'Sam']
powers = ['Sales', 'Marketing', 'IT', 'Human Resource']
marks  = [20, 10, 5, 40]

zipped_iterator = zip(names, powers, marks)

# Converting iterator to list
zipped_values = list(zipped_iterator)
print(zipped_values)

import math

x = 0

for k in range(8):
    x += math.factorial(4 * k) * (1103 + 26390 * k) / (math.factorial(k) ** 4 * 396 ** (4 * k))
    pi = (99 ** 2) / (2 * math.sqrt(2) * x)

    print("Annäherung an pi mit {0}. Reihe : {1}").format(k, pi)