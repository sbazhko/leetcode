# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        chToW = {}
        wToCh = {}
        for i in range(0, len(words)):
            if pattern[i] in chToW and chToW[pattern[i]] != words[i]:
                return False
            if words[i] in wToCh and wToCh[words[i]] != pattern[i]:
                return False
            chToW[pattern[i]] = words[i]
            wToCh[words[i]] = pattern[i]
        return True


s = Solution()

assert s.wordPattern("abba", "dog dog dog dog") == False
assert s.wordPattern("abba", "dog cat cat dog") == True
assert s.wordPattern("abba", "dog cat cat fish") == False
assert s.wordPattern("aaaa", "dog cat cat dog") == False
