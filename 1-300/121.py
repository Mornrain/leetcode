# 121.买卖股票的最佳时机
# 给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i]-minprice)
        return maxprofit


s = Solution()
result = s.maxProfit([7,1,5,3,6,4])
print(result)