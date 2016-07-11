'''The four adjacent digits in the 1000-digit number that have the greatest product are 9*9*8*9= 5832.
Find the 13 adjacent digits in the 1000-digit # that have the greatest product. What is the value of this product?'''

# Save the given input as a .txt file, and import; cast each char to int.
input = "pathToInput/pe8_input.txt"
file=open(input,'r')
inArray = []

for line in file: # read rest of lines
    for char in line:
        if(char != "\n"):
            inArray.append(int(char))

def maxProduct(inputArray, lowIndex, highIndex, maxSoFar):

    while(highIndex < len(inputArray)):
        product= 1
        for i in range(lowIndex, highIndex+1):
            print(product)
            product *= float(inputArray[i])

        if(product > maxSoFar):
            maxSoFar = product

        lowIndex += 1
        highIndex +=1

    return maxSoFar


a =maxProduct(inArray, 0,3,1)
b = maxProduct(inArray, 0, 12, 1)
print(a, b)

# 5832.0 23514624000.0
