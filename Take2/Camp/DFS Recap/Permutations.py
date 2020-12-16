class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## neigbhours = [0 to n - 1] or indices
        ## state =  currList,
        ## 1. add each num in nums to stack
        ## 2. go through all neighbours and append to each case & add to visited
        ## 3.
        
        stack = []
        for i in range(len(nums)):
            currList = [nums[i]]
            visited = set()
            visited.add(i)
            stack.append((currList, visited))
        
        res = []
        while stack:
            curr = stack.pop()
            res_curr = self.dfs(curr[0], curr[1], [], nums)
            res.extend(res_curr)
        return res
            
    def dfs(self, currList, visited, res, nums):
        neighbours = [i for i in range(len(nums))]
        
        stack = [(currList, visited, res, nums)]
        while stack:
            currList, currVisited, res, nums = stack.pop()
            if len(currList) == len(nums):
                res.append(currList)
                continue
            for i in range(len(neighbours)):
                if i not in currVisited:
                    newList = currList[:]
                    newList.append(nums[i])
                    newVisited = set()
                    for each in currVisited:
                        newVisited.add(each)
                    newVisited.add(i)
                    stack.append((newList, newVisited, res, nums))

        return res
