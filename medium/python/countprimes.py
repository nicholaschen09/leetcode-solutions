# Given an integer n, return the number of prime numbers that are strictly less than n.
#  
# Example 1:
# 
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:
# 
# Input: n = 0
# Output: 0
# Example 3:
# 
# Input: n = 1
# Output: 0
#  
# Constraints:
# 
# 0 <= n <= 5 * 10^6


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # Initialize a list indicating whether numbers are prime.
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime.
        
        p = 2
        while p * p < n:
            if is_prime[p]:
                # Mark multiples of p as not prime.
                for i in range(p * p, n, p): # iterates over all multiples of p strting at p^2 up to n going by multiples of p
                    is_prime[i] = False
            p += 1
        
        # Count the number of primes.
        return sum(is_prime)
