from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        result = deque()

        for i in range(len(nums)):
            if result and i - result[0] == k:
                result.popleft()

            while result and nums[i] >= nums[result[-1]]:
                result.pop()
            result.append(i)
            if i >= k - 1:
                output.append(nums[result[0]])

        return output