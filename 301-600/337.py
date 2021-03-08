# 337. 打家劫舍Ⅲ
class Solution:
    def rob(self, root):
        def dp(root):
            if not root:
                return 0, 0
            ls, ln = dp(root.left)
            rs, rn = dp(root.right)
            return root.val + ln + rn, max(ls, ln)+ max(rs, rn)
        return max(dp(root))