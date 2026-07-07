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
        res = 1
        stack = [[root,1]]
        while stack:
            node, dist = stack.pop()
            res = max(dist,res)
            if node.left:
                stack.append([node.left,dist+1])
                # res = max(dist+1,res)
            if node.right:
                stack.append([node.right,dist+1])
                # res = max(dist + 1,res)
        return res



