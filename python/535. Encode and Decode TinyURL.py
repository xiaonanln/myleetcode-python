"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Subscribe to see which companies asked this question.
"""

class Codec:

	PREFIX = 'http://t.cn/'
	PREFIXLEN = len(PREFIX)

	def __init__(self):
		self.cache = {}

	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.

		:type longUrl: str
		:rtype: str
		"""
		h = hash(longUrl)
		self.cache[h] = longUrl
		return Codec.PREFIX + str(h)

	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.

		:type shortUrl: str
		:rtype: str
		"""
		h = shortUrl[Codec.PREFIXLEN:]
		return self.cache[int(h)]

# Your Codec object will be instantiated and called as such:
codec = Codec()
print codec.decode(codec.encode('http://google.com'))