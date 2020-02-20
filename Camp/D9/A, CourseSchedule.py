from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for i in range(len(prerequisites)):
            prerequisites[i][0], prerequisites[i][1] = prerequisites[i][1], prerequisites[i][0]

        visited_list = {}
        frequency_list = [0] * numCourses
        adjacency_list = []
        for i in range(numCourses):
            adjacency_list.append([])
        for i in range(numCourses):
            visited_list[i] = False
        for i in range(len(prerequisites)):
            index = prerequisites[i][1]
            frequency_list[index] += 1

        for i in range(len(prerequisites)):
            adjacency_list[prerequisites[i][0]].append( prerequisites[i][1] )

        queue = deque()
           
        for i in range(len(frequency_list)):
            if not frequency_list[i]:
                queue.append(i)
                
        # print("queue is ", queue)
        # print("visited list is ", visited_list)
        # print("adjacency_list : ", adjacency_list)
        result = []
        if len(queue) == 0:
            print("AAA")
            return False
        while queue:
            # print("queue is ", queue)
            curr = queue.popleft()
            for eachIndex in adjacency_list[curr]:
                frequency_list[eachIndex] -= 1
                if frequency_list[eachIndex] == 0 :
                    queue.append(eachIndex)
                # elif frequency_list[eachIndex] <= 0 :
                #     print("NN")
            result.append(curr)
        
        print("result is ", result)
        # if not len(result):
        #     return False
        if len(result) != numCourses:
            print("coz result is ", result, " and numCourses is ", numCourses)
            return False
        return True
                