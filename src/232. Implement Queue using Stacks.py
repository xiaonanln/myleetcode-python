class Stack(list):
	push = list.append
	def peek(self):
		return self[-1]

	def empty(self):
		return not self

class MyQueue(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.instk = Stack()
		self.outstk = Stack()

	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: void
		"""
		self.instk.push(x)

	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if not self.outstk:
			while not self.instk.empty():
				self.outstk.push(self.instk.pop())

		return self.outstk.pop()

	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if not self.outstk:
			while self.instk:
				self.outstk.push(self.instk.pop())

		return self.outstk.peek()

	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return self.outstk.empty() and self.instk.empty()

