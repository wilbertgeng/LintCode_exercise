"""780 · Remove Invalid Parentheses"""
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        queue = collections.deque()
        queue.append(s)
        found = False
        res = []
        visited = set()
        visited.add(s)

        while queue:
            string = queue.popleft()
            if self.isValid(string):
                res.append(string)
                found = True
            if found:
                continue
            for i in range(len(string)):
                if string[i] != "(" and string[i] != ")":
                    continue
                new_string = string[:i] + string[i + 1:]
                if new_string in visited:
                    continue
                visited.add(new_string)
                queue.append(new_string)

        return res

    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != "(" and s[i] != ")":
                continue
            if s[i] == "(":
                count += 1
            if s[i] == ")":
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True

        return False
