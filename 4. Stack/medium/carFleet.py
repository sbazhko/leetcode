# https://leetcode.com/problems/car-fleet/

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetStack = []
        for [p, s] in sorted(zip(position, speed))[::-1]:
            arrivalTime = (target - p) / s
            fleetStack.append(arrivalTime)
            if len(fleetStack) >= 2 and fleetStack[-1] <= fleetStack[-2]:
                # don't need more than one car in fleet (we keep the one that has the furtherst position, because cars stack)
                fleetStack.pop()

        return len(fleetStack)


s = Solution()

assert s.carFleet(12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3
assert s.carFleet(10, position=[3], speed=[3]) == 1
assert s.carFleet(100, position=[0, 2, 4], speed=[4, 2, 1]) == 1
