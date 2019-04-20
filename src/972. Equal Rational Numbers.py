class Solution(object):
	def isRationalEqual(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		si, sn, sr = self.parse(S)
		ti, tn, tr = self.parse(T)
		# print si, sn, sr
		# print ti, tn, tr
		if si == ti and sn == tn and sr == tr:
			return True

		if sr == '9' and tr == '0' and self._is_smallby1(si, sn, ti, tn):
			return True

		elif sr == '0' and tr == '9' and self._is_smallby1(ti, tn, si, sn):
			return True

		return False

	def parse(self, s):
		ip, nrp, rp = self._parse(s)
		# print '_parse', ip, nrp, rp
		return self._simplify(ip, nrp, rp)

	def _parse(self, s):
		L = len(s)
		i = 0
		ip = ''
		while i < L and '0' <= s[i] <= '9':
			ip += s[i]
			i += 1

		assert i == L or s[i] == '.'
		if i == L:
			return ip, '', ''

		i += 1  # skio dot
		nrp = ''
		while i < L and s[i] != '(':
			nrp += s[i]
			i += 1

		assert i == L or s[i] == '('
		if i == L:
			return ip, nrp, ''

		i += 1
		rp = ''
		while i < L and s[i] != ')':
			rp += s[i]
			i += 1

		return ip, nrp, rp

	def _simplify(self, ip, nrp, rp):
		if ip == '':
			ip = '0'

		while len(ip) > 1 and ip[0] == '0':
			ip = ip[1:]

		# make sure rp is in its shortest form
		# print '_shortest_rp', rp,
		rp = self._shortest_rp(rp)
		# print rp
		while nrp and rp and nrp[-1] == rp[-1]:
			rp = nrp[-1] + rp[:-1]
			nrp = nrp[:-1]

		return ip, nrp, rp

	def _shortest_rp(self, rp):
		if rp == '':
			rp = '0'

		rpl = len(rp)
		if rpl <= 1:
			return rp

		for i in xrange(2, rpl + 1):
			if rpl % i != 0:
				continue

			if rp[:(rpl / i)] * i == rp:
				return rp[:(rpl / i)]

		return rp

	def _is_smallby1(self, ti, tn, si, sn):
		if len(tn) != len(sn):
			return False

		return int(ti + tn) +1 == int(si + sn)


# print Solution().isRationalEqual('0.(52)', '0.5(25)')
print Solution().isRationalEqual("1.9(0)", "1.8(9)")
# print Solution().isRationalEqual('0.9(9)', '1')
