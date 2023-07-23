# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True


s = Solution()

assert s.validPalindrome("") == True
assert s.validPalindrome(" ") == True
assert s.validPalindrome("a") == True
assert s.validPalindrome("ab") == True
assert s.validPalindrome("aba") == True
assert s.validPalindrome("abac") == True
assert s.validPalindrome("abacd") == False
assert s.validPalindrome("eeccccbebaeeabebccceea") == False
assert s.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True
