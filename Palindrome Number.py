class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        if y[::-1]==y[0::]:
            return True
        else:
            return False
