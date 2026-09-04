class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # is_prime[i] indicates whether i is prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Only iterate up to sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark multiples starting from i*i
                is_prime[i * i : n : i] = [False] * len(range(i * i, n, i))
                
        return sum(is_prime)