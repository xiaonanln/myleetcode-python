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
		try:
			while i < datalen:
				b0 = data[i]
				if b0 <= 0b01111111: # 0xxxxxxx
					i += 1
				elif b0 <= 0b11011111:
					if not (0b10000000 <= data[i+1] <= 0b10111111): return False
					i += 2 
				elif b0 <= 0b11101111:
					if not (0b10000000 <= data[i+1] <= 0b10111111): return False
					if not (0b10000000 <= data[i+2] <= 0b10111111): return False
					i += 3
				elif b0 <= 0b11110111:
					if not (0b10000000 <= data[i+1] <= 0b10111111): return False
					if not (0b10000000 <= data[i+2] <= 0b10111111): return False
					if not (0b10000000 <= data[i+3] <= 0b10111111): return False
					i += 4
				else:
					return False 
		except IndexError:
			return False

		return i == datalen



print Solution().validUtf8([])

print Solution().validUtf8([197, 130, 1])
print Solution().validUtf8([235, 140, 4])
print Solution().validUtf8([206,210,189,208,197,163,182,171,212,243,10,0,10])
