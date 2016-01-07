# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(num):
    """
   :rtype : boolean
    """
    nums = str(num)

    # Recursive stopping rule: a one-digit number is a palindrome; two-digits are if both digits match
    if len(nums) == 1 | 0:
        print("true")
        return True

    elif len(nums) == 2:
        if nums[0] == nums[1]:
            print("true")
            return True
            
        else:
            print("false")
            return False

    else:
        if nums[0] == nums[len(nums) - 1]:
            nums = nums[1:len(nums) - 1]
            palindrome(nums)
            
        else:
            print("false")
            return False

# Test cases:
mylist = [90109, 0, 401, 33, 696, 100, 2442, 35653, 190]

for x in mylist:
    print(x)
    palindrome(x)
