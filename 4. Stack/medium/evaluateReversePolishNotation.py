# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = set(['+', '-', '*', "/"])
        stack = []
        for token in tokens:
            if token not in signs:
                stack.append(int(token))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = 0
                if token == '*':
                    res = num2 * num1
                elif token == '/':
                    res = num2 / num1
                elif token == '+':
                    res = num2 + num1
                else:
                    res = num2 - num1
                stack.append(int(res))
        return stack.pop()


s = Solution()

assert s.evalRPN(["18"]) == 18
assert s.evalRPN(["0", "3", "/"]) == 0
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*",
                 "/", "*", "17", "+", "5", "+"]) == 22
