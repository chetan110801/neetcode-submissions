# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height =  self.dfs(root.left)
        right_height = self.dfs(root.right)
        res = left_height + right_height

        sub = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )

        return max(res, sub)


    def dfs(self, root):
        return 0 if not root else 1 + max(self.dfs(root.left), self.dfs(root.right))
        