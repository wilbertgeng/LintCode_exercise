"""547. Intersection of Two Arrays
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        m = len(nums1)
        n = len(nums2)

        dict1 = set(nums1)
        res = set()
        for i in range(n):
            if nums2[i] in dict1:
                res.add(nums2[i])

        return list(res)
            
