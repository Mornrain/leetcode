# 28. 实现 strStr()实现strStr()函数。
#
# 给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1

class Solution:
    def strStr(self, haystack, needle):
        if needle == '': return 0
        n = len(needle)
        m = len(haystack)
        k = 0
        pnext = self.getnext(needle)
        for i in range(m):
            while k > 0 and haystack[i] != needle[k]:
                k = pnext[k]
            if haystack[i] == needle[k]:
                k += 1
                if k == n:
                    return i - n +1
        return -1

    def getnext(self, s):
        n = len(s)
        pnext = [0, 0]
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pnext[j]  # 指针跳跃
            if s[j] == s[i]:
                j += 1
            pnext.append(j)
        return pnext



s = Solution()
result = s.strStr("aaaaa","bba")
print(result)
