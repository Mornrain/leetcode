# 704.二分查找
# 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1

class Solution:
    def search(self,nums,target):
        left, right = 0, len(nums) - 1
        while (left <= right):
            if nums[left] == target:
                return left
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
t = Solution()
result = t.search([1,3,5,7,9,11,13,115], 13)
print(result)