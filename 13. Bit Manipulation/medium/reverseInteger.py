# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        MIN = -2147483648
        MAX = 2147483648

        while x:
            lastDigit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or MAX % 10 < lastDigit and MAX // 10 == res:
                return 0
            if res < MIN // 10 or MIN % 10 > lastDigit and MIN // 10 == res:
                return 0
            res = (res * 10) + lastDigit
        return res
