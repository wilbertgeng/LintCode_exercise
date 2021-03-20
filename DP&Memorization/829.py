"""829. Word Pattern II (Hard)"""
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.isMatch(pattern, str, {}, set())

    def isMatch(self, pattern, string, map, used):
        if not pattern:
            return not string

        char = pattern[0]
        if char in map:
            word = map[char]
            if string.startswith(word):
                return self.isMatch(pattern[1:], string[len(word):], map, used)
            else:
                return False
        
        for length in range(len(string)):
            word = string[:length + 1]
            if word in used:
                continue

            used.add(word)
            map[char] = word
            if self.isMatch(pattern[1:], string[length + 1:], map, used):
                return True
            used.remove(word)
            del map[char]

        return False
