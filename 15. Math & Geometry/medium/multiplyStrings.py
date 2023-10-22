# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        out = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                # account for something left in that position from previous iteration
                # => avoid 2-digit numbers
                posSum = out[i + j] + mul 
                out[i + j + 1] += (posSum // 10)
                out[i + j] = posSum % 10

        res = out[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
    
s = Solution()
assert s.multiply("123", "456") == "56088"