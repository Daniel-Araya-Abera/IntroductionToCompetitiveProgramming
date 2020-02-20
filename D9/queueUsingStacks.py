class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack2 = []
        self.firstItem = None
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack) == 0:  self.firstItem = x
        self.stack.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        stateOfLengthOfStack1 = len(self.stack) <= 1
        while len(self.stack) > 1:
            temp = self.stack.pop()
            self.stack2.append(temp)
        poppedItem = self.stack.pop()
        
        if stateOfLengthOfStack1:   self.firstItem = None
        else:  self.firstItem = self.stack2[-1]
        
        while len(self.stack2) > 0:
            temp = self.stack2.pop()
            self.stack.append(temp)
        return poppedItem
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.firstItem

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.stack)
        
        
        
        
        
# Few Sample test cases
# ["MyQueue","push","pop","empty","peek"]
# [[],[5],[],[],[]]

# ["MyQueue","push","push","push","push","peek","push","pop","empty","pop","peek", "pop"]
# [[],[1],[2],[3],[4],[],[5],[],[],[],[],[]]

# ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
# 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()