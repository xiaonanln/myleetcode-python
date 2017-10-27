import sys 

class Solution(object):
	def maxNumber(self, nums1, nums2, K):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""
		L1 = len(nums1)
		L2 = len(nums2)

		dp = [[[None]*(K+1) for j in xrange(0, L2+1)] for i in xrange(0, L1+1)]

		for i in xrange(0, L1+1):
			for j in xrange(0, L2+1):
				dp[i][j][0] = ()

		for i in xrange(L1-1, -1, -1): # L1-1 ~ 0
			ni = nums1[i]
			maxk = min(L1-i, K)
			for k in xrange(maxk, 0, -1): # L1-i-1 ~ 0
				if k == L1-i:
					dp[i][L2][k] = (ni, ) + dp[i+1][L2][k-1]
				else:
					dp[i][L2][k] = self.max(
						(ni, ) + dp[i+1][L2][k-1], 
						dp[i+1][L2][k]
						)

		for j in xrange(L2-1, -1, -1): # L2-1 ~ 0
			nj = nums2[j]
			maxk = min(L2-j, K)
			for k in xrange(maxk, 0, -1): # L2-j-1 ~ 0
				if k == L2-j:
					dp[L1][j][k] = (nj, ) + dp[L1][j+1][k-1]
				else:
					dp[L1][j][k] = self.max(
						(nj, ) + dp[L1][j+1][k-1], 
						dp[L1][j+1][k]
					)

		for i in xrange(L1-1, -1, -1):
			for j in xrange(L2-1, -1, -1):
				for k in xrange(1, min(K, L1-i + L2-j)+1):
					# print >>sys.stderr, i, j, k
					v1 = (nums1[i], ) + dp[i+1][j][k-1]
					v2 = (nums2[j], ) + dp[i][j+1][k-1]
					if L1-i + L2-j > k:
						v3 = dp[i+1][j][k]
						v4 = dp[i][j+1][k]
						dp[i][j][k] = self.max(self.max(v1, v2), self.max(v3, v4))
					else:
						dp[i][j][k] = self.max(v1, v2)
					# print >>sys.stderr, i, j, k, dp[i][j][k]

		return dp[0][0][K]

	def max(self, nums1, nums2):
		assert len(nums1) == len(nums2)
		for n1, n2 in zip(nums1, nums2):
			if n1 > n2:
				return nums1
			elif n1 < n2:
				return nums2

		return nums1


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
nums1 = [9,1,2,5,8,3]
nums2 = [3,4,6,5]
k = 5
print Solution().maxNumber(nums1, nums2, k)