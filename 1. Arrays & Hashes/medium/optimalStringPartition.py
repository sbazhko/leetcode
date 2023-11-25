# https://leetcode.com/problems/optimal-partition-of-string/
class Solution:
    def partitionString(self, s: str) -> int:
        numberOfUniqueStrs = 0
        uniqueCh = set()
        for ch in s:
            if ch in uniqueCh:
                numberOfUniqueStrs += 1
                uniqueCh.clear()
            uniqueCh.add(ch)
        return numberOfUniqueStrs + 1