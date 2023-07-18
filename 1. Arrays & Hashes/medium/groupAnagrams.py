# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    # O(m * n log n) == m times to sort by n log n
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            groupKey = "".join(sorted(str))
            if groupKey in groups:
                groups[groupKey].append(str)
            else:
                groups[groupKey] = [str]
        return groups.values()

    # O(m * n  * 26) => O (m * n)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            key = [0] * 26
            for ch in str:
                key[ord(ch) - ord('a')] += 1
            if tuple(key) in groups:
                groups[tuple(key)].append(str)
            else:
                groups[tuple(key)] = [str]
        return groups.values()


s = Solution()

print(s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams2([""]))
print(s.groupAnagrams2(["a"]))
