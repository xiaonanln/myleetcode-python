
class ListNode(object):
	__slots__ = ('val', 'next')

	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList(object):
	__slots__ = ('head', 'tail')

	def __init__(self):
		self.head = None
		self.tail = None

	def insertTail(self, val):
		node = ListNode(val)
		if not self.head:
			self.head = self.tail = node
		else:
			self.tail.next = node
			self.tail = node 
		return node

	def moveToTail(self, node):
		if node is self.tail: # already tail
			return ()

		nodeval = node.val
		nextnode = node.next
		node.val = nextnode.val
		node.next = nextnode.next  # remove nextnode
		if nextnode is self.tail:
			self.tail = node 

		nextnode.val = nodeval

		self.tail.next = nextnode
		self.tail = nextnode
		return node, nextnode


	def removeHead(self):
		head = self.head
		self.head = head.next 
		head.next = None 

		return head 

class LRUCache(object):

	def __init__(self, capacity):
		self.capacity = capacity
		self.map = {}
		self.lrulist = LinkedList()
		
	def get(self, key):
		if key in self.map:
			node = self.map[key]
			value = node.val[1]
			for cn in self.lrulist.moveToTail(node):
				self.map[cn.val[0]] = cn
			return value
		else:
			return -1

	def put(self, key, value):
		if key in self.map:
			node = self.map[key]
			node.val = (key, value)
			for cn in self.lrulist.moveToTail(node):
				self.map[cn.val[0]] = cn
		else:
			if len(self.map) == self.capacity: # full, remove one
				head = self.lrulist.removeHead()
				del self.map[head.val[0]]

			node = self.lrulist.insertTail( (key, value) )
			self.map[key] = node


# Your LRUCache object will be instantiated and called as such:mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)	   
cache.put(3, 3)	
print cache.get(2)	   
cache.put(4, 4)	
print cache.get(1)	   
print cache.get(3)
print cache.get(4)	   

cache = LRUCache(1)
cache.put(2, 1)
print cache.get(2)