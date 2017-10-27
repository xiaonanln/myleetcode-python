import random
class RandomizedSet(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.index = {}
		self.vals = []

	def insert(self, val):
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		if val in self.index: # already exists
			return False

		self.vals.append(val)
		self.index[val] = len(self.vals) - 1
		return True

	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		idx = self.index.pop(val, None)
		if idx is None:
			return False

		if idx == len(self.vals) - 1:
			self.vals.pop()
		else:
			lastval = self.vals[idx] = self.vals.pop()
			self.index[lastval] = idx
		return True

	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		return random.choice(self.vals)



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print obj.insert(1)
print obj.insert(2)
print obj.insert(3)
print obj.insert(4)
print obj.remove(3)
print obj.getRandom()