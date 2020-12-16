class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## 1. construct the graph in prerequisite -> next_course manner
        ## 2. keep track of how many prerequisites each course has
        ## 3. start from the end(with courses that are ta)
        num_of_prerequisites = [0] * numCourses
        stack = []
        graph = {}
        for i,each in enumerate(prerequisites):
            if each[1] not in graph:
                graph[each[1]] = [each[0]]
            else:
                graph[each[1]].append(each[0])
            
            num_of_prerequisites[each[0]] += 1

            
        for i,num in enumerate(num_of_prerequisites):
            if not num:
                stack.append(i)
        count = len(stack) 
        while stack:
            curr_course = stack.pop()
            if curr_course in graph:
                for course in graph[curr_course]:
                    num_of_prerequisites[course] -= 1
                    if not num_of_prerequisites[course]:
                        stack.append(course)
                        count += 1
        
        return count  == numCourses
    
    