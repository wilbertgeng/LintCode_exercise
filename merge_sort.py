class Solution:
    def sortIntegers(self, A):
        if not A:
            return A

        temp = [0] * len(A)

        self.mergeSort(A, 0, len(A) - 1, temp)

    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return
        self.mergeSort(A, start, (start + end) // 2, temp)
        self.mergeSort(A, (start + end) // 2 + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        mid = (start + end) // 2
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1

        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1

        for i in range(start, index):
            A[i] = temp[i]














########
