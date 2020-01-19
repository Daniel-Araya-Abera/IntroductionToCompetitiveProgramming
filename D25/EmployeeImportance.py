"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id) -> int:
        employeeSubordinatesID = []
        employeeImportanceValue = 0
        
        for each in employees:
            xTEMP_eachID = each.id
            if each.id == id: ## employee found
                employeeImportanceValue = each.importance
                # employeeSubordinatesID.append(each.subordinates)
                if len(each.subordinates) > 0:
                    summ = each.importance
                    for eachSubEmployeeId in each.subordinates:
                        summ += self.getImportance(employees,eachSubEmployeeId)
                    return summ
                else:
                    print("ABCDEABCDE")
                    print(each.subordinates)
                    print("each id found : ", each.id)
                    print("each employee importance found is : ", each.importance)
                    return each.importance
        print("got here")
        print("list of employee is ", employees)
        for each in employees:
            print("each : ", each.id)

                
                
                
# s = Solution()

# e1 = Employee(1,5,[2, 3])
# e2 = Employee(2,3,[])
# e3 = Employee(3,3,[])
# listOfEmployees = []
# listOfEmployees.append(e1)
# listOfEmployees.append(e2)
# listOfEmployees.append(e3)
# result = s.getImportance(listOfEmployees, 1)
# print("FINAL RESULT IS ", result)