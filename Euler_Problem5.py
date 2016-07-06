from numpy import unique

"""
Project Euler Problem #5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Borrowed from my solution to Project Euler #3:
def isPrime(number):
    base = 2
    while (base < number):
        if (number % base == 0):
            return False
        elif (number % base != 0):
            base += 1
    return True


def smallestMultiple(start, stop):
    primelist = []
    nonprime=[]
    remainders=[]
    product = 1

    for x in range(start, stop):
        if isPrime(x):
            primelist.append(x)
        else:
            nonprime.append(x)

    # All primes must be included for number to be divisible by them
    for i in range(1, len(primelist)):
        product = product*primelist[i]

    # For non-primes, check to see if # is already divisible; if not, add to product, but divide by prod % nonprime #
    for i in range(0, len(nonprime)):

        # if already divisible, don't need to add
        if(product % nonprime[i] == 0):
          continue

        # else, multiply by the product, but divide by the remainder of (product/nonprime[i])
        elif(product % nonprime[i] !=0):
            product= (product*nonprime[i])/(product %nonprime[i])

    return product

# Test on both inputs
x = smallestMultiple(1,11)
y = smallestMultiple(1,21)
print(x, '\n', y)
