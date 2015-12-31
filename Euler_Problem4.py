# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(num, counter):
    """

    :rtype : boolean
    """
    nums = str(num)

    # A one-digit number is a palindrome

    if len(nums) == 1 | 0:
            print("true")
            return True

    else:

            if nums[0] == nums[len(nums)-1]:
                counter += 1
                print(counter)
                temp = nums[counter:-1]
                print(temp)
                palindrome(nums[counter:-1], counter)
            else:
                print("false")
                return False



mynum = 90109
palindrome(mynum, 0)
