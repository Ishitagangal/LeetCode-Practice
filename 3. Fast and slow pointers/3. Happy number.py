class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            sum = 0
            while num > 0:
                digit = num %10
                num = num //10
                sum += digit **2
            return sum
        slow = n
        fast = get_next_number(n)
        while slow != fast and fast!=1:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))
            
        return fast == 1