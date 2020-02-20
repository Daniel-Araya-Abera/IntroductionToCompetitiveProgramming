from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.lastElement = None
        
        self.queue2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.lastElement = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
        # print("FIRST, len of first queue is ", len(self.queue))
        # print("FIRST, len of second queue is ", len(self.queue2))
        
        while len(self.queue) > 1:
            temp = self.queue.popleft()
            self.queue2.append(temp)
        
        poppedItem = self.queue.popleft()
        # print("popped item is ", poppedItem)
        # print("len of first queue is ", len(self.queue))
        # print("len of second queue is ", len(self.queue2))
        possibleLastElement = None
        while self.queue2:
            temp = self.queue2.popleft()
            self.queue.append(temp)
            possibleLastElement = temp
        
        # print("FINALLY len of first queue is ", len(self.queue))
        # print("FINALLY len of second queue is ", len(self.queue2))
        self.lastElement = possibleLastElement
        return poppedItem
            
        
        
            
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.lastElement
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        # if d: # not empty
        #     return False
        # else:
        #     return True
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()