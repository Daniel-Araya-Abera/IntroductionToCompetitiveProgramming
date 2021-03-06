"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        return self.maxDepthHelper(root)
    
    def maxDepthHelper(self, root: 'Node') -> int:
        count = 0
        if not(root):
            return 0
        depth = 0
        # print("root is ", root.val)
        if root.children is None:
            return depth
        
        for child in root.children:
            depth = max(depth, self.maxDepthHelper(child))
            
        return depth + 1
        