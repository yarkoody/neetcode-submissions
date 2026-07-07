# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        

        stack = [[root,1]]
        res = 0
        while stack:
            curr,d = stack.pop()
            if curr:
                res=max(res,d)
                stack.append([curr.left,d+1])
                stack.append([curr.right,d+1])
        return res

