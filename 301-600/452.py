class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        min_num = 1
        if not points:
            return 0
        for i in range(n):
            points[i].reverse()

        points = sorted(points)

        for i in range(n):
            points[i].reverse()

        temp = points[0][1]

        for i in range(1,n):
            if points[i][0] > temp:
                min_num += 1
                temp = points[i][1]

        return min_num



s = Solution()
result = s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(result)