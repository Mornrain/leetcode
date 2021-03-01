# 167. 两数之和 II - 输入有序数组
# 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
#
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
#
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

class Solution:
    def twoSum(self, numbers, target):
        # 方法一：二分查找（时间复杂度为nlogn)
        first_num, second_num = 0, 1
        if (numbers[len(numbers) - 2] + numbers[len(numbers) - 1] < target):
            return None
        while (first_num < len(numbers)):
            second_num = (first_num + len(numbers)) // 2
            left_border = first_num
            right_border = len(numbers)
            while (left_border < second_num and second_num < right_border):
                if (numbers[first_num] + numbers[second_num] == target):
                    return [first_num + 1, second_num + 1]
                if (numbers[first_num] + numbers[second_num] > target):
                    right_border = second_num
                    second_num = (left_border + right_border) // 2
                if (numbers[first_num] + numbers[second_num] < target):
                    left_border = second_num
                    second_num = (left_border + right_border) // 2
                if (second_num == left_border or second_num == right_border):
                    break
            first_num += 1
        return None

        # 方法二：双指针 (时间复杂度为n):
        left, right = 0, len(numbers) - 1
        while (left != right):
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return None


s = Solution()
result = s.twoSum([2,3,4], 6)
print(result)