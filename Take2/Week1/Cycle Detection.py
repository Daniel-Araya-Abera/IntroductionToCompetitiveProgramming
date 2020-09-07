# Cycle Detection
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# Difficulty: Medium


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if not head:
        return False
    if not head.next:
        return False
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if (fast == slow):
            return True
    
    return False