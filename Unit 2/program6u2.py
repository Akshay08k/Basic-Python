#checking the number is prime or not
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

#generating prime numbers
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
            print(primes)
    return primes

# Get prime numbers up to a certain limit, e.g., 50
limit = 50
prime_numbers = generate_primes(limit)

print("Prime numbers up to", limit, "are:")
print(prime_numbers)
