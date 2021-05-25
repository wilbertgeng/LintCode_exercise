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
        ### Practice:
        shortest = len(s)
        if not s:
            return 0

        queue = collections.deque([s])
        visited = set()
        visited.add(s)

        while queue:
            string = queue.popleft()
            for w in dict:
                idx = string.find(w)
                while idx != -1:
                    string_new = string[:idx] + string[idx + len(w):]
                    if string_new not in visited:
                        shortest = min(shortest, len(string_new))
                        queue.append(string_new)
                        visited.add(string_new)
                        idx = string.find(w, idx + 1)

        return shortest



        #####
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
