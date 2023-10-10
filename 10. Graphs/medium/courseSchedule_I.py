# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            prereqMap[crs].append(prereq)

        visited = set()

        def dfs(crs):
            if crs in visijjted:
                return False
            if prereqMap[crs] == []:
                return True

            visited.add(crs)
            for prereq in prereqMap[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            prereqMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
