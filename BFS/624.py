"""624. Remove Substrings
"""
class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        queue = collections.deque([s])
        visited = set()
        visited.add(s)
        cnt = len(s)

        while queue:
            string = queue.popleft()
            cnt = min(cnt, len(string))
            for w in dict:
                found = string.find(w)
                while found != -1:
                    new_str = string[:found] + string[found + len(w):]
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append(new_str)
                    found = string.find(w, found + 1)

        return cnt
