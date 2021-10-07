names = ['John', 'Danny', 'Tyrion', 'Sam']
powers = ['Sales', 'Marketing', 'IT', 'Human Resource']
marks  = [20, 10, 5, 40]

zipped_iterator = zip(names, powers, marks)

# Converting iterator to list
zipped_values = list(zipped_iterator)
print(zipped_values)