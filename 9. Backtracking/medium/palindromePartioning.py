# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def isPalindrome(self, s, i, j):
        for i in range(len(s) // 2):
            if s[i] != s[j]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def dfs(i):
            # no choices left or wrong choice
            if i >= len(s):
                res.append(partition[:])
                return

            # traverse all substrings
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i: j + 1])
                    dfs(j + 1)
                    partition.pop()
        dfs(0)
        return res
