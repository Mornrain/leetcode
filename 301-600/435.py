# 435. 无重叠区间
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
#
# 注意:
#
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 示例 1:
#
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
#
# 输出: 1
#
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
class Solution:
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)
        num = 0
        for i in range(n):
            intervals[i].reverse()

        intervals = sorted(intervals)

        for i in range(n):
            intervals[i].reverse()

        j = 1
        while j < len(intervals):
            if intervals[j][0] < intervals[j-1][1]:
                num += 1
                del intervals[j]
            else:
                j += 1

        return num
        # for i in range(n):
        #     for j in range(i,n):

s = Solution()
result = s.eraseOverlapIntervals([[1,2],[3,7],[3,6],[5,9],[2,6],[4,5]])
print(result)