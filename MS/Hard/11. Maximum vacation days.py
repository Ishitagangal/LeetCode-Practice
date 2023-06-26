class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        memo = collections.defaultdict(int)
        result = 0

        def dfs(flights, days, cur_city, week, memo):
            if week == len(days[0]):
                return 0
            if (cur_city, week) in memo:
                return memo[(cur_city, week)]
            max_days = 0
            for i in range(len(flights)):
                if flights[cur_city][i] or i == cur_city:
                    cur_days = days[i][week] + dfs(flights, days, i, week +1, memo)
                    max_days = max(max_days, cur_days)
            memo[(cur_city,week)] = max_days
            return max_days
        
        return dfs(flights, days, 0, 0, memo)
        