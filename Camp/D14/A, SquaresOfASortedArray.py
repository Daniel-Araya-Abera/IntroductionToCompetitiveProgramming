class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        curr = head
        count = 0
        hadDisconnection = True
        start = 0
        gSet = set()
        for each in G:
            if each not in gSet: gSet.add(each)

        while curr:
            if curr.val in gSet and hadDisconnection:
                count += 1
                hadDisconnection = False
                
            if curr.val not in gSet:
                hadDisconnection = True
                
            curr = curr.next
        
        return count