class Solution(object):
	def validIPAddress(self, IP):
		"""
		:type IP: str
		:rtype: str
		"""
		if '.' in IP:
			return 'IPv4' if self.checkIPv4(IP) else "Neither"
		elif ':' in IP:
			return 'IPv6' if self.checkIPv6(IP) else "Neither"
		else:
			return 'Neither'

	def checkIPv4(self, IP):
		sp = IP.split('.')
		if len(sp) != 4: return False 
		for n in sp:
			if n == '': return False 
			if len(n) >= 4: return False 
			for c in n:
				if c < '0' or c > '9': return False 

			if n[0] == '0' and n != '0': return False
			if int(n) >= 256: return False 
		return True

	def checkIPv6(self, IP):
		sp = IP.split(':')
		if len(sp) != 8: return False 
		for h in sp:
			if h == '': return False 
			if len(h) >= 5: return False 
			for c in h:
				if not ('0' <= c <= '9' or 'a'<=c<='z' or 'A'<=c<='Z'):
					return False 
			try:
				int(h, 16)
			except:
				return False 

		return True 

print Solution().validIPAddress("172.16.254.1")
print Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
print Solution().validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334")

print Solution().validIPAddress("0.0.0.-0")
print Solution().validIPAddress("")
print Solution().validIPAddress("172.16.254.01")
print Solution().validIPAddress("256.16.254.01")
print Solution().validIPAddress("2001:0db8:85a3::8A2E:0370:7334")
print Solution().validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334")
