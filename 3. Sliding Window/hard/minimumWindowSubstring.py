# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        substringChars = {}
        for ch in t:
            substringChars[ch] = substringChars.get(ch, 0) + 1
        length = len(substringChars)

        begin = 0
        end = 0
        ans = ""
        minLen = 10 ** 6
        while end < len(s):
            if s[end] in substringChars:
                substringChars[s[end]] -= 1
                if substringChars[s[end]] == 0:
                    length -= 1
            while length == 0:
                if end - begin < minLen:
                    minLen = end - begin
                    ans = s[begin: begin + minLen + 1]

                if s[begin] in substringChars:
                    substringChars[s[begin]] += 1
                    if substringChars[s[begin]] > 0:
                        length += 1
                begin += 1
            end += 1

        return ans


s = Solution()

# print(s.minWindow("ADOBECODEBANC", "ABC"))  # == "BANC"
# print(s.minWindow("aa", "aa"))  # == "aa"
print(s.minWindow("cabwefgewcwaefgcf", "cae"))  # == "cwae"
# print(s.minWindow("a", "a"))  # == "a"
# print(s.minWindow("a", "b"))  # == ""
# assert s.minWindow("a", "aa") == ""
