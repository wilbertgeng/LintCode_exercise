"""197 · Permutation Index"""
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        permutation = 1
        result = 0

        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation
            permutation *= len(A) - i

        return result + 1

"""Q：为了找寻每个元素右侧有多少元素比自己小，用了O(n^2)的时间，能不能更快些？
A：可以做到O(nlogn)，但是很复杂，这是另外一个问题了，可以使用BST，
归并排序或者线段树：http://www.lintcode.com/zh-cn/problem/count-of-smaller-number-before-itself/
Q：元素有重复怎么办？
A：好问题！元素有重复，情况会复杂的多。因为这会影响 A[i] 右侧元素的排列数，
此时的排列数计算方法为总元素数的阶乘，除以各元素值个数的阶乘，例如 [1, 1, 1, 2, 2, 3] ，排列数为
6! ÷ (3! × 2! × 1!) 。为了正确计算阶乘数，需要用哈系表记录 A[i] 及右侧的元素值个数，
并考虑到 A[i] 与右侧比其小的元素 A[k] 交换后，要把 A[k] 的计数减一。用该哈系表计算正确的阶乘数。
而且要注意，右侧比 A[i]小 的重复元素值只能计算一次，不要重复计算！"""
