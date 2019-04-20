from collections import deque


class Solution(object):
	def catMouseGame(self, graph):
		"""
		:type graph: List[List[int]]
		:rtype: int
		"""
		N = len(graph)
		state = (1, 2)
		q = deque()
		q.append((1, 2))

		states = [(1, 2)]
		state_index = {(1, 2): 0}
		state_graph = [[]]
		lose_states = set()
		win_states = set()

		while q:
			m, c = q.popleft()
			sidx = state_index[(m, c)]
			print (m, c)
			assert (m, c) in state_index
			ncs = set(nc for nc in graph[c] if nc != 0)
			nms = set(nm for nm in graph[m] if nm != c and nm not in ncs)

			if not nms:
				# mouse lose in this pos
				lose_states.add(sidx)
			elif 0 in nms:
				win_states.add(sidx)
			else:
				for nm in nms:
					for nc in ncs:
						if (nm, nc) not in state_index:
							# found new state
							nsidx = len(state_index)
							state_index[(nm, nc)] = nsidx
							states.append((nm, nc))
							state_graph.append([])
							assert len(state_graph) == len(states) == len(state_index)
							q.append((nm, nc))
						else:
							nsidx = state_index[(nm, nc)]

						# this state can be reached from (m, c)
						state_graph[sidx].append(nsidx)

		print states
		print state_index
		print state_graph
		print 'lose', lose_states
		print 'win', win_states


print Solution().catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]])
