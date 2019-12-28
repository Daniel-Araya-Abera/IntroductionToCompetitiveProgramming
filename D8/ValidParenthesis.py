# class Stack:
#     def __init__(self):
#         self.data = []
    
#     def push(self, givenNum):
#         self.data.append(givenNum)
#     def pop(self):
#         self.data.pop()

class Stack():
    def __init__(self):
        self.elements=[]
    def push(self,item):
        self.elements.append(item)
        print("JUST added ", item)
    def pop(self):
        if len(self.elements)<=0:           
            return None
        else:
            print("JUST removed ", self.elements[-1])
            return self.elements.pop()
    def top(self):
        if len(self.elements)<=0:
        
            return None
        else:
            return self.elements[-1]
    def size(self):
        return len(self.elements)
    
    def isEmpty(self):
        if(len(self.elements)==0):
            return True
        return False

##  () [] {}
##  ( [ {{ () [] [(]) } () } ] )
## [(])
class Solution(object):
    def isValid(self, s):
        stack1 = Stack()
##        for each in s:
##            stack1.push(each)

        if len(s) % 2:
           return False
        
        for i in range((len(s) // 2)):
            print("input is ", s)
            if s[i] in "{[(":
                stack1.push(s[i])
            else:
                if stack1.isEmpty():
                    break
                value = stack1.pop()
                if stack1.isEmpty():
                    break
                potentialPair = stack1.top()
                if value == ")":
                    print("a")
                    if potentialPair == "(":
                        stack1.pop()
                    else:
                        return False
                elif value == "}":
                    print("b")
                    if potentialPair == "{":
                        stack1.pop()
                    else:
                        return False
                elif value == "]":
                    print("c")
                    if potentialPair == "[":
                        stack1.pop()
                    else:
                        return False
                else:
                    print("e")
                    return False   ## invalid chars on input
                
            if stack1.isEmpty():
                break
        if not(stack1.isEmpty()):
            return False

        return True
            



s = Solution()
print( s.isValid("{[]}") )
