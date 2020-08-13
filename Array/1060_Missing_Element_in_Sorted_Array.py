class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        total = 0
        for t, num in enumerate(nums[:-1]):
            pre = total
            total += (nums[t + 1] - nums[t] - 1)
            if total >= k:
                return nums[t] + (k - pre)

        return nums[t + 1] + (k - total)

### binary search

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            diff = (nums[mid] - nums[0]) - mid
            if diff < k:
                left = mid + 1
            elif diff >= k:
                right = mid - 1

        return nums[right] + k - (nums[right] - nums[0]) + right

'''
comments:
1. [a, b]
2. terminal condition: left <= right
3. left = mid + 1; right = mid - 1
'''
