# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# ------------------#
# Define functions #
# -----------------_#

def palindrome(num):
    """
   :rtype : boolean
    """
    nums = str(num)

    # Recursive stopping rule: a one-digit number is a palindrome; even numbers will result in an empty string

    if len(nums) == 1 | 0:
        print("True")
        return True

    elif len(nums) == 2:
        if nums[0] == nums[1]:
            print("True")
            return True

        else:
            # print("false")
            return False

    else:
        if nums[0] == nums[len(nums) - 1]:
            nums = nums[1:len(nums) - 1]

            # Recursive function call
            palindrome(nums)

        else:
            # print("false")
            return False


# Thought process here: most efficient would NOT be to brute force it.
# We can assume the correct answers will be in the range of 900 to 999

# Need to account for possibility that it might be the number times itself.


def findLargestPal(start):
    templist = []
    for i in range(start, 899, -1):
        for j in range(start, 899, -1):
            temp = i * j
            # print(i , j)
            print(temp)
            if palindrome(temp):
                templist.append(temp)
                print(temp)
                return templist



# Test cases for palindrome function:
mylist = [24, 90109, 0, 401, 33, 696, 100, 2442, 35653, 190]

for x in mylist:
    print(x)




list2 = [1]
list2= findLargestPal(999)

for x in list2:
    print(x)





#ANSWER IS: 906609
