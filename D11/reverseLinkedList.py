# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode = head
        previousNode = None
        
        while currentNode:
            # print("currentNode is ", currentNode)
            nextNode = currentNode.next
            currentNode.next = previousNode
            # print("** ", currentNode, " pointing to ", previousNode)
            previousNode = currentNode
            if nextNode is None:
                break
            currentNode = nextNode
            
        # print("NOW CURRENT NODE IS ", currentNode)
        # print("NOW head IS ", head)
        return currentNode
            