class StringIterator(object):
	def __init__(self, compressedString):
		"""
		:type compressedString: str
		"""
		self.cs = compressedString
		self.cursor = 0
		self.nextChar = None
		self.nextCharNum = 0

	def next(self):
		"""
		:rtype: str
		"""
		if self.nextCharNum == 0:
			# get more char
			self.getMoreChars()

		if self.nextCharNum > 0:
			self.nextCharNum -= 1
			return self.nextChar
		else:
			return ' '

	def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.nextCharNum == 0:
			# get more char
			self.getMoreChars()

		return self.nextCharNum > 0

	def getMoreChars(self):
		L = len(self.cs)
		cursor = self.cursor
		if cursor < L:
			self.nextChar = self.cs[cursor]
			cursor += 1
			numstart = cursor
			while cursor < L and '0' <= self.cs[cursor] <= '9':
				cursor += 1

			self.nextCharNum = int(self.cs[numstart:cursor])
			self.cursor = cursor

si = StringIterator('L1e2t1C1o1d1e1')
while si.hasNext():
	print si.next()


