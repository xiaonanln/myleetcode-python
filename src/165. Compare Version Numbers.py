class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		version1 = tuple(int(v) for v in version1.split('.'))
		version2 = tuple(int(v) for v in version2.split('.'))
		for i in xrange(max(len(version1), len(version2))):
			v1 = version1[i] if i < len(version1) else 0
			v2 = version2[i] if i < len(version2) else 0
			if v1 < v2:
				return -1
			elif v1 > v2:
				return 1

		return 0