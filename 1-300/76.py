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
        tlens, slens = len(t), len(s)
        if (slens == 0 or tlens == 0 or slens < tlens):
            return ""
        left, right = 0, 0
        freqs, freqt = {}, {}

        # 初始化数组S,T每个字母
        for c in s:
            if c not in freqs:
                freqs[c] = 0
            if c not in freqt:
                freqt[c] = 0

        # 统计数组T每个字母的频数
        for c in t :
            if c not in freqt:
                return ""
            freqt[c] += 1



        # 滑动窗口内部包含多少个t中的字符，且对应字符频数超过不重复计算
        freq_total = 0
        minlen = slens + 1
        begin = 0
        while(right < slens):
            if (freqt[s[right]] == 0):
                right += 1;
                continue
            if (freqs[s[right]]< freqt[s[right]]):
                freq_total += 1

            freqs[s[right]] += 1
            right += 1

            while (freq_total == tlens):
                if (right - left < minlen):
                    minlen = right - left
                    begin = left
                if (freqt[s[left]] == 0):
                    left += 1;
                    continue
                if (freqs[s[left]] == freqt[s[left]]):
                    freq_total -= 1

                freqs[s[left]] -= 1
                left += 1

        if minlen == slens + 1:
            return ""
        else:
            return s[begin : begin+minlen]

s = Solution()
result = s.minWindow("A","B")
print(result)