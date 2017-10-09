from collections import defaultdict
class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		E = len(tickets)
		airports = set()
		for a, b in tickets:
			airports.add(a)
			airports.add(b)
		airports = sorted(airports)
		airportsV = {a: i for i, a in enumerate(airports)}
		# print airportsV
		V = len(airports)

		adjs = [defaultdict(int) for _ in xrange(V)]
		for a, b in tickets:
			a, b = airportsV[a], airportsV[b]
			adjs[a][b] += 1

		# print 'adjs', adjs
		itinerary = ['JFK']
		def bt(a, usedTickNum):
			if usedTickNum == E:
				return True

			for b in sorted(adjs[a].keys()):
				adjs[a][b] -= 1
				if adjs[a][b] == 0:
					del adjs[a][b]

				itinerary.append(airports[b])
				if bt(b, usedTickNum+1):
					return True

				itinerary.pop()
				adjs[a][b] += 1

			return False

		bt(airportsV['JFK'], 0)
		return itinerary

# print Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])