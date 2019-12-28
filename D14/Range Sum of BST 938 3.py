# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rangeSumBST(self, root, L, R):   
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        rangeSum = 0

        if root == None:
            return 0
        
        
        
        if L<=root.val<= R:
            rangeSum += root.val
        if L <= root.val:
            rangeSum += self.rangeSumBST(root.left, L, R)  
        if root.val <= R:
            rangeSum += self.rangeSumBST(root.right, L, R)
    
    
        
        
        