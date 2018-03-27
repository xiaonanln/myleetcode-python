from itertools import izip
class Solution(object):
	def minSwap(self, A, B):
		"""
		:type A: List[int]
		:type B: List[int]
		:rtype: int
		"""
		N = len(A)
		dp = [[None, None] for _ in xrange(N) ]
		dp[0][0] = 0
		dp[0][1] = 1
		for i in xrange(1, N):
			if A[i] <= A[i-1] or B[i] <= B[i-1]: # bad order in i-1 ~ i
				dp[i][0] = dp[i-1][1]
				dp[i][1] = dp[i-1][0] + 1
			elif min(A[i], B[i]) > max(A[i-1], B[i-1]): # very good order in i-1~i
				dp[i][0] = min(dp[i-1][0], dp[i-1][1])
				dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
			else: # good order in i-1 ~ i
				dp[i][0] = dp[i-1][0]
				dp[i][1] = dp[i-1][1] + 1

			# print A[i] <= A[i-1] or B[i] <= B[i-1], i, dp[i]


		# print dp
		return min(dp[N-1][0], dp[N-1][1])


A = [0,4,4,5,9]
B = [0,1,6,8,10]
print Solution().minSwap(A, B)