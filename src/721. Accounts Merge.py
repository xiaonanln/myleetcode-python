class Solution(object):
	def accountsMerge(self, mails):
		"""
		:type mails: List[List[str]]
		:rtype: List[List[str]]
		"""
		accountByName = {}
		for account in mails:
			name = account[0]
			maillist = account[1:]
			accountByName.setdefault(name, []).append(maillist)

		res = []
		for name, maillists in accountByName.iteritems():
			# print 'name', name, 'maillists', maillists
			for sub in self.divideMailLists(maillists):
				res.append( [name] + sorted(sub) )

		return res

	def divideMailLists(self, maillists):
		N = 0
		mail2vertex = {}
		mails = []
		for maillist in maillists:
			for mail in maillist:
				if mail not in mail2vertex:
					mail2vertex[mail] = N
					N += 1
					mails.append(mail)

		# print mail2vertex, N
		graph = [[] for _ in xrange(N)]
		for maillist in maillists:
			for i in xrange(len(maillist)-1):
				u = mail2vertex[maillist[i]]
				v = mail2vertex[maillist[i+1]]
				graph[u].append(v)
				graph[v].append(u)

		visited = [False] * N

		def dfs(u, maillist):
			maillist.append( mails[u] )
			visited[u] = True
			for v in graph[u]:
				if not visited[v]:
					dfs(v, maillist)

		for u in xrange(N):
			if not visited[u]:
				maillist = []
				dfs(u, maillist)
				yield maillist

accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print Solution().accountsMerge(accounts)

