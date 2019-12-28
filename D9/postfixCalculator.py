# leetcode question
# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self,num):
        self.stack.append(num)
        self.count += 1
        return self.stack ##
    def pop(self):
        val = self.stack.pop()
        self.count -= 1
        # print("After popping ......", self.stack)
        return val
        
    def top(self):
        return self.stack[-1]

    def size(self):
        return self.count
    def display(self):
        print(  self.stack )

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        givenString = tokens
        operators = ['+', '-', '*', '/', '^']
        stack = Stack()
        output = []
        i = 0
        while i < len(givenString):
            if givenString[i] not in operators:
                stack.push(givenString[i])

            elif givenString[i] in operators and stack.size() >= 2:
                y = stack.pop()
                x = stack.pop()

                y = eval(y)
                x = eval(x)


                z = 1
                operator = givenString[i]
                if operator == "+":
                    z = x + y
                elif operator == "-":
                    z = x - y
                elif operator == "*":
                    z = x * y
                elif operator == "/":
                    z = x / y
                    z = int(z)
                elif operator == "^":
                    z = x ^ y
                else:
                    print("unspecified operator")
                z = str(z)
                stack.push(z)
            elif givenString[i] == "-":
                a = eval(stack.pop())
                z = -a
                z = str(z)
                stack.push(z)
            i += 1
        result = stack.top()
        return result