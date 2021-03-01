# 188. 买卖股票的最佳时机 IV
# 给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0:
            return 0
        if k == 0:
            return 0
        buy = [-prices[0]] * k
        sell = [0] * k
        for i in range(1,n):
            for j in range (0, k):
                if j == 0:
                    buy[j] = max(buy[j], -prices[i])
                else:
                    buy[j] = max(buy[j], sell[j-1]-prices[i])
                sell[j] = max(sell[j], buy[j]+prices[i])
        return sell[k-1]
s = Solution()
result = s.maxProfit(2,[3,2,6,5,0,3])
print(result)