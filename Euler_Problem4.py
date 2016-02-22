# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# ------------------#
# Define functions  #
# -----------------_#

#palindrome returns TRUE if the parameter is a palindrome and FALSE if it is not
# @param: num = an integer to inspect
def palindrome(num):
    """
   :rtype : boolean
    """
    nums = str(num)

    # Recursive stopping rule: a one-digit number is a palindrome; even numbers will result in an empty string

    if len(nums) == 1| 0:
        #print("True")
        return True


    elif len(nums) == 2:
        if nums[0] == nums[1]:
            #print("True")
            return True

        else:
            # print("false")
            return False

    else:
        if nums[0] == nums[len(nums) - 1]:
            nums = nums[1:len(nums) - 1]


            # Note: in Python, for this recursive call to work, you can't just call the func; you have to include "return"
            # Otherwise, if it goes here, it will return "None"
            return palindrome(nums)

        else:
            # print("false")
            return False


# Thought process here: most efficient would NOT be to brute force it.
# We can assume the correct answers will be in the range of 900 to 999

# Need to account for possibility that it might be the number times itself.

# findLargestPal finds the largest palindrome that is the product of 2 three-digit numbers within a given range
# @param: start: an integer; represents the max you want to start with; each pass through the outer loop will decrement
# @param: num = an integer to inspect
def findLargestPal(start):
    """
       :rtype : int
    """
    templist = []
    mybool = False
    for i in range(start, 899, -1):
        for j in range(start, 899, -1):
            temp = i * j
            # print(i , j)
            # print(temp)
            if palindrome(temp):
                templist.append(temp)
                print(i, j, temp)
    return templist[0]


# Test cases for palindrome function:
mylist = [24, 90109, 0, 401, 33, 696, 100, 2442, 35653, 190, 990009]

for x in mylist:
 print(palindrome(x))

#Run the function, starting at 999 (largest 3 digit number)
print(findLargestPal(999))

#ANSWER IS: 906609
#Product of: 993 * 913
