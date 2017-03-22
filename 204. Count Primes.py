class SolutionMine(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2: return 0
		A = [1] * n

		numPrimes = 0
		for p in xrange(2, n):
			if not A[p]: continue 
			# p is prime! clear from p*2 to p*k ... where p*k <= n
			numPrimes += 1

			pp = p + p
			while pp < n:
				A[pp] = 0
				pp += p

		return numPrimes

class Solution: # good solution!
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

print Solution().countPrimes(1)
print Solution().countPrimes(2)
print Solution().countPrimes(3)
print Solution().countPrimes(6)
print Solution().countPrimes(10)
print Solution().countPrimes(100)