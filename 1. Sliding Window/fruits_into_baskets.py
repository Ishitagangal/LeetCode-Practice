class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_freq = Counter() # or use defaultdict()
        window_start = window_size = 0
        max_fruits = 0 #max_len

        for window_end in range(len(fruits)):
            fruit_freq[fruits[window_end]] += 1

            while len(fruit_freq) > 2:
                left_fruit = fruits[window_start]
                fruit_freq[left_fruit] -= 1

                if fruit_freq[left_fruit] == 0:
                    del fruit_freq[left_fruit]
                window_start +=1
            
            window_size = window_end - window_start + 1
            max_fruits = max(max_fruits, window_size)
        
        return max_fruits
