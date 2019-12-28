# TODO
# # class Stack:
# #     def __init__(self):
# #         self.data = []
    
# #     def push(self, givenNum):
# #         self.data.append(givenNum)
# #     def pop(self):
# #         self.data.pop()

# class Stack():
#     def __init__(self):
#         self.elements=[]
#     def push(self,item):
#         self.elements.append(item)
#         print("JUST added ", item)
#     def pop(self):
#         if len(self.elements)<=0:           
#             return None
#         else:
#             print("JUST removed ", self.elements[-1])
#             return self.elements.pop()
#     def top(self):
#         if len(self.elements)<=0:
        
#             return None
#         else:
#             return self.elements[-1]
#     def size(self):
#         return len(self.elements)
    
#     def isEmpty(self):
#         if(len(self.elements)==0):
#             return True
#         return False

# def evaluatePrefix(givenString):
#     givenString = givenString.split()

#     s = Stack()
#     s2 = Stack()

#     print("given string is ", givenString)
#     print("len is ", len(givenString))
    
#     for each in givenString:
#         s.push(each)

    
#     while not s.isEmpty():

#         abc = s.top()
#       # if abc is None:
#         #     continue
#         if(abc in '+-*/^'):
#             s.pop()
#             operand=0
#             x = s2.pop()
#             y = s2.pop()
#             x = int(x)
#             y = int(y)
#             if (abc =='+'):
#                     operand=x+y
                
#             elif(abc =='-'):
# ##                    operand=y-x
#                     operand = x - y                    
#             elif(abc =='*'):
# ##                    operand=y*x
#                     operand = x * y                   
#             elif(abc =='/'):
# ##                    operand=y/x
#                     operand = x / y                                      
#             elif(abc =='^'):
# ##                     operand=y**x
#                     operand = x ** y                   
#             s2.push(operand)
#         else:
#             s2.push(abc)
#             s.pop()
#             print("size check FINAL " , s.size())
#             if (s.size() == 1):
#                 print("am here")
# ##                break
        
        
#     print("************************\n\n\n")
# ##    return s.elements
#     return s2.elements
# # print(  evaluatePrefix("+ 4 * 3 12") )
# print(  evaluatePrefix("- + * 4 5 3 10") )
