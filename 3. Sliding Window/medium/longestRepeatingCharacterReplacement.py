# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def findMostFreqCh(self, freqChars):
        mostFreq = 0
        for ch, freq in freqChars.items():
            mostFreq = max(mostFreq, freq)
        return mostFreq

    # Worst case : O(26*n)
    def characterReplacement(self, str: str, k: int) -> int:
        b = 0
        e = 0
        longestSubstring = 0
        freqChars = {}
        while e < len(str):
            freqChars[str[e]] = freqChars.get(str[e], 0) + 1

            mostFreqCh = self.findMostFreqCh(freqChars)
            windowSize = e + 1 - b
            if windowSize - mostFreqCh <= k:
                longestSubstring = max(longestSubstring, windowSize)
            else:
                freqChars[str[b]] -= 1
                b += 1
            e += 1
        return longestSubstring


s = Solution()

assert s.characterReplacement("AB", 2) == 2
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("ABAC", 2) == 4
assert s.characterReplacement("ABBB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("BBBBBAB", 1) == 7
