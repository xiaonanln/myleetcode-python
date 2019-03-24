from collections import namedtuple
from heapq import *

class Region(object):
	def __init__(self, N, start, end):
		assert end >= start

		self.N = N
		self.start = start
		self.end = end
		self.heapidx = None

	def __repr__(self):
		return 'Region<%d-%d|%d>' % (self.start, self.end, self.d)

	@property
	def d(self):
		N = self.N

		if self.start == 0 and self.end == N-1:
			return 10**10

		elif self.start == 0:
			return self.end - self.start
		elif self.end == N-1:
			return self.end - self.start
		else:
			return (self.end - self.start) // 2

	def __lt__(self, other):
		d1, d2 = self.d, other.d
		if d1 > d2:
			return True
		elif d1 < d2:
			return False

		return self.start < other.start

def cmp_lt(x, y):
	# Use __lt__ if available; otherwise, try __le__.
	# In Py3.x, only __lt__ will be called.
	return (x < y) if hasattr(x, '__lt__') else (not y <= x)

def heappop(heap):
	lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
	if heap:
		returnitem = heap[0]
		heap[0] = lastelt
		lastelt.heapidx = 0
		_siftup(heap, 0)
	else:
		returnitem = lastelt

	returnitem.heapidx = None
	_heapverify(heap)
	return returnitem

def heappush(heap, item):
	"""Push item onto heap, maintaining the heap invariant."""
	assert item.heapidx is None
	heap.append(item)
	item.heapidx = len(heap) - 1
	_siftdown(heap, 0, len(heap)-1)
	_heapverify(heap)

def heappopat(heap, pos):
	assert  0 <= pos < len(heap)
	lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
	if pos != len(heap):
		returnitem = heap[pos]
		heap[pos] = lastelt
		lastelt.heapidx = pos
		_siftup(heap, pos)
	else:
		returnitem = lastelt

	returnitem.heapidx = None
	_heapverify(heap)
	return returnitem

def _siftup(heap, pos):
	endpos = len(heap)
	startpos = pos
	newitem = heap[pos]
	# Bubble up the smaller child until hitting a leaf.
	childpos = 2*pos + 1    # leftmost child position
	while childpos < endpos:
		# Set childpos to index of smaller child.
		rightpos = childpos + 1
		if rightpos < endpos and not cmp_lt(heap[childpos], heap[rightpos]):
			childpos = rightpos
		# Move the smaller child up.
		heap[pos] = heap[childpos]
		heap[pos].heapidx = pos
		pos = childpos
		childpos = 2*pos + 1
	# The leaf at pos is empty now.  Put newitem there, and bubble it up
	# to its final resting place (by sifting its parents down).
	heap[pos] = newitem
	newitem.heapidx = pos
	_siftdown(heap, startpos, pos)

def _siftdown(heap, startpos, pos):
	newitem = heap[pos]
	# Follow the path to the root, moving parents down until finding a place
	# newitem fits.
	while pos > startpos:
		parentpos = (pos - 1) >> 1
		parent = heap[parentpos]
		if cmp_lt(newitem, parent):
			heap[pos] = parent
			parent.heapidx = pos
			pos = parentpos
			continue
		break
	heap[pos] = newitem
	newitem.heapidx = pos

def _heapverify(heap):
	for i, item in enumerate(heap):
		assert item.heapidx == i

class ExamRoom(object):

	def __init__(self, N):
		"""
		:type N: int
		"""
		self.N = N
		rootregion = Region(N, 0, N-1)
		rootregion.heapidx = 0
		self.heap = [rootregion]
		self.regions = {
			0: rootregion,
			N-1: rootregion,
		}
		_heapverify(self.heap)

	def seat(self):
		"""
		:rtype: int
		"""
		assert self.heap, (self.heap, self.regions)
		# print 'before seat', self.heap
		region = heappop(self.heap)
		# print region
		N = self.N
		assert region.start in self.regions
		assert region.end in self.regions
		del self.regions[region.start]
		if region.end != region.start:
			del self.regions[region.end]

		# print 'seat', region, self.regions

		if region.start == 0:
			self._add_new_region(1, region.end)
			return 0
		elif region.end == N-1:
			self._add_new_region(region.start, N-2)
			return N-1
		else:
			s = region.start + region.d
			if s-1 >= region.start:
				self._add_new_region(region.start, s-1)
			if s+1 <= region.end:
				self._add_new_region(s+1, region.end)

			return s

	def _add_new_region(self, start, end):
		if start > end:
			return

		region = Region(self.N, start, end)
		heappush(self.heap, region)
		assert region.start not in self.regions
		assert region.end not in self.regions, (self.regions, region)
		self.regions[region.start] = self.regions[region.end] = region

	def leave(self, p):
		"""
		:type p: int
		:rtype: void
		"""
		assert p not in self.regions
		lr = self.regions.get(p-1)
		rr = self.regions.get(p+1)
		if lr:
			heappopat(self.heap, lr.heapidx)
			assert lr.start in self.regions, (self.regions, lr)
			assert lr.end in self.regions, (self.regions, lr)
			del self.regions[lr.start]
			if lr.end != lr.start:
				del self.regions[lr.end]

		if rr:
			heappopat(self.heap, rr.heapidx)
			assert rr.start in self.regions, (self.regions, rr)
			assert rr.end in self.regions, (self.regions, rr)
			del self.regions[rr.start]
			if rr.end != rr.start:
				del self.regions[rr.end]

		start = lr.start if lr else p
		end = rr.end if rr else p
		self._add_new_region(start, end)


r = ExamRoom(10)
assert r.seat() == 0
assert r.seat() == 9
assert r.seat() == 4
r.leave(0)
r.leave(4)
assert r.seat() == 0
assert r.seat() == 4
assert r.seat() == 2
assert r.seat() == 6