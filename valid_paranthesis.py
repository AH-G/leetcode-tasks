class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_strings={
            "(": ")",
            "{": "}",
            "[": "]"
        }
        got_brackets=[]
        check=0
        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                got_brackets.append(s[i])
            elif s[i] in [")","}","]"]:
                if not got_brackets:
                    got_brackets.append(s[i])
                    break
                elif s[i] == brackets_strings[got_brackets[-1]]:
                    got_brackets.pop()
                else:
                    break
        if not got_brackets:
            return(True)
        else:
            return(False)
