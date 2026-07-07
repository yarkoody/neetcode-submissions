# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Create a stack with the root node
        visited = [root]
        
        # while stack not empty
        while visited:
            # pop the top element from the stack and save it
            currNode = visited.pop()
            # check if it has any childs (left or right)
            # if there are add them to the stack to treat them later
            if currNode.left:
                visited.append(currNode.left)
            if currNode.right:
                visited.append(currNode.right)
            # for the curr node swap its children
            currNode.left,currNode.right = currNode.right, currNode.left
        return root            



