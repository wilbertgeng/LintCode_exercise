"""137. Clone Graph"""
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        ### Practice:
        if not node:
            return None

        nodes = self.findNodes(node)

        map = self.copyNodes(nodes)

        self.copyEdges(nodes, map)

        return map[node]

    def findNodes(self, node):
        visited = set()
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        return list(visited)

    def copyNodes(self, nodes):
        map = {}
        for node in nodes:
            map[node] = UndirectedGraphNode(node.label)
        return map

    def copyEdges(self, nodes, map):
        for node in nodes:
            new_node = map[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(map[neighbor])


    

        ###
        if not node:
            return None
        nodes = self.findNodes(node)

        mapping = self.copyNodes(nodes)

        self.copyEdges(nodes, mapping)

        return mapping[node]

    def findNodes(self, node):
        visited = set([node])
        queue = collections.deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        return list(visited)

    def copyNodes(self, nodes):
        map = {}
        for node in nodes:
            map[node] = UndirectedGraphNode(node.label)
        return map

    def copyEdges(self, nodes, mapping):
        for node in nodes:
            newNode = mapping[node]
            for neighbor in node.neighbors:
                newNeighbor = mapping[neighbor]
                newNode.neighbors.append(newNeighbor)













######
