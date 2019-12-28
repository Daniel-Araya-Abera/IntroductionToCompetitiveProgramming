# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if val < root.val:
            if root.left == None:
                newTreeNode = TreeNode(val)
                root.left = newTreeNode
            else:
                self.insertIntoBST(root.left, val)
        elif val > root.val:
            if root.right == None:
                newTreeNode = TreeNode(val)
                root.right = newTreeNode
            else:
                self.insertIntoBST(root.right, val)
        else:
            pass
        
        return root