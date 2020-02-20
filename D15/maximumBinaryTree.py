# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMax(self, nums: List[int]):
        maxx = nums[0]
        maxIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > maxx:
                maxx = nums[i]
                maxIndex = i
        return maxx, maxIndex
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) > 0:
            maxx, maxIndex = self.getMax(nums)
            root = TreeNode(maxx)
            root.right = self.constructMaximumBinaryTree( nums[ maxIndex + 1 : ] ) 
            root.left = self.constructMaximumBinaryTree( nums[: maxIndex ] ) 
            return root
        return None