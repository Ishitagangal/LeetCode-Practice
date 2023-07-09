class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_website = defaultdict(list)
        for i in range(len(username)):
            user_website[username[i]].append((timestamp[i], website[i]))
        
        patterns = defaultdict(set) # pattern to set of users
        max_pattern = defaultdict(set)
        max_count = 0

        def get_combinations(websites, index, path, user, patterns):
            nonlocal max_count, max_pattern
            if len(path) == 3:
                patterns[tuple(path)].add(user)
                count = len(patterns[tuple(path)])
                if count >= max_count:
                    max_count = count
                    max_pattern[max_count].add(tuple(list(path)))
                return
            
            for i in range(index, len(websites)):
                get_combinations(websites, i + 1, path + [websites[i][1]], user, patterns)

        for user, websites in user_website.items():
            websites.sort() # sort by timestamp
            get_combinations(websites, 0, [], user, patterns)
        
        result = sorted(list(max_pattern[max_count]))
        print(result)
        #  for below return res[0][0]
        # res = sorted(list(patterns.items()), key=lambda a:(-len(a[1]), a[0]))
        return result[0]
        