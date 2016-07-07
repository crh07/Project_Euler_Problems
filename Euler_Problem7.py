'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?'''

def isPrime(number):
  # Range is not inclusive in python [ , )
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def findXPrime(x):
    primeDictionary = dict()
    start = 2
    i=0
    while i < (x + 1):
        if isPrime(start):
            primeDictionary.update({i: start})
            i = i + 1
        start = start + 1

    return(primeDictionary.get(x-1))

# Test both
print(findXPrime(6), findXPrime(10001))
