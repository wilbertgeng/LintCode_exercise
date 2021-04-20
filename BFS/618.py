"""618 · Search Graph Nodes"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        queue = collections.deque([node])

        visited = set()
        visited.add(node)

        while queue:
            node_cur = queue.popleft()
            if values[node_cur] == target:
                return node_cur
            for node_nxt in node_cur.neighbors:
                if node_nxt not in visited:
                    visited.add(node_nxt)
                    queue.append(node_nxt)
        print(visited)
        return None 
