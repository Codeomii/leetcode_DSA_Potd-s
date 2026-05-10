'''1914. Cyclically Rotating a Grid:--

You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

Return the matrix after performing k cyclic rotations on it.



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.

Example 1:

Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.

Example 2:

Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109'''

# Solution:--

from typing import List


class Solution:
    def rotateGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(g),len(g[0])
        for l in range(min(m,n)//2):
            a=[]
            for j in range(l,n-l): a+=[g[l][j]]
            for i in range(l+1,m-l-1): a+=[g[i][n-l-1]]
            for j in range(n-l-1,l-1,-1): a+=[g[m-l-1][j]]
            for i in range(m-l-2,l,-1): a+=[g[i][l]]
            a=a[k%len(a):]+a[:k%len(a)]
            t=0
            for j in range(l,n-l): g[l][j]=a[t];t+=1
            for i in range(l+1,m-l-1): g[i][n-l-1]=a[t];t+=1
            for j in range(n-l-1,l-1,-1): g[m-l-1][j]=a[t];t+=1
            for i in range(m-l-2,l,-1): g[i][l]=a[t];t+=1
        return g