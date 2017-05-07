class Solution(object):
	def countBattleships(self, board):
		counter = 0
		for r, row in enumerate(board): # for each row
			for c, v in enumerate(row): # for each col
				if v == 'X' and ((not (r > 0 and board[r-1][c] == 'X') and 
					not (c > 0 and board[r][c-1] == 'X'))): 
					counter += 1

		return counter



print Solution().countBattleships(
	[
		'X..X', 
		'...X',
		'...X', 
	]
)