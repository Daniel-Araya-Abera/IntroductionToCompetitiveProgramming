# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        good_pair = [0]
        self.helper(root, distance, good_pair)
        return good_pair[0]
        
    def helper(self, root, distance, good_pair):
        if not root.left and not root.right:
            return [1]
        
        left = []
        right = []
        
        if root.left:
            left = self.helper(root.left, distance, good_pair)
        if root.right:
            right = self.helper(root.right, distance, good_pair)
        
        for i in range(len(left)):
            for j in range(len(right)):
                if left[i] + right[j] <= distance:
                    good_pair[0] += 1
        
        for i in range(len(left)):
            left[i] += 1
        for j in range(len(right)):
            right[j] += 1
        
        return left + right
        