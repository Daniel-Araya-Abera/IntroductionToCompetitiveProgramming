# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        firstHead = None
        if not head:
            return None
        result = None
           
        if head:
            result = ListNode(head.val)
            firstHead = result
            head = head.next
        # print("**************")
        # print("result is ", result)
        # print("head is ", head)
        # print("first head is ", firstHead)
        # print("**************")
        
        while head:
            if head.val == result.val:
                head = head.next
            else:
                result.next = ListNode(head.val)
                result = result.next
                head = head.next
        # print("**************")
        # print("INSIDE LOOP")
        # print("result is ", result)
        # print("head is ", head)
        # print("first head is ", firstHead)
        # print("**************")
        return firstHead