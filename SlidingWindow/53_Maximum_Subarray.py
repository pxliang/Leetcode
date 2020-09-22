class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = 0
        max_sum = -float(inf)

        for n in nums:
            if total + n < 0:
                total = 0
            else:
                total += n
                max_sum = max(max_sum, total)

            if max_sum < 0:
                max_sum = max(n, max_sum)

        return max_sum