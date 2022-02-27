class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_number = 0
        if x<(2**31)-1 and x>(-2**31):
            original=x
            if x >= 0:
                while x != 0:
                    dummy = x % 10
                    reversed_number = (reversed_number * 10) + dummy
                    x //= 10
                if reversed_number==original:
                    return(True)
                else:
                    return(False)
            elif x < 0:
                return(False)
        else:
            return(False)
