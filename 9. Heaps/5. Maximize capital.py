class Solution:
    def findMaximizedCapital(self, numProjects: int, initialCap: int, profits: List[int], capital: List[int]) -> int:
        minCapital = [] # minheap to select minimum capital possible
        maxProfit = [] # maxheap to select projects of maximum profit
        
        for i in range(len(capital)):
            heapq.heappush(minCapital, (capital[i], i))
            
        available = initialCap
        
        for i in range(numProjects):
            while minCapital and minCapital[0][0] <= available:
                capital, j = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, (-profits[j]))
                
            if not maxProfit:
                break
            
            available += -heapq.heappop(maxProfit)
        
        return available
            
        
        
        