from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_stack = deque()
        max_stack = deque()
        left = 0
        indicate = 0
        result = 0
        for right, n in enumerate(nums):
            while min_stack and n <= nums[min_stack[-1]]:
                min_stack.pop()
            if not min_stack:
                indicate = 0
            min_stack.append(right)

            while max_stack and n >= nums[max_stack[-1]]:
                max_stack.pop()
            if not max_stack:
                indicate = 1
            max_stack.append(right)

            if nums[max_stack[0]] - nums[min_stack[0]] > limit:
                result = max(result, right - left)
                if indicate:
                    while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                        left = min_stack.popleft() + 1
                else:
                    while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                        left = max_stack.popleft() + 1

        if nums[max_stack[0]] - nums[min_stack[0]] <= limit:
            result = max(result, right - left + 1)
        return result

'''
comments:
1. process the left part in the queue when the while loop terminate
'''