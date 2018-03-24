class Solution(object):

	def evaluate(self, expression):
		"""
		:type expression: str
		:rtype: int
		"""
		val = self.expect_expr(expression, 0, {})[0]
		# print 'expr', expression, val
		return val

	def expect_expr(self, s, pos, scope):
		assert s[pos] != ' ', (s, pos, s[pos:])
		if s[pos] == '(':
			pos += 1
			tok, pos = self.next_token(s, pos)
			# print 'tok', tok, pos
			if tok == 'add':
				e1, pos = self.expect_expr(s, pos, scope)
				e2, pos = self.expect_expr(s, pos, scope)
				# print 'e1', e1, 'e2', e2
				# assert s[pos] == ')'
				_, pos = self.next_token(s, pos)
				return e1 + e2, pos
			elif tok == 'mult':
				e1, pos = self.expect_expr(s, pos, scope)
				e2, pos = self.expect_expr(s, pos, scope)
				# print 'e1', e1, 'e2', e2
				# assert s[pos] == ')'
				_, pos = self.next_token(s, pos)
				return e1 * e2, pos
			elif tok == 'let':
				scope = {'_': scope} # create child scope
				while True:
					if 'a' <= s[pos] <= 'z':
						# next tok is id
						id, pos = self.next_token(s, pos)
						if s[pos] == ')':
							# this id is actually the last expr
							_, pos = self.next_token(s, pos)
							return self.getvarval(id, scope), pos
						else:
							idval, pos = self.expect_expr(s, pos, scope)
							scope[id] = idval
					else:
						# must be the final expr
						exprval, pos = self.expect_expr(s, pos, scope)
						# assert s[pos] == ')', (s, pos, scope)
						_, pos = self.next_token(s, pos)
						return exprval, pos

		elif 'a' <= s[pos] <= 'z':
			return self.expect_id_val(s, pos, scope)
		else:
			# must be an int
			return self.expect_int(s, pos)

	def expect_id_val(self, s, pos, scope):
		tok, pos = self.next_token(s, pos)
		return self.getvarval(tok, scope), pos

	def expect_int(self, s, pos):
		tok, pos = self.next_token(s, pos)
		return int(tok), pos

	def getvarval(self, var, scope):
		if var in scope:
			return scope[var]
		else:
			return self.getvarval(var, scope['_'])

	def next_token(self, s, pos):
		tok = s[pos]
		# assert tok != ' '
		if tok in '()':
			pos += 1
		else:
			while pos < len(s):
				pos += 1
				if s[pos] in '() ':
					break
				tok += s[pos]

		while pos < len(s) and s[pos] == ' ':
			pos += 1

		return tok, pos

assert Solution().evaluate('(add 1 2)') == 3
assert Solution().evaluate('(mult 3 (add 2 3))') == 15
assert Solution().evaluate('(let x 2 (mult x 5))') == 10
assert Solution().evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))') == 14
assert Solution().evaluate('(let x 3 x 2 x)') == 2
assert Solution().evaluate('(let x 1 y 2 x (add x y) (add x y))') == 5
assert Solution().evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))') == 6
assert Solution().evaluate('(let a1 3 b2 (add a1 1) b2)') == 4