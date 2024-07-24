class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        n, m = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        pacificAccess = set()
        atlanticAccess = set()
        
        def dfs_pacific(height, pair):
            x, y = pair 
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if (nx in range(n) and
                    ny in range(m) and 
                    (nx,ny) not in pacificAccess and
                    heights[nx][ny] >= height):

                   pacificAccess.add((nx,ny))
                   dfs_pacific(heights[nx][ny], (nx,ny)) 

        def dfs_atlantic(height, pair):
            x, y = pair 
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if (nx in range(n) and
                    ny in range(m) and 
                    (nx,ny) not in atlanticAccess and
                    heights[nx][ny] >= height):

                   atlanticAccess.add((nx,ny))
                   dfs_atlantic(heights[nx][ny], (nx,ny)) 

        # first row
        for i in range(m):
            pacificAccess.add((0,i))
            dfs_pacific(heights[0][i], (0,i))

        # first column 
        for i in range(n):
            pacificAccess.add((i,0))
            dfs_pacific(heights[i][0], (i,0))

        # last row
        for i in range(m):
            atlanticAccess.add((n-1,i))
            dfs_atlantic(heights[n-1][i], (n-1,i))

        # last column 
        for i in range(n):
            atlanticAccess.add((i,m-1))
            dfs_atlantic(heights[i][m-1], (i,m-1))

        intersection = pacificAccess & atlanticAccess

        result = [[x, y] for x, y in intersection]

        return result
        