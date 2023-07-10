class Solution:
    # if the current character is '0', then all we need to do it 
    # find the number of 1 before this 0 and number of 1 after this 0 
    # and multiply them to add them to the answer.
# We do the same for the central character as '1' and count the number of 0 before and after this one.
    def numberOfWays(self, s: str) -> int:
        result = 0
        n = len(s)
        total_zeroes = 0

        for char in s:
            if char == '0': total_zeroes +=1
        total_ones = n - total_zeroes
        curr_zeroes = curr_ones = 0
        if s[0] == '0': 
            curr_zeroes +=1 
        else: curr_ones +=1

        for i in range(1, n):
            if s[i] == '0':
                result += curr_ones * (total_ones - curr_ones)
                curr_zeroes +=1
            else:
                result += curr_zeroes * (total_zeroes - curr_zeroes)
                curr_ones += 1
        return result
    
    # dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
    #     for i in range(len(s)):
    #         if s[i] == "0":
    #             dp["0"] += 1
    #             dp["10"] += dp["1"]
    #             dp["010"] += dp["01"]
    #         if s[i] == "1":
    #             dp["1"] += 1
    #             dp["01"] += dp["0"]
    #             dp["101"] += dp["10"]
                
    #     return dp["010"] + dp["101"]