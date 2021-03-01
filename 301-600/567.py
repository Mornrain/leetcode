
class Solution:
    def checkInclusion(self, s1, s2):
        left = 0
        win_freq = len(s1)
        array_s1, array_s2 = {}, {}
        for c in s1 :
            array_s2[c] = 0
            if c not in array_s1:
                array_s1[c] = 0
                array_s1[c] += 1
            else:
                array_s1[c] += 1

        if(len(s1) > len(s2)):
            return False

        while(left + win_freq <= len(s2)):
            win_left = left

            match, match_word =0, array_s2.copy()
            while (s2[win_left] in s1 and match_word[s2[win_left]] < array_s1[s2[win_left]]):
                match_word[s2[win_left]] += 1
                win_left += 1
                match += 1
                if (match == len(s1)):
                    return True
            left += 1
        if (left + win_freq == len(s2) + 1):
            return False
        else:
            return True

s = Solution()
result = s.checkInclusion("ros", "horse")
print(result)