
from heapq import heappush, heappop, heapify
class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		if n <= 1: return 1
		NUMS = [1]
		V = {1, }
		IDX = [0 for _ in primes]
		MINS = [(pr, i) for i, pr in enumerate(primes)]
		heapify(MINS)

		while len(NUMS) < n:
			nextMin, pi = heappop(MINS) # get the next min
			# print nextMin, pi
			if nextMin not in V:
				NUMS.append(nextMin)
				V.add(nextMin)
				
			IDX[pi] += 1
			newVal = primes[pi] * NUMS[IDX[pi]]
			heappush(MINS, (newVal, pi))

		return NUMS[-1]


print Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
# print Solution().nthSuperUglyNumber(100000, 
# [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
# )