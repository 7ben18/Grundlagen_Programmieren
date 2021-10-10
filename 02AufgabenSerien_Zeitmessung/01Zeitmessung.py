import datetime

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n,1): # is is 2 until n
            if n % i == 0: # 4 % 2 == 0 -> 4 is not a prime!
                return False
        else:
            return True

def all_primes_comprehension(n):
    return [i for i in range(2,n) if is_prime(i)]


start = datetime.datetime.now()
print(all_primes_comprehension(1000))
dur = (datetime.datetime.now() - start)

time_in_seconds = (dur.microseconds + 10 ** 6 * dur.total_seconds()) / 10 ** 6
print(time_in_seconds)