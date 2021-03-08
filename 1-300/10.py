# 10. 正则表达式匹配
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        def matches(i, j):
            if i == 0:
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j] or dp[i][j-2]
                    if matches(i, j - 1):        #判断p[j-2]情况
                        dp[i][j] = dp[i-1][j] or dp[i][j]
                else:
                    if matches(i,j):
                        dp[i][j] = dp[i][j] or dp[i-1][j-1]
        return dp[m][n]




s = Solution()
result = s.isMatch("aab","c*a*b")
print(result)