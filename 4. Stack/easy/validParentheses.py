# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        seenBrackets = []
        for ch in s:
            if ch in brackets:
                seenBrackets.append(brackets[ch])
            else:
                if len(seenBrackets) == 0:
                    return False
                bracket = seenBrackets.pop()
                if ch != bracket:
                    return False
        return len(seenBrackets) == 0


s = Solution()

assert s.isValid("[") == False
assert s.isValid("]]]") == False
assert s.isValid("()[]{}") == True
assert s.isValid("()") == True
assert s.isValid("())") == False
assert s.isValid("(]") == False
assert s.isValid("((])]") == False
