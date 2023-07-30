# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        charFreq = {}
        for ch in s1:
            charFreq[ch] = charFreq.get(ch, 0) + 1

        charMatchesLeft = len(charFreq)
        b = 0
        e = len(s1)
        for i in range(len(s1)):
            ch = s2[i]
            if ch in charFreq:
                charFreq[ch] -= 1
                if charFreq[ch] == 0:
                    charMatchesLeft -= 1
        if charMatchesLeft == 0:
            return True
        while e < len(s2):
            chb = s2[b]
            if chb in charFreq:
                charFreq[chb] += 1
                if charFreq[chb] == 1:
                    charMatchesLeft += 1
            che = s2[e]
            if che in charFreq:
                charFreq[che] -= 1
                if charFreq[che] == 0:
                    charMatchesLeft -= 1
            if charMatchesLeft == 0:
                return True
            b += 1
            e += 1
        return False


s = Solution()

assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("a", "ab") == True
assert s.checkInclusion("ab", "a") == False
assert s.checkInclusion("ab", "eidboaoo") == False
assert s.checkInclusion("abbc", "eidcbacbbaoaoo") == True
assert s.checkInclusion("abbc", "eidcbaaaacbaoaoo") == False
assert s.checkInclusion("trinitrophenylmethylnitramine",
                        "dinitrophenylhydrazinetrinitrophenylmethylnitramine") == True
