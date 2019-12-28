# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == val:
            print("find val", root.val)
            return root
        else:
            if val > root:
                print("going to left side", root.left)
                if root.left == None:
                    root = None
                else:
                    root = self.searchBST(root.left, val)
                    return root
            else:
                print("going to right side", root.right)
                if root.right == None:
                    root = None
                else:
                    root = self.searchBST(root.right, val)
                    return root
            