# Remove Nth Node
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not n:
            return head
        
        nodeArray = []
        
        count = 0
        curr = head
        while curr:
            count += 1
            nodeArray.append(curr)
            curr = curr.next
        
        count = len(nodeArray)
        requiredIndex = count - n
        requiredNode = nodeArray[requiredIndex]
        if requiredIndex == len(nodeArray) - 1:
            if len(nodeArray) != 1:
                nodeArray[requiredIndex - 1].next = None
            else:
                return None
        
        elif requiredIndex == 0:
            return head.next
        else:
            nodeArray[requiredIndex].val = nodeArray[requiredIndex + 1].val
            nodeArray[requiredIndex].next = nodeArray[requiredIndex].next.next
        
        return head
            