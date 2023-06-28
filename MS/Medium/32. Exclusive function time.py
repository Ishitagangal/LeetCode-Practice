class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        
        def normalizeProcessTime(processTime):
            return processTime.split(':') 
        
        for processTime in logs:
            processId, eventType, time = normalizeProcessTime(processTime)
            
            if eventType == "start":
                stack.append([processId, time])
            
            elif eventType == "end":
                processId, startTime = stack.pop()
                timeSpent = int(time) - int(startTime) + 1 # Add 1 cause 0 is included
                result[int(processId)] += timeSpent
                
                # Decrement time for next process in the stack
                if len(stack) != 0:
                    nextProcessId, timeSpentByNextProcess = stack[-1] #
                    result[int(nextProcessId)] -= timeSpent
                    
        return result