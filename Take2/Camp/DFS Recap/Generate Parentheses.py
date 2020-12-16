class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## 1. initialize with ( in stack
        ## 2. check both open and closed brackets if valid
        ## 3. stop adding open brackets if remaining open is 0
        ## 4. stop adding closed brackets if they are balanced
        ## 5. if both remaining open and closed are 0, add to result
        
        res = []
        remaining_open, remaining_closed = n - 1, n
        stack = [(["("],remaining_open, remaining_closed)]
        while stack:
            curr_string, rem_open, rem_closed = stack.pop()
            if not rem_open and not rem_closed:
                res.append("".join(curr_string))
            if rem_open != 0:
                new_string = curr_string + ["("]
                stack.append((new_string, rem_open - 1, rem_closed))
            if rem_open != rem_closed:
                new_string = curr_string + [")"]
                stack.append((new_string, rem_open, rem_closed - 1))
        
        return res
