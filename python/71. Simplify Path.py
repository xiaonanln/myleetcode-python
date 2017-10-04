class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		path = path.split('/')
		stack = []
		for p in path:
			if p in ('', '.'):
				pass
			elif p == '..':
				if stack: stack.pop()
			else:
				stack.append(p)

		return '/' + '/'.join(stack)



print Solution().simplifyPath("/home/")
print Solution().simplifyPath("/a/./b/../../c/")