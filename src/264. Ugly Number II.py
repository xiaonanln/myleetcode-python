from heapq import *
class SolutionMineSlow(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		heap = [1]
		pushed = set([1])
		for i in xrange(n-1):
			popval = heappop(heap)
			if popval * 2 not in pushed:
				heappush(heap, popval * 2)
				pushed.add(popval * 2)
			if popval * 3 not in pushed:
				heappush(heap, popval * 3)
				pushed.add(popval * 3)
			if popval * 5 not in pushed:
				heappush(heap, popval * 5)
				pushed.add(popval * 5)

		return heappop(heap)

class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ugly = [1]
		i, j, k = 0, 0, 0
		for _ in xrange(n-1):
			next = min(ugly[i]*2, ugly[j]*3, ugly[k]*5)
			ugly.append(next)

			if next == ugly[i]*2: i += 1
			if next == ugly[j]*3: j += 1
			if next == ugly[k]*5: k += 1

		return ugly[-1]

for i in xrange(1, 11):
	print Solution().nthUglyNumber(i)