# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if (not p and q) or ( p and not q): #one null without the other null
                return [p, q, False]
            if not p and not q:
                return [p, q, True]
            if p.val != q.val:
                return [p, q, False]
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return [p, q, left[2]==right[2]==True]

        return dfs(p,q)[2]