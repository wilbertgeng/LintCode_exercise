"""
130. Heapify"""
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, k):
        while k < len(A):
            son = k
            if k * 2 + 1 < len(A) and A[k * 2 + 1] < A[son]:
                son = k * 2 + 1
            if k * 2 + 2 < len(A) and A[k * 2 + 2] < A[son]:
                son = k * 2 + 2
            if son == k:
                break
            A[son], A[k] = A[k], A[son]
            k = son



            for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, index):
        n = len(A)
        while index < n:
            left = index * 2 + 1
            right = index * 2 + 2
            minIndex = index
            if left < n and A[left] < A[minIndex]:
                minIndex = left
            if right < n and A[right] < A[minIndex]:
                minIndex = right

            if minIndex == index:
                break

            A[minIndex], A[index] = A[index], A[minIndex]
            index = minIndex
