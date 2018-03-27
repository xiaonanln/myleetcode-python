class Solution(object):
	def similarRGB(self, color):
		"""
		:type color: str
		:rtype: str
		"""
		CANDINATE_NUMS = (0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff)
		r = int(color[1:3], 16)
		g = int(color[3:5], 16)
		b = int(color[5:7], 16)
		# print r,g,b
		mostSimilarColor = None
		highestSimilarity = float('-inf')
		for sr in CANDINATE_NUMS:
			for sg in CANDINATE_NUMS:
				for sb in CANDINATE_NUMS:
					sim = - ((r-sr)**2) - ((g-sg)**2) - ((b-sb)**2)
					# print (sr, sg, sb), sim
					if sim > highestSimilarity:
						highestSimilarity = sim
						mostSimilarColor = (sr, sg, sb)

		return '#%02x%02x%02x' % mostSimilarColor


print Solution().similarRGB("#09f166")