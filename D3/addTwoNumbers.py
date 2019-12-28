class ListNode(self):
    def init(self, x):
        self.val = x
        self.next = None

def add(self, l1, l2):
    head = l3 = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        l3.val = carry % 10
        carry = carry // 10

        if l1 or l2 or carry:
            l3 = l3.next
    return head


            
