from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = Counter(nums)

        h = []
        index = defaultdict(list)
        for item in dic:
            h.append(dic[item])
            index[dic[item]].append(item)

        result = []
        res = heapq.nlargest(k, h)
        for i in set(res):
            for j in index[i]:
                result.append(j)

        return result