# https://leetcode.com/problems/is-subsequence/

class Solution:
    # Time O(n) Space O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        charsMatched = 0
        if len(s) == 0:
            return True
        if len(s) > len(t): 
            return False
        for i in range(len(t)):
            if s[charsMatched] == t[i]:
                charsMatched = charsMatched + 1
                if charsMatched == len(s):
                    return True
        return False
    

s =  Solution()
print(s.isSubsequence("acb", "ahbgdc"))
print(s.isSubsequence("adb", "sdafdppbsda"))
print(s.isSubsequence("", "sdafdppbsda"))