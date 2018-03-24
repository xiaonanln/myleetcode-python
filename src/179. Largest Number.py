from itertools import izip
class Solution:
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		def cmpnum(n1, n2):
			d1 = 1
			while d1*10 <= n1: d1 *= 10

			d2 = 1
			while d2*10 <= n2: d2 *= 10
			while d1>0 and d2>0:
				nd1 = n1 // d1
				nd2 = n2 // d2
				if nd1 != nd2:
					return (nd1 - nd2) * 2
				n1 %= d1
				n2 %= d2
				d1, d2 = d1//10, d2//10

			if d1 == 0 and d2 == 0:
				return 0
			elif d1 == 0:
				return 1
			elif d2 == 0:
				return -1

		nums.sort(cmp=cmpnum, reverse=True)
		print 'sorted', nums
		N = len(nums)
		used = [False] * N
		def bt(prefix):
			if prefix == '0':
				return '0'

			lastN = None
			maxnum = prefix
			for i, (n, u) in enumerate(izip(nums, used)):
				if u: continue

				if not lastN or -1 <= cmpnum(lastN, n) <= 1:
					used[i] = True
					lastN = n
					maxnum = max(maxnum, bt(prefix + str(n)))
					used[i] = False
				else:
					break

			# print 'max', maxnum
			return maxnum

		return bt('')

print Solution().largestNumber([41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55])


