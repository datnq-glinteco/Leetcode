class Solution(object):
    def closestPrimes(self, left, right):
        # Step 1: Generate all primes up to 'right' using Sieve of Eratosthenes
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime

        # Step 2: Get prime numbers in the range [left, right]
        is_prime = sieve(right)
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]  # Not enough primes to form a pair

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result
