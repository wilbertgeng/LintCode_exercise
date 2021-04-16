"""13. Implement strStr()
"""
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0

        m = len(source)
        n = len(target)

        for i in range(m - n + 1):
            for j in range(n):
                if source[i + j] != target[j]:
                    break

            else:
                return i

        return -1












        ####
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else: ## !! careful
                return i
        return -1











###
