"""615 · Course Schedule"""
class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        graph = [[] for _ in range(numCourses)]
        for relation in prerequisites:
            graph[relation[1]].append(relation[0])
        indegree = self.getIndegree(graph)
        start_courses = [course for course in range(numCourses) if indegree[course] == 0]
        if not start_courses:
            return False

        queue = collections.deque(start_courses)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(order) == numCourses

    def getIndegree(self, graph):
        indegree = {n: 0 for n in range(len(graph))}
        for n in range(len(graph)):
            for course in graph[n]:
                indegree[course] += 1
        return indegree
