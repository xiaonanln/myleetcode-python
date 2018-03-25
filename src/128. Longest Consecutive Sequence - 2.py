class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		RS = {}
		LC = 0
		for n in nums:
			print RS, n
			if n in RS: continue

			if n-1 not in RS and n+1 not in RS:
				RS[n] = n
				LC = max(LC, 1)

			elif n-1 in RS and n+1 in RS:
				a, b = RS[n-1], RS[n+1]
				if a <= n-1 and b >= n+1:
					RS[a] = b
					RS[b] = a
					if n-1 != a:
						del RS[n-1]
					if b != n+1:
						del RS[n+1]
					LC = max(LC, b-a+1)

			elif n-1 in RS:
				a = RS[n-1]
				if a >= n: continue
				assert RS[a] == n-1, (RS, a, n-1)
				RS[a] = n
				RS[n] = a
				if n-1 != a:
					del RS[n-1]
				LC = max(LC, n - a + 1)

			elif n+1 in RS:
				a = RS[n+1]
				if a <= n: continue
				# print RS, a, n+1
				assert RS[a] == n+1, (RS, a, n+1)
				RS[a] = n
				RS[n] = a
				if n+1 != a:
					del RS[n+1]
				LC = max(LC, a-n + 1)

			# print RS
		return LC

print Solution().longestConsecutive([-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2])