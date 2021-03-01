# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

class Solution:
    def rob(self, nums):
        def dp(nums, start):
            if start >= len(nums):
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums, start + 1), nums[start] + dp(nums, start + 2))
            memo[start] = res
            return res

        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1] * n
        a = [0] * n
        b = [0] * n
        for i in range(len(nums)):
            a[i] = nums[i]
            b[i] = nums[i]
        del a[len(nums) -1]
        del b[0]

        a_result = dp(a, 0)
        memo = [-1] * n
        b_result = dp(b,0)
        return max(a_result,b_result)
s = Solution()
result = s.rob([1])
print(result)