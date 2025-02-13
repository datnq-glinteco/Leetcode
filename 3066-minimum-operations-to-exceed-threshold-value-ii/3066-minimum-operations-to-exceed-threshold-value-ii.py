import heapq


class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        num_operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            num_operations += 1

        return num_operations