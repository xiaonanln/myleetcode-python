from bisect import bisect_left, bisect_right
class Solution(object):
	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		i = bisect_left(arr, x)
		j = bisect_right(arr, x,  i)
		N = len(arr)
		while j - i < k:
			if j == N:
				i = N-k
				break
			elif i == 0:
				j = k
				break
			elif arr[j] - x < x - arr[i-1]:
				j += 1
			else:
				i -= 1

		return arr[i:j]

print Solution().findClosestElements([1,2,3,4,5], 4, -1)

