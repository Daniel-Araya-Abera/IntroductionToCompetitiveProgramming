# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not( l1 or l2 ):
            return None
        head = None
        result = None
        if l1 and l2:
            if l1.val == min(l1.val, l2.val):
                    result = ListNode(l1.val)
                    l1 = l1.next
            else: #if l2.val == min(l1.val, l2.val):
                    result = ListNode(l2.val)                
                    l2 = l2.next
            head = result             
        elif l1:
                result = ListNode(l1.val)
                head = result
                l1 = l1.next
        elif l2:
            result = ListNode(l2.val)
            head = result
            l2 = l2.next

        while l1 or l2:
            if l1 and l2:
                minnNum = min(l1.val, l2.val)
                if l1.val == minnNum:
                    result.next = ListNode(l1.val)
                    result = result.next
                    l1 = l1.next
                
                if l2.val == minnNum:
                    result.next = ListNode(l2.val)
                    result = result.next
                    l2 = l2.next
            elif l1:
                result.next = ListNode(l1.val)
                result = result.next
                l1 = l1.next
            elif l2:
                result.next = ListNode(l2.val)
                result = result.next
                l2 = l2.next
    
        return head