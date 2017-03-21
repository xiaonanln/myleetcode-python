"""
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
"""

class Solution(object):
	def validUtf8(self, data):
		"""
		:type data: List[int]
		:rtype: bool
		"""
		i = 0
		datalen = len(data)
		while i < datalen:
			b0 = data[i]
			if b0 <= 0x7f: # 0xxxxxxx
				i += 1
				elif b0 <= 

		return i == datalen



print Solution().validUtf8([197, 130, 1])
print Solution().validUtf8([235, 140, 4])