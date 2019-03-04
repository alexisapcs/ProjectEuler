##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##
##Find the largest palindrome made from the product of two 3-digit numbers.

def largePali():
    biggest = 0
    for y in range(1000):
        for x in range(1000):
            if isPalindrome(str(y*x)):
                if y*x > biggest:
                    biggest = y*x
    return biggest

def isPalindrome(sWord):
    if reverse(sWord) == sWord:
        return True
    return False

def reverse(sWord):
  return sWord[::-1];


print(999*999)
print(largePali())
