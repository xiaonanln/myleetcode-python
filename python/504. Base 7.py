class Solution(object):
	def convertToBase7(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num < 0:
			return '-' + self.convertToBase7(-num)

		if num == 0:
			return '0'

		v = ''
		while num > 0:
			num, mod = divmod(num, 7)
			v = chr(48+mod) + v
		return v

print Solution().convertToBase7(100)
print Solution().convertToBase7(-7)