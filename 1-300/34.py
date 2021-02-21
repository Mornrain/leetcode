# 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回[-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？

class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums)
        if len(nums) == 0 :
            return [-1, -1]
        # elif len(nums) == 1 and nums[0] == target:
        #     return [0, 0]
        # elif len(nums) == 1 and nums[0] != target:
        #     return [-1, -1]
        while( left < right ):
            mid = left + (right - left ) // 2
            if ( nums[mid] < target ):
                left = mid + 1
            elif ( nums[mid] >= target):
                right = mid
        # left -= 1
        if  left >= len(nums):
            left_position = -1
        elif  nums[left] == target:
            left_position = right
        else:
            left_position = -1

        left, right = 0, len(nums)
        while( left < right ):
            mid = left + (right - left) // 2
            if ( nums[mid] <= target ):
                left = mid + 1
            elif( nums[mid] > target ):
                right = mid
        left -= 1
        if nums[left] == target:
            right_position = left
        else:
            right_position = -1

        return [left_position, right_position]

t = Solution()
result = t.searchRange([2,2], 2)
print(result)