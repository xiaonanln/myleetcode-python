class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		return [
			'FizzBuzz' if i % 15 == 0 else (
				'Fizz' if i % 3 == 0 else (
					'Buzz' if i % 5 == 0 else (
						str(i)
					)
				)
			)

			for i in xrange(1, n+1)
		]

print Solution().fizzBuzz(15)