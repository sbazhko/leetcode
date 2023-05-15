# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List


class Solution:
    # Time Limit Exceeded (O(n^2)):
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     for i in range(len(arr)):
    #         localMax = -1
    #         for j in range(i + 1, len(arr)):
    #             if i + 1 != len(arr):
    #                 localMax = max(localMax, arr[j])
    #         arr[i] = localMax
    #     return arr
    
    # Time: O(n); Space O(1)
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     def replaceElementsHelper(posStart, posEnd):
    #         if posStart == posEnd:
    #             last = arr[posEnd]
    #             arr[posEnd] = -1
    #             return last
    #         prevMax = replaceElementsHelper(posStart + 1, posEnd)
    #         curr = arr[posStart]
    #         arr[posStart] = prevMax
    #         return max(prevMax, curr)
    #     replaceElementsHelper(0, len(arr) - 1)
    #     return arr

    # Time: O(n); Space O(1)
    def replaceElements(self, arr: List[int]) -> List[int]:
        # go in reverse order
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            nextMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = nextMax
        return arr        

s = Solution()
print(s.replaceElements([1, 2, 3, 4, 5])) # [5, 4, 3, 2, -1]
print(s.replaceElements([17, 18, 5, 4, 6, 1])) # [18, 6, 6, 6, 1, -1]
# print(s.replaceElements([])) # []
print(s.replaceElements([1])) # [-1]