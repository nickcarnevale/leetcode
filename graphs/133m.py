# https://leetcode.com/problems/clone-graph/description/

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # we are going to want to map the copys to the originals with a hashmap
        m = {}

        def dfs(node):
            if node in m:
                return m[node]
            
            # made a copy of the current node
            copy = Node(node.val)

            # add to the hashmap
            m[node] = copy

            # for each node neighbors run dfs on it

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node) if node else None
