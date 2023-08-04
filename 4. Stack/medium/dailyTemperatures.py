# https://leetcode.com/problems/daily-temperatures/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # contains indexes of temperatures that are lesser than current temp
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while len(stack) > 0 and temperatures[stack[len(stack) - 1]] < currTemp:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result


s = Solution()

assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
    1, 1, 4, 2, 1, 1, 0, 0]
assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
assert s.dailyTemperatures([10]) == [0]
