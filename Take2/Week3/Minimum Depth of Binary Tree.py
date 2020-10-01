# Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        minn = float('inf')
        queue = deque()
        queue.append([root,1])

        while queue:
            curr = queue.popleft()
            currNode, currDepth = curr[0], curr[1]
            if not currNode.left and not currNode.right:
                minn = min(minn, currDepth)
            
            if currNode.left:
                queue.append([currNode.left, currDepth + 1])
            if currNode.right:
                queue.append([currNode.right, currDepth + 1])

        return minn