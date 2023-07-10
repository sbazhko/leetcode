# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mappedTo = {}
        mappedFrom = {}
        for i in range(0, len(s)):
            if s[i] not in mappedTo:
                mappedTo[s[i]] = t[i]
                if t[i] in mappedFrom and mappedFrom[t[i]] != s[i]:
                    return False
                else:
                    mappedFrom[t[i]] = s[i]
            else:
                if mappedTo[s[i]] != t[i]:
                    return False
        return True


s = Solution()

print(s.isIsomorphic("egg", "add"))  # True
print(s.isIsomorphic("foo", "bar"))  # False
print(s.isIsomorphic("e", "a"))  # True
print(s.isIsomorphic("efa", "asa"))  # False
print(s.isIsomorphic("badc", "baba"))  # False
print(s.isIsomorphic("title", "paper"))  # True
