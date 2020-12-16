from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            ## has no prerequisites
            res = [i for i in range(numCourses)]
            return res

        if self.hasCycle(numCourses, prerequisites):
            return []
        
        visited = [False] * numCourses
        graph = {}
        
        for i, curr_edge in enumerate(prerequisites):
            if curr_edge[0] not in graph:
                graph[curr_edge[0]] = [curr_edge[1]]
            else:
                graph[curr_edge[0]].append(curr_edge[1])
            
        stack = []
        for i in range(numCourses):
            if not visited[i]:
                self.dfs(i, graph, visited,stack)
        return stack
        
    def hasCycle(self, numCourses, prerequisites):
        num_of_prerequisites = [0] * numCourses
        queue = deque()
        graph = {}
        for i,each in enumerate(prerequisites):
            if each[1] not in graph:
                graph[each[1]] = [each[0]]
            else:
                graph[each[1]].append(each[0])
            
            num_of_prerequisites[each[0]] += 1

            
        for i,num in enumerate(num_of_prerequisites):
            if not num:
                queue.append(i)
        count = len(queue) 
        while queue:
            curr_course = queue.popleft()
            if curr_course in graph:
                for course in graph[curr_course]:
                    num_of_prerequisites[course] -= 1
                    if not num_of_prerequisites[course]:
                        queue.append(course)
                        count += 1
        
        return count  != numCourses
    
    def dfs(self, index, graph, visited, stack):        
        visited[index] = True
        if index in graph:
            for course in graph[index]:
                if not visited[course]:
                    self.dfs(course, graph, visited, stack)
        
        stack.append(index)
