
class SolutionFloydButTimeout(object):
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		inf = float('inf')
		G = [[inf] * n for _ in xrange(n)]
		DEGREE = [0] * n
		for v1, v2 in edges:
			G[v1][v2] = 1
			G[v2][v1] = 1
			DEGREE[v1] += 1
			DEGREE[v2] += 1

		for i in xrange(n): # use vertexn as intermidate node
			if DEGREE[i] <= 1: continue
			for v1 in xrange(n):
				for v2 in xrange(v1+1, n):
					G[v1][v2] = G[v2][v1] = min(G[v1][v2], G[v1][i] + G[i][v2])

		maxDist = [-inf] * n

		for v1 in xrange(n):
			for v2 in xrange(v1+1, n):
				maxDist[v1] = max(maxDist[v1], G[v1][v2])
				maxDist[v2] = max(maxDist[v2], G[v1][v2])

		minTreeDepth = min(maxDist)
		return [v for v, md in enumerate(maxDist) if md == minTreeDepth]


class Solution(object):
	def findMinHeightTrees(self, N, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		adjs = [set() for _ in xrange(N)]
		degree = [0] * N
		for a, b in edges:
			adjs[a].add(b)
			adjs[b].add(a)
			degree[a] += 1
			degree[b] += 1

		leafs = [v for v in xrange(N) if degree[v] == 1]
		newleafs = []
		leftVertex = set(xrange(N))
		while len(leftVertex) > 2:
			# print 'removing leafs', leftVertex, leafs, degree
			for u in leafs: # remove leafs from the graph
				# print 'remove', u
				assert len(adjs[u]) == 1 and degree[u] == 1, (u, adjs, degree,leftN)

				degree[u] = 0
				leftVertex.discard(u)
				v = adjs[u].pop()

				adjs[v].discard(u)
				degree[v] -= 1

				if degree[v] == 1:
					newleafs.append(v)

			leafs, newleafs = newleafs, []

		return list(leftVertex)



print Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
# print Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
# import cProfile
# cProfile.run("""
# print Solution().findMinHeightTrees(210,
# [[0,1],[1,2],[0,3],[3,4],[4,5],[3,6],[6,7],[7,8],[0,9],[7,10],[6,11],[3,12],[5,13],[8,14],[7,15],[11,16],[12,17],[12,18],[18,19],[7,20],[8,21],[18,22],[7,23],[15,24],[21,25],[14,26],[11,27],[5,28],[15,29],[21,30],[12,31],[22,32],[1,33],[14,34],[14,35],[33,36],[14,37],[18,38],[19,39],[6,40],[29,41],[27,42],[25,43],[0,44],[26,45],[3,46],[1,47],[34,48],[26,49],[9,50],[34,51],[18,52],[41,53],[6,54],[25,55],[55,56],[47,57],[34,58],[58,59],[48,60],[24,61],[43,62],[51,63],[30,64],[24,65],[27,66],[30,67],[41,68],[64,69],[46,70],[49,71],[58,72],[43,73],[24,74],[43,75],[3,76],[32,77],[74,78],[31,79],[59,80],[25,81],[12,82],[26,83],[21,84],[35,85],[37,86],[39,87],[36,88],[67,89],[58,90],[22,91],[91,92],[56,93],[92,94],[3,95],[94,96],[89,97],[81,98],[6,99],[75,100],[56,101],[41,102],[68,103],[46,104],[3,105],[104,106],[56,107],[104,108],[83,109],[9,110],[0,111],[2,112],[53,113],[21,114],[76,115],[34,116],[26,117],[117,118],[116,119],[82,120],[27,121],[101,122],[8,123],[99,124],[79,125],[116,126],[53,127],[46,128],[116,129],[6,130],[46,131],[113,132],[25,133],[79,134],[38,135],[68,136],[116,137],[66,138],[56,139],[102,140],[36,141],[0,142],[126,143],[9,144],[36,145],[34,146],[140,147],[70,148],[117,149],[1,150],[5,151],[38,152],[48,153],[20,154],[145,155],[126,156],[54,157],[21,158],[155,159],[128,160],[34,161],[61,162],[72,163],[64,164],[144,165],[165,166],[60,167],[139,168],[85,169],[133,170],[60,171],[163,172],[120,173],[69,174],[21,175],[84,176],[24,177],[3,178],[131,179],[129,180],[35,181],[159,182],[31,183],[100,184],[110,185],[9,186],[6,187],[149,188],[141,189],[112,190],[22,191],[125,192],[174,193],[19,194],[156,195],[124,196],[88,197],[195,198],[187,199],[164,200],[179,201],[95,202],[48,203],[25,204],[53,205],[13,206],[127,207],[71,208],[119,209]])
# """)