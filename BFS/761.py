"""761. Smallest Subset
"""
class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        # write your code here
        total = sum(arr)
        arr.sort(reverse = True)

        queue = [0]

        for i in range(len(arr)):
            for j in range(len(queue)):
                subset = int(queue[j])
                queue.append(subset + arr[j])
                if (subset + arr[j]) * 2 > total:
                    return i + 1

        return len(arr)
