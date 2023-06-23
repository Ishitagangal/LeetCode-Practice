class Solution:
    def countPrimes(self, n: int) -> int:
        # return primes between 0 and n 
        # init array 0 to n to true prime
        # starting from 2, update all nums that are multiples of 2 to False
        # repeat with 3, and so on for every "still" prime num till we reach n
        # now all the nums that have any lower primes as multiple are discounted
        # leaving us with list of "True" at ith index where i = prime num
        if n <=2:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] =False
        for num in range(2, n):
            if primes[num]: # if number is prime, update its multiples till n as not prime
                for i in range(2*num, n, num): # step by number itself "addition" for multiplying
                    primes[i] = False
        
        return sum(primes)