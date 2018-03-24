
from collections import deque
class Solution(object):
	def floodFill(self, image, sr, sc, newColor):
		"""
		:type image: List[List[int]]
		:type sr: int
		:type sc: int
		:type newColor: int
		:rtype: List[List[int]]
		"""
		R = len(image)
		if not R: return image
		C = len(image[0])

		# visited = [[False]*C for _ in xrange(R)]
		# visited[sr][sc] = True
		if newColor == image[sr][sc]:
			# no need to flood fill
			return image

		oldColor, image[sr][sc] = image[sr][sc], newColor
		Q = deque( [(sr, sc)] )
		while Q:
			r, c = Q.popleft()
			for nr, nc in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1) ):
				if 0 <= nr < R and 0 <= nc < C and image[nr][nc] == oldColor:
					image[nr][nc] = newColor
					Q.append( (nr, nc) )

		return image

print Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)


