class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        i=1
        current=0
        previous=roman[s[0]]
        number=previous

        while i < len(s):
            current=roman[s[i]]
            if current > previous:
                number=abs(number-previous+(current-previous))
            else:
                number=number+current
            previous=current
            i+=1
        return(number)
