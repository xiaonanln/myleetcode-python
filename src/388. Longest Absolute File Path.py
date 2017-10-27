class Solution(object):
	def lengthLongestPath(self, input):
		"""
		:type input: str
		:rtype: int
		"""
		path = []
		curdepth = 0
		pathlen = [0]
		maxfilepathlen = 0
		for line in input.split('\n'):
			d = 0
			while line[d] == '\t':
				d += 1

			name = line[d:]
			assert d <= len(path)
			if d == len(path):
				path.append(name)
			else:
				path[d] = name

			curdepth = d + 1
			assert curdepth <= len(pathlen)
			if curdepth == len(pathlen):
				pathlen.append(pathlen[curdepth-1] + len(name))
			else:
				pathlen[curdepth] = pathlen[curdepth-1] + len(name)

			# print path[:curdepth], pathlen[:curdepth+1]
			if '.' in name: # this is a file
				maxfilepathlen = max(maxfilepathlen, pathlen[curdepth] + curdepth-1)

		return maxfilepathlen




print Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")