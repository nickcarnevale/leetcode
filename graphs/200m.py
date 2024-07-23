# https://leetcode.com/problems/number-of-islands/

import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # check if the grid is empty
        if not grid:
            return 0
        
        # initalize variables
        rows, cols, = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # breadth first search 
        def bfs(r,c):
            
            # iterave
            q = collections.deque()

            # add (r, c) to the visited set
            visited.add((r,c))

            # append the node to the bfs queue
            q.append((r,c))

            # while the queue is not empty
            while q:
                
                # offset for directions
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                
                # pop the first appended for breadth first search 
                #row, col = q.pop() for depth first search
                row, col = q.popleft()

                for r, c in directions: 
                    # apply the offset each time
                    r, c = r + row, c + col
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r,c) not in visited):

                        q.append((r,c))
                        visited.add((r,c))

        # traverse each point in the grid
        for r in range(rows):
            for c in range(cols):

                # if a point is ever an island, we need to breadth first search and add the entire island to the visited set
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands



