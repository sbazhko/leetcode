# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    # O(n)
    def lengthOfLongestSubstring(self, str: str) -> int:
        s = 0
        e = 0
        longestSubstring = 0
        substring = set()
        while e < len(str):
            while str[e] in substring:
                substring.remove(str[s])
                s += 1

            substring.add(str[e])
            e += 1

            longestSubstring = max(longestSubstring, e - s)
        return longestSubstring


s = Solution()

assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("") == 0
assert s.lengthOfLongestSubstring("a") == 1
