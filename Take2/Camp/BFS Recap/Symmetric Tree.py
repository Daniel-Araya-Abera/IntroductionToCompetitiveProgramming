# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        single_row = []
        depth = 0
        queue = deque([(root, 0)])
        curr_row = []
        
        while queue:
            curr_node, curr_depth = queue.popleft()
            if curr_depth == depth:
                if curr_node:
                    curr_row.append(curr_node.val)
                else:
                    curr_row.append(None)
            else:
                print("curr row ", curr_row)
                if not self.row_is_symmetric(curr_row):
                    return False
                curr_row = []
                depth = curr_depth
                if curr_node:
                    curr_row = [curr_node.val]
                else:
                    curr_row = [None]
            
            if curr_node:
                if curr_node.left:
                    queue.append((curr_node.left, curr_depth + 1))
                else:
                    queue.append((None, curr_depth + 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_depth + 1))
                else:
                    queue.append((None, curr_depth + 1))

        # for row in depth_row:
        #     if not self.row_is_symmetric(depth_row[row]):
        #         return False
        # return True
        return True
    
    
    def row_is_symmetric(self, curr_list):
        end = len(curr_list) - 1
        for i in range(len(curr_list) // 2):
            if curr_list[i] != curr_list[end - i]:
                return False
            
        return True
        