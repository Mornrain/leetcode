# n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
#
# 每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

class Solution:
    def solveQueens(self,n):
        res = []
        s = '.' * n
        print()

        def backtrack(path=[], i=0, col_selected=[], z_daig=set(), f_ziag=set()):
            if i == n:
                res.append(path)
                return
            for j in range(n):
                if j not in col_selected and i-j not in z_daig and i+j not in f_ziag:
                    backtrack( path +[ s[:j] + 'Q' + s[j+1:] ], i+1, col_selected + [j], z_daig|{i-j}, f_ziag|{i+j})

        backtrack()
        return res

t = Solution()
result = t.solveQueens(5)
print(result)