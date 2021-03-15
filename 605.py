"""
605. Sequence Reconstruction"""
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if org and not seqs:
            return False
        if org and not seqs[0]:
            return False
        nodes_indegree, graph = self.getIndegree(org, seqs)
        queue = collections.deque([n for n in nodes_indegree if nodes_indegree[n] == 0])
        order = []
        if len(graph) != len(org):
            return False
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            order.append(node)
            for n in graph[node]:
                nodes_indegree[n] -= 1
                if nodes_indegree[n] == 0:
                    queue.append(n)

        if order == org:
            return True
        return False


    def getIndegree(self, org, seqs):
        nodes_indegree = {n: 0 for n in range(1, len(org) + 1)}
        graph = collections.defaultdict(list)
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = []

        for seq in seqs:
            for i in range(1, len(seq)):
                if seq[i] in nodes_indegree:
                    nodes_indegree[seq[i]] += 1
                graph[seq[i - 1]].append(seq[i])

        return nodes_indegree, graph
