class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # find number of decreasing days to the left of ith day
        # find number of increasing days to the right of ith day 
        # iterate through both arrays and find the which i has left and right > time
        if time == 0:
            return list(range(len(security)))
        
        left, right = [0], [0]
        days = 0
        n = len(security)
        for i in range(1, n):
            if security[i] <= security[i-1]:
                days +=1
            else:
                days = 0
            left.append(days)

        days = 0
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                days += 1
            else:
                days = 0
            right.append(days)
        right.reverse()
        result = []
        for i in range(time, n - time):
            if left[i]>=time and right[i] >= time:
                result.append(i)
        return result
