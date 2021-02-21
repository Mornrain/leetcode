# 最小覆盖字串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"

class Solution:
    def minWindow(self, s, t):
        start, min_length, min_length_left = 0, float('inf'), float('inf')
        left, right = 0, 0
        needs =  {}
        for c in t :
            if c not in needs :
                needs[c] = 1
        while(right <= len(s)):
            temp_array = {}
            temp = right - left
            if temp < len(t):
                right += 1
                continue
            else:
                for c in s[left:right]:
                    aa = s[left:right]
                    if c in needs:
                        if c not in temp_array:
                            temp_array[c] = 1
                        else:
                            temp_array[c] += 1
                match = 0
                for c in needs:
                    if c not in temp_array:
                        right += 1
                        break
                    elif needs[c] <= temp_array[c]:
                        match += 1
                    else:
                        right += 1
                        break
                if (match == len(needs)):
                    res = right - left
                    # min_length = min(min_length,res)
                    if min_length > res:
                        min_length_left = left
                        min_length = res
                    left += 1
        min_length_right = min_length_left + min_length
        if min_length == float('inf'):
            return ""
        else:
            return s[min_length_left: min_length_right]

s = Solution()
result = s.minWindow("ADOBECODEBANC","BAC")
print(result)