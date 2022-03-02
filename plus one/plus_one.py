class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dummy=""
        dummy=dummy.join(map(str,digits))
        return( list(map(int, list(str(int(dummy)+1)))) )
