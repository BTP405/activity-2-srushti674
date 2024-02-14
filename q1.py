# Helper function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to get prime numbers up to n

def getPrimeNumbers(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

# for example:

result = getPrimeNumbers(20)
print(result)
