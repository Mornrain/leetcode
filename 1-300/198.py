# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

class Solution:
    def rob(self, nums):
        def dp(nums, start):
            if start >= len(nums):
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums, start + 1), nums[start] + dp(nums,start + 2))
            memo[start] = res
            return res
        n = len(nums)
        memo = [-1] * n
        return dp(nums, 0)

s = Solution()
result = s.rob([2,7,9,3,1])
print(result)