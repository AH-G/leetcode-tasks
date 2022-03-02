class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size_of_needle=len(needle)
        size_of_haystack=len(haystack)
        if not needle:
            return(0)
        elif not haystack:
            return(-1)
        if size_of_needle<size_of_haystack:
            i=0
            while i<=size_of_haystack-size_of_needle:
                j=0
                if haystack[i]==needle[j]:
                    check=i
                    while j<=size_of_needle-1:
                        if haystack[check]!=needle[j]:
                            break
                        elif j==size_of_needle-1:
                            return(i)
                        check+=1
                        j+=1
                if i==(size_of_haystack-size_of_needle):
                    return(-1)
                i+=1
        elif size_of_needle==size_of_haystack:
            if not needle:
                return(0)
            else:
                for i in range(size_of_needle):
                    if needle[i]!=haystack[i]:
                        return(-1)
                    elif i==size_of_needle-1:
                        return(0)
        else:
            return(-1)
