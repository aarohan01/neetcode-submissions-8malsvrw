class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:


        
        total = len(students)

        while True:
            prevtotal = total
            for i in range(len(students)):
                if students[0] ==  sandwiches[0]:
                    print('True')
                    students.pop(0)
                    sandwiches.pop(0)
                    total -=  1
                else:
                    students.append(students.pop(0))

            if total == prevtotal:
                break
            

        return len(students)

            
