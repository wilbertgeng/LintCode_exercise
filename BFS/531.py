"""531 · Six Degrees"""
"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        if s == t or not graph:
            return 0

        queue = collections.deque([(s, 0)])
        visited = set()
        visited.add(s)

        while queue:
            core, current_step = queue.popleft()
            if core == t:
                return current_step
            for node in core.neighbors:
                if node in visited:
                    continue
                visited.add(node)
                queue.append((node, current_step + 1))

        return -1
