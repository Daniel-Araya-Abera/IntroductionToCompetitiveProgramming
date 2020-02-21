class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        if len(stack):            
            return False
        return True