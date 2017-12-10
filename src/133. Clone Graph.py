# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if not node: return None

		copyedNode = {}
		visited = set()

		def dfs(node):
			# visit the node here
			visited.add(node)

			if node not in copyedNode:
				copyedNode[node] = UndirectedGraphNode(node.label)
			cnode = copyedNode[node]

			for n in node.neighbors:
				if n not in copyedNode:
					copyedNode[n] = UndirectedGraphNode(n.label)
				cnode.neighbors.append( copyedNode[n] )

				if n not in visited:
					dfs(n)



		dfs(node)
		return copyedNode[node]