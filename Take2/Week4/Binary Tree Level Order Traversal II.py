# Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        curr = root
        queue = deque()
        queue.append((curr,1))
        
        queue2 = deque()
        depth = 1
        while queue:
            currNode, count = queue.popleft()
            queue2.append((currNode, count))
            
            if currNode.left:
                queue.append((currNode.left, count + 1))
                
            if currNode.right:
                queue.append((currNode.right, count + 1))
            
            if not queue:
                depth = count
        
        res = [[] for _ in range(depth)]
        
        while queue2:
            currNode, count = queue2.popleft()
            
            res[len(res) - count].append(currNode.val)
   
        return res
            