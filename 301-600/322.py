# 322.零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。
#
# 你可以认为每种硬币的数量是无限的。
#
# 示例：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins, amount) -> int:
        array = [0] * (amount+1)
        if amount == 0: return 0
        if amount < min(coins):
            return -1
        return self.coinNumber(array, coins,amount)


    def coinNumber(self, array, coins, amount):
        if amount == 0: return 0
        if amount <0 : return -1
        if array[amount] != 0 : return array[amount]
        res = float('INF')
        for coin in coins:
            subproblem = self.coinNumber(array, coins, amount-coin)
            if subproblem == -1 : continue
            res = min(res, 1 + subproblem)
            array[amount] = res
        return  res if res != float('INF') else -1


# 测试
t = Solution()
result = t.coinChange([53,44,25,5,9,12,76], 8353)
print(result)


# 优化后代码
class Solution:
    def coinChange(self, coins, amount) -> int:
        def dp(n):
            # base case
            if n == 0:
                return 0
            elif n < 0:
                return -1
            else:
                res = float("inf")
                for coin in coins:
                    subproblem = dp(n - coin)
                    if subproblem == -1:
                        continue
                    res = min(res, subproblem + 1)
                return res if res != float("inf") else -1
        return dp(amount)