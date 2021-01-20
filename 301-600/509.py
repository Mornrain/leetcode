class Solution:
    def fib(self, n: int) -> int:
        temp = [0] * (n+1)
        return self.support(temp, n)

    def support(self, array, n):
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        if array[n] != 0:
            return array[n]
        array[n] = self.support(array, n-1) + self.support(array, n-2)
        return array[n]

t = Solution()
result = t.fib(10)
print(result)