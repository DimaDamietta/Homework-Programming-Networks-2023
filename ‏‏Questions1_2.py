primes = [num for num in range(1, 1000) if all(num % i != 0 for i in range(2, num//2))]

print(primes)
