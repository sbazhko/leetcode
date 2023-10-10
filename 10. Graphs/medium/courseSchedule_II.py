# https://leetcode.com/problems/course-schedule-ii/

from typing import List

# O(E + V) == O (Prereq + NumCourses)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Course states
        # Visited -> Course has been added to output
        # Visiting -> Course not added, but added to a cycle
        # Unvisited -> Course is not in the cycle or visited

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
