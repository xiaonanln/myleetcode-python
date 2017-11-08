class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		stack = [
			["", None, ]
		]

		cur = stack[-1]
		for c in s:
			if c == '[':
				cur = ["", None]
				stack.append( cur )
			elif c == ']':
				# print 'closing', cur
				s = cur[0]
				stack.pop()
				cur = stack[-1]
				cur[0] += s * cur[1]
				cur[1] = None
			elif '0' <= c <= '9':
				cur[1] = int(c) if cur[1] is None else cur[1] * 10 + int(c)
			else:
				cur[0] += c

		return cur[0]


print Solution().decodeString("3[a]2[bc]")
# print Solution().decodeString("3[a2[c]]")
# print Solution().decodeString("2[abc]3[cd]ef")