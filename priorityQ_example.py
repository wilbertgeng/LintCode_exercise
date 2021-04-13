
class Solution:
    def findSequence(self, nums):
        if not nums:
            return []
        import heapq
        nums.sort(key = lambda x: x[1])
        elements = []
        for num in nums:
            elements.append((num[2], num[1], num[0]))

        heap = [elements[0]]

        timer = elements[0][1]
        # tuple: (exq_time, q_time, idx)
        index = 1
        res = []
        print(elements)
        while heap:
            exq_time, q_time, idx = heapq.heappop(heap)
            res.append(idx)
            timer += exq_time
            print(timer)

            if index < len(elements) and elements[index][1] > timer:
                timer = elements[index][1]
                heapq.heappush(elements[index])
                index += 1
            for i in range(index, len(elements)):
                if elements[i][1] <= timer:
                    heapq.heappush(heap, elements[i])
                    index += 1
                else:
                    break
        return res

s = Solution()
output = s.findSequence([[1, 1, 9], [2, 2, 8], [3, 8, 2], [4, 8, 9]])
print(output)
