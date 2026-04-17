class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for i in range(len(operations)):

            if operations[i] == 'C':
                record.pop()
            
            elif operations[i] == '+':
                record.append(record[-1] + record[-2])
            
            elif operations[i] == 'D':
                record.append(record[-1] * 2)
            
            else:
                record.append(int(operations[i]))

        return sum(record)            
