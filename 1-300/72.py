# 72.编辑距离
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
# 示例1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')

class Solution:
    def minDistance(self, word1, word2):
        m1, m2 = len(word1), len(word2)
        matrix = [[0 for i in range(m1+1)] for i in range(m2+1)]
        for i in range(1, m2+1):
            matrix[i][0] = matrix[i-1][0] + 1
        for j in range(1, m1+1):
            matrix[0][j] = matrix[0][j-1] + 1

        for i in range(1, m2+1):
            for j in range(1, m1+1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else :
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return matrix[-1][-1]






s = Solution()
result = s.minDistance("horse","ros")
print(result)