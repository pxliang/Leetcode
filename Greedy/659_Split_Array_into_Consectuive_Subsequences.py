from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        if not nums:
            return True

        left = Counter(nums)
        right = Counter()

        for n in nums:
            if not left[n]:
                continue
            elif right[n - 1]:
                left[n] -= 1
                right[n - 1] -= 1
                right[n] += 1
            elif left[n + 1] and left[n + 2]:
                left[n] -= 1
                left[n + 1] -= 1
                left[n + 2] -= 1
                right[n + 2] += 1
            else:
                return False

        return True