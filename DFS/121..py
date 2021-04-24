"""121 · Word Ladder II"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        path = [start]
        visited = {start: 0}
        queue = collections.deque(path)
        dict.add(end)
        dict.add(start)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for word_nxt in self.findNextWOrds(word, dict):
                    if word_nxt in visited:
                        continue
                    visited[word_nxt] = visited[word] + 1
                    queue.append(word_nxt)

        res = []
        self.dfs(end, start, [end], dict, visited, res)
        return res

    def dfs(self, word, start, path, dict, visited, res):
        if word == start:
            path = list(path)
            res.append(path[::-1])
            return

        for word_prv in self.findNextWOrds(word, dict):
            if visited[word_prv] != visited[word] - 1:
                continue
            path.append(word_prv)
            self.dfs(word_prv, start, path, dict, visited, res)
            path.pop()



    def findNextWOrds(self, word, dict):
        words = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[i]:
                    continue
                word_next = word[:i] + char + word[i + 1:]
                if word_next in dict:
                    words.append(word_next)

        return words
