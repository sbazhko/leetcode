# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     LCP = strs[0]
    #     for i in range(len(strs)):
    #         currStr = strs[i]

    #         j, maxWordLen = 0, min(len(LCP), len(currStr))
    #         currLCP = ""
    #         while j < maxWordLen:
    #             if LCP[j] != currStr[j]:
    #                 break
    #             currLCP += currStr[j]
    #             j += 1
    #         LCP = currLCP
    #     return LCP
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["flower"]))
print(s.longestCommonPrefix(["flower", "flow", ""]))
print(s.longestCommonPrefix(["flower", "flow", "ac"]))
print(s.longestCommonPrefix(["reflower","flow","flight"]))