__author__ = 'christine'
from math import sqrt

''' A Pythagorean triplet is a set of 3 natural numbers, a < b < c, which a^2 + b^2 = c^2.
There exists exactly one for which a + b + c = 1000. Find the product abc.'''

# Test to see if a tuple is a pythagorean triplet
def ispythtriplet(a, b, c):
    if (a < b < c) & (a ** 2 + b ** 2 == c ** 2):
        return True
    else:
        return False


test1 = ispythtriplet(2, 4, 5)
test2 = ispythtriplet(3, 4, 5)
print(test1, test2)

# Test to see if 3 numbers sum to 1000
def sumsup(a, b, c):
    """
    :type a, b, c: float
    :rtype : bool

    """
    if a + b + c == 1000:
        return True
    else:
        return False


perfectSquares = []
a = 0

for i in range(1, 1000):
    if sqrt(i) % 1 == 0:
        perfectSquares.append([a, i])
        a += 1

print(perfectSquares[0:len(perfectSquares)])

for i in range(len(perfectSquares) - 1, 2, -1):
    c = perfectSquares[i - 0]
    b = perfectSquares[i - 1]
    a = perfectSquares[i - 2]

    if a + b + c == 1000:
        print("yes")