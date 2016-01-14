"""
Project Euler Problem #5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Any number divisible by 10 will also be divisible by 5 and 2
#Any number divisible by 8 will also be divisible by 4 and 2
#Primes= 7, 5, 3, 2


# 2520 = 5*7*(2*4)*(2*3) = 5*7*8*6

print(5*7*8*6)


#primes


#Borrowed from my solution to Project Euler #3:
def isPrime(number):
    base = 2
    while (base < number):
        if (number % base == 0):
            return False
        elif (number % base != 0):
            base += 1
    return True
