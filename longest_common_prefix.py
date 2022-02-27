class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size=len(strs)
        if size==0:
            return ""
        elif size==1:
            return strs[0]
        answer=""
        final_answer=""
        for i in range(len(strs[0])):
            answer=final_answer+strs[0][i]
            for j in range(size):
                if strs[j].find(answer)!=0:
                    return(final_answer)
            final_answer=answer
        return(final_answer)
