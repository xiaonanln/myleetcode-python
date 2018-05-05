from collections import Counter
class Solution:
	def deleteAndEarn(self, nums):
		C = Counter(nums)
		nums = sorted(C.items())
		N = len(nums)
		dp = [[0, 0] for _ in range(N+1) ]
		for i in range(1, N+1):
			# check 2 conditions: pick nums[i-1] or not
			dp[i][False] = max(dp[i-1])
			if i-1 > 0 and nums[i-1][0] == nums[i-2][0] + 1:
				dp[i][True] = dp[i-1][False] + nums[i-1][0] * nums[i-1][1]
			else:
				dp[i][True] =  max(dp[i-1]) + nums[i - 1][0] * nums[i - 1][1]
		return max(dp[N])

print(Solution().deleteAndEarn([3,1]))
print(Solution().deleteAndEarn([3,4,2]))
print(Solution().deleteAndEarn([2,2,3,3,3,4]))