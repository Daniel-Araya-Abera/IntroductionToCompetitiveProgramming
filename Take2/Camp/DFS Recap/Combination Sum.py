class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.dfs(0, candidates,[], target)
    
    def dfs(self, start, candidates, res, target):
        result = []
        for i in range(start, len(candidates)):
            if candidates[i] < target:
                result.extend(self.dfs(i, candidates, res + [candidates[i]], target - candidates[i]))
            elif candidates[i] == target:
                result.append(res + [candidates[i]])
                break
            else:
                break
        
        return result
