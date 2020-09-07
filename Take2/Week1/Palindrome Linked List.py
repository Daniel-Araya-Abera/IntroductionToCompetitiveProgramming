# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy

# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # slow pointer is now at the middle   
        slow = self.reverseLinkedList(slow)
        start = head
        while slow:
            if slow.val != start.val:
                return False
            slow = slow.next
            start = start.next
        return True
    
    def reverseLinkedList(self, currNode):
        prev = None
        
        while currNode:
            nextNode = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = nextNode        
        return prev
