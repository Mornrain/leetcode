# 714. 买卖股票的最佳时机含手续费
# 给定一个整数数组prices，其中第i个元素代表了第i天的股票价格 ；非负整数fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        buy = -prices[0]
        sell = 0
        if not prices:
            return 0
        for i in range(n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell


s = Solution()
result = s.maxProfit([1, 3, 2, 8, 4, 9],2)
print(result)