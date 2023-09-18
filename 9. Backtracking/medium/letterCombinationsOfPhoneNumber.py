# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        res = []
        digitToCh = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'prqs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(digitIdx, combination):
            if digitIdx >= len(digits):
                res.append(combination[:])
                return
            for ch in digitToCh[digits[digitIdx]]:
                dfs(digitIdx + 1, combination + ch)
        dfs(0, "")
        return res


s = Solution()
s.letterCombinations('23')
