"""144. Interleaving Positive and Negative Numbers
"""
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        left = 0
        right = len(A) - 1
        self.partition(left, right, A)

        pos = 0
        neg = 0
        for num in A:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        if neg > pos:
            left = 1
        if neg < pos:
            right = len(A) - 2

        while left <= right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2

    def partition(self, start, end, A):
        left = start
        right = end
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1


        ### Jiuzhang Solution 
        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1

        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)

    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1
        if has_same_length:
            right = len(A) - 2

        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
