# 300.最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

class Solution:
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        max_len = 0
        for i in range(0, len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        for i in range(0, len(nums)):
            if dp[i] > max_len:
                max_len = dp[i]
        return max_len

s = Solution()
result = s.lengthOfLIS([0])
print(result)