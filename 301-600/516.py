# 516.最长回文子序列
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[ 0 for n in range(len(s))] for n in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if (s[i] == s[j]):
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][len(s)-1]

s = Solution()
result = s.longestPalindromeSubseq("heorose")
print(result)