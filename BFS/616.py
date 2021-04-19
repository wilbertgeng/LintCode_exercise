"""616. Course Schedule II
"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        ## build graph:
        graph = [[] for _ in range(numCourses)]
        nodes_indegree = [0] * numCourses

        ######
        nodes_indegree, dependency = self.getIndegree(numCourses, prerequisites)
        queue = collections.deque([n for n in nodes_indegree if nodes_indegree[n] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for n in dependency[node]:
                nodes_indegree[n] -= 1
                if nodes_indegree[n] == 0:
                    queue.append(n)
        if len(order) == numCourses:
            return order
        return []


    def getIndegree(self, numCourses, prerequisites):
        nodes_indegree = {n: 0 for n in range(numCourses)}
        dependency = collections.defaultdict(list)

        for node_relation in prerequisites:
            nodes_indegree[node_relation[0]] += 1
            if node_relation[1] in dependency:
                dependency[node_relation[1]].append(node_relation[0])
            else:
                dependency[node_relation[1]] = [node_relation[0]]

        return nodes_indegree, dependency
