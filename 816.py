"""816. Traveling Salesman Problem"""
class Result:
    def __init__(self):
        self.min_cost = float('inf')
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        # Write your code here
        result = Result()
        graph = self.buildGraph(n, roads)
        visited = set([1])
        self.dfs(1, n, [], visited, 0, graph, result)
        return result.min_cost

    def dfs(self, city, n, path, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.hasBetterPath(graph, path, next_city):
                continue
            path.append(next_city)
            visited.add(next_city)
            self.dfs(next_city, n, path, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)
            path.pop()

    def buildGraph(self, n, nodes):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in nodes:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)

        return graph

    def hasBetterPath(self, graph, path, next_city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][next_city] > graph[path[i - 1]][path[-1]] + graph[path[i]][next_city]:
                return True
        return False

############# state compression DP

        graph = self.buildGraph(roads, n)
        stateSize = 1 << n
        f = [[float('inf')] * (n + 1) for _ in range(stateSize)]
        f[1][1] = 0
        for state in range(stateSize):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)) == 0:
                    continue
                prev_state = state ^ (1 << (i - 1))
                for j in range(1, n + 1):
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    f[state][i] = min(f[state][i], f[prev_state][j] + graph[j][i])
        return min(f[stateSize - 1])

    def buildGraph(self, roads, n):
        graph = {i: {j: float('inf') for j in range(1, n + 1)} for i in range(1, n + 1)}
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)

        return graph 







    ########
