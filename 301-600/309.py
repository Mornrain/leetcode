# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第i个元素代表了第i天的股票价格 。
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        f0 = -prices[0]
        f1 = 0
        f2 = 0

        for i in range(1, n):
            profit0 = max(f2 - prices[i], f0)
            profit1 = f0 + prices[i]
            profit2 = max(f1, f2)
            f0, f1, f2 = profit0, profit1, profit2
        return max(f1, f2)

s = Solution()
result = s.maxProfit([1,2,3,0,2])
print(result)
