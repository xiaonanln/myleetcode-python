class Solution(object):
	def constructArray(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[int]
		"""
		res = [1]
		minn, maxn = 2, n
		while k > 2:
			res.append(maxn)
			res.append(minn)
			k -= 2
			minn += 1
			maxn -= 1

		# print minn, maxn, k, res
		if k == 1:
			res.extend(range(minn, maxn+1))
		elif k == 2:
			res.extend([minn+1, minn, minn+2])
			res.extend(range(minn+3, maxn+1))

		return res

print Solution().constructArray(10, 4)