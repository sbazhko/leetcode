# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        l = 0
        r = len(values) - 1
        ans = -1
        while l <= r:
            m = (r + l) // 2
            if values[m][1] <= timestamp:
                ans = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("love", "high-", 0)
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)
assert timeMap.get("love", 10) == "high"
assert timeMap.get("love", 5) == "high-"
assert timeMap.get("love", 15) == "high"
assert timeMap.get("love", 20) == "low"
assert timeMap.get("love", 25) == "low"
