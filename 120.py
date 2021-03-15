"""120. Word Ladder
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        queue = collections.deque([start])
        distance = {start: 0}
        dict.add(end)

        while queue:
            word = queue.popleft()
            for w in self.getNextWords(word, dict):
                if w == end:
                    return distance[word] + 1
                if w in distance:
                    continue
                queue.append(w)
                distance[w] = distance[word] + 1

        return 0


    def getNextWords(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                new_word = left + char + right
                if new_word in dict:
                    words.append(new_word)

        return words













#####
