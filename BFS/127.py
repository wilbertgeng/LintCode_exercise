"""127. Topological Sorting"""
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        ## Practice:
        indegree = self.getIndegree(graph)
        start_nodes = [node for node in graph if indegree[node] == 0]
        queue = collections.deque(start_nodes)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def getIndegree(self, graph):
        indegree = {n: 0 for n in graph}

        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        return indegree



        ###
        nodes_indegree = self.getIndegree(graph)
        start_nodes = collections.deque([n for n in graph if nodes_indegree[n] == 0])
        order = []

        while start_nodes:
            node = start_nodes.popleft()
            order.append(node)
            for n in node.neighbors:
                nodes_indegree[n] -= 1
                if nodes_indegree[n] == 0:
                    start_nodes.append(n)

        return order


    def getIndegree(self, graph):
        nodes_indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                nodes_indegree[neighbor] += 1

        return nodes_indegree














#####
