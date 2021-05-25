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
        ## Practice:
        steps = 0
        visited = set()

        if s == t or not graph:
            return 0

        visited.add(s)
        queue = collections.deque([s])

        while queue:
            steps += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for node_n in node.neighbors:
                    if node_n == t:
                        return steps
                    if node_n not in visited:
                        visited.add(node_n)
                        queue.append(node_n)
        return -1




        ##
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
