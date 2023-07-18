# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonChars = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in balloonChars:
                balloonChars[ch] += 1
        balloonChars['l'] = balloonChars['l'] // 2
        balloonChars['o'] = balloonChars['o'] // 2
        return min(balloonChars.values())


s = Solution()

assert s.maxNumberOfBalloons("nlaebolko") == 1
assert s.maxNumberOfBalloons("loonbalxballpoon") == 2
assert s.maxNumberOfBalloons("balloonballoonballon") == 2
assert s.maxNumberOfBalloons("balon") == 0
