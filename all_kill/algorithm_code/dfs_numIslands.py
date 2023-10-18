
class Solution:
    def dfs(self,grid,i,j):
        n=len(grid)
        m=len(grid[0])
        if i<0 or i>=n or j<0 or j>=m or grid[i][j]=='0':
            return 0
        grid[i][j]='0'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)

    def numislands(self,grid)->int:
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    cnt+=1
        return cnt
grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numislands(grid))
