class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy=""
        i=-1
        while len(dummy)!=len(s):
            if s[-1]==" ":
                s=s[:-1]
            elif s[i] == " ":
                break
            else:
                dummy=dummy+s[i]
                i=i-1
        return(len(dummy))
