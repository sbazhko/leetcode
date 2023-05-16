# https://leetcode.com/problems/length-of-last-word/

import re


class Solution:
    # with regular exp
    # def lengthOfLastWord(self, s: str) -> int:
    #     words = re.findall(r'[^ ]+', s)
    #     return len(words[-1])
    
    # def lengthOfLastWord(self, s: str) -> int:
    #     words = s.split()
    #     return len(words[-1])

    def lengthOfLastWord(self, s: str) -> int:
        i, wordLen = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while s[i] != " ":
            wordLen += 1
            i -= 1
        return wordLen

s = Solution()
print(s.lengthOfLastWord('Hello World'))
print(s.lengthOfLastWord('  fly me    to   the   moon   '))
print(s.lengthOfLastWord('luffy is still joyboy'))