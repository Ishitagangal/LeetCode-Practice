class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = math.inf
        arr.sort()
        minimum_diff_pairs = defaultdict(list)

        for i in range(len(arr) - 1):
            d = arr[i+1] - arr[i]
            minimum_diff_pairs[d].append((arr[i], arr[i+1]))
            min_diff = min(min_diff, d)
        return minimum_diff_pairs[min_diff]