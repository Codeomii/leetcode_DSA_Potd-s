from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m,n=len(grid),len(grid[0])
        d=[[10**9]*n for _ in range(m)]
        d[0][0]=grid[0][0]
        q=deque([(0,0)])
        while q:
            x,y=q.popleft()
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                i,j=x+dx,y+dy
                if 0<=i<m and 0<=j<n:
                    w=d[x][y]+grid[i][j]
                    if w<d[i][j]:
                        d[i][j]=w
                        (q.appendleft if grid[i][j]==0 else q.append)((i,j))
        return d[-1][-1]<health