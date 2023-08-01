# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2 ** 32

    def push(self, val: int) -> None:
        stackLen = len(self.stack)
        if stackLen != 0:
            self.min = min(self.stack[len(self.stack) - 1][1], val)
        else:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3  # return -3
minStack.pop()
assert minStack.top() == 0    # return 0
assert minStack.getMin() == -2  # return -2

minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
assert minStack.getMin() == 0
minStack.pop()
assert minStack.getMin() == 0
