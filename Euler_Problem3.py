__author__ = 'ZJ5586B'
import math


# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# To solve, we need a function that allows us to check to see if a number is prime, and a way to rank all prime factors
# of a given parameter so that we can identify the largest one

# pseudocode (implement recursively):
# Start with a given number; divide the number by itself; if this number is prime, stop.
# Else, decrement the number by 1; take original % new; if == 0, check to see if new is prime.
# If new is prime, stop;
# Else, keep going; check each time to see if # is prime.

def isPrime(number):
    base = 2
    while (base < number):
        if (number % base == 0):
            return False
        elif (number % base != 0):
            base += 1
    return True

#Works, but is inefficient
def findLargestPrime(number2):
    temp = number2
    # print(temp)
    while temp >= 2:
       # print(temp)
        if number2 % temp == 0:
            if isPrime(temp):
                return temp
            else:
                temp -= 1
        else:
            temp -= 1
    return number2


#Works; will cause stackoverflow if you print the var each time
def findLPrime(number2):
    temp = 2
    list = []
    counter = 0
    # print(temp)
    while temp <= math.sqrt(number2):
       # print(temp)
        if number2 % temp == 0:
            if isPrime(temp):
                list.append(temp)
                counter += counter
                temp += 1
            else:
                temp += 1
        else:
            temp += 1
    return list[counter-1]

print(findLPrime(13195))
print(findLPrime(600851475143))

#Answer = 6857

