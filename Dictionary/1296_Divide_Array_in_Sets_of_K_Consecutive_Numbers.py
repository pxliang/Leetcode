from collections import Counter, OrderedDict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        time = Counter(nums)
        record = sorted(time)

        for num in record:
            if time[num] > 0:
                t = time[num]
                time[num] = 0
                for i in range(1, k):
                    time[num + i] -= t
                    if time[num + i] < 0:
                        return False

        return True