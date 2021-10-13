def eratosthenes(n):
    zahlenliste = []
    primezahlen = []
    for z in range(2,n,1):
        zahlenliste.append(z)

    for i in range(2,n,1):
        if i in zahlenliste:
            primezahlen.append(i)
            zahlenliste.remove(i)
        for a in zahlenliste:
            if a % i == 0:
                zahlenliste.remove(a)
    return primezahlen

def distances(primes):
    distance = []
    for x in range(0,len(primes)-1,1):
        diff = (primes[x+1] - primes[x])
        #diff = abs(diff)
        distance.append(diff)
    return distance

print(distances(eratosthenes(100)))

def heuristic(n):
    prime_numbers = n

    number_of_distances_list = [] # prime_numbers as set
    number_of_distances_set = set(n)
    for num in number_of_distances_set:
        number_of_distances_list.append(num)
    number_of_distances_list.sort() # Sorted ascending

    counted_number = [] # counted numbers in prime_numbers
    for i in number_of_distances_list:
        count = prime_numbers.count(i)
        counted_number.append(count)

    result = zip(number_of_distances_list, counted_number)
    return list(result)

print(heuristic(distances(eratosthenes(100))))

