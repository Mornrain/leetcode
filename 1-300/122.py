# 122. 买卖股票的最佳时机 II
# 给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy_prices = -1
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                if buy_prices == -1:
                    buy_prices = prices[i]
            elif buy_prices != -1:
                profit =profit + prices[i] - buy_prices
                buy_prices = -1
        if prices[len(prices)-1] > prices[len(prices)-2]:
            profit = profit + prices[len(prices)-1] - buy_prices
        return profit


s = Solution()
result = s.maxProfit([2,1,2,1,0,1,2])
print(result)