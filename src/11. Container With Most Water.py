class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		l, r = 0, len(height)-1
		res = 0
		while l < r:
			area = min(height[l], height[r]) * (r-l)
			res = max(res, area)
			# find next r
			if height[l] <= height[r]:
				# find next l' that height[l'] > height[l]
				l_ = l+1
				while l_ < r and height[l_] <= height[l]:
					l_ += 1
				l = l_
			else:
				r_ = r-1
				while l < r_ and height[r_] <= height[r]:
					r_ -= 1
				r = r_

		return res

print Solution().maxArea([1,2,3])