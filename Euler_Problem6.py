
"""The sum of the squares of the first ten natural numbers is,
(1^2 + 2^2 + ... + 10^2) = 385

The square of the sum of the first ten natural numbers is,
(1+2+ ... +10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def calcDiff(low, high):
    sumSquares = 0
    sumSoFar = 0
    squareOfSum = 0
    assert isinstance(low, int)

    for i in range(low,high+1):
        sumSquares = sumSquares + (i**2)
        sumSoFar = sumSoFar + i

    squareOfSum = sumSoFar**2
    out =  squareOfSum - sumSquares
    return out

a= calcDiff(1,10)
b = calcDiff(1,100)
print(a, b)
