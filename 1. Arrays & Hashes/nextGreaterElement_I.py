# https://leetcode.com/problems/next-greater-element-i/

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterMap = {}
        # Will keep elements that are less than current (closest in the array to the ones that are added) or we pop elements until the condition is true
        decreasingMonotonicStack = []
        nextGreaterElementsForNum1 = []
        for num in nums2:
            while len(decreasingMonotonicStack) and num > decreasingMonotonicStack[-1]:
                el = decreasingMonotonicStack.pop()
                nextGreaterMap[el] = num
            decreasingMonotonicStack.append(num)
        for num in nums1:
            if num not in nextGreaterMap:
                nextGreaterElementsForNum1.append(-1)
                continue
            nextGreaterElementsForNum1.append(nextGreaterMap[num])
        return nextGreaterElementsForNum1


s = Solution()

print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1, 3, -1]
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3, -1]
print(s.nextGreaterElement([5, 4, 1, 10], [7, 5, 4, 1, 10]))  # [3, -1]
