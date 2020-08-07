from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        a = defaultdict(int)
        for i, num in enumerate(nums1):
            a[num] += 1

        for i, num in enumerate(nums2):
            if a[num]:
                result.append(num)
                a[num] -= 1

        return result