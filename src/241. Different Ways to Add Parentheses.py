import re

class Solution(object):
	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		"""
		opfuncs = {
			'+': lambda a, b: a+b,
			'-': lambda a, b: a-b,
			'*': lambda a, b: a*b
		}

		oppat = re.compile(r'[\+\-\*]')
		ops = re.findall(oppat, input)
		nums = map(int, oppat.split(input))

		# print 'input', input, 'nums', nums, 'ops', ops

		N = len(nums)
		dp = [ [None] * N for _ in xrange(N) ]
		for i in xrange(N):
			dp[i][i] = [nums[i]]
			if i < N-1:
				dp[i][i+1] = [opfuncs[ops[i]](nums[i], nums[i+1])]

		# print dp
		# calc from len 3 to len N
		for l in xrange(3, N+1):
			for i in xrange(0, N-l+1):
				j = i + l -1
				pv = dp[i][j] = []
				for k in xrange(i+1, j+1):
					opf = opfuncs[ ops[k-1] ]
					pv.extend([opf(a, b) for a in dp[i][k-1] for b in dp[k][j]])

		# print dp
		return dp[0][N-1]


print Solution().diffWaysToCompute("2-1-1")
print Solution().diffWaysToCompute("2*3-4*5")