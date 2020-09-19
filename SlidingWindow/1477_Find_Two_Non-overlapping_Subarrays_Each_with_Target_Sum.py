class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        result = []
        pre = [float(inf) for _ in range(len(arr))]
        post = [float(inf) for _ in range(len(arr))]
        total = 0
        left = 0

        for right, num in enumerate(arr):
            total += num
            if total == target:
                result.append((left, right))
                if left < len(arr) - 1:
                    total -= arr[left]
                    left += 1
            elif total > target:
                total = total - arr[left]
                left += 1
                while left < right and total > target:
                    total -= arr[left]
                    left += 1

                if total == target:
                    result.append((left, right))
                    total -= arr[left]
                    left += 1
        if len(result) < 2:
            return -1

        start = result[0][1]
        cur_length = float(inf)
        for item in result:
            cur_length = min(cur_length, item[1] - item[0] + 1)
            for i in range(start, item[1] + 1):
                pre[i] = cur_length
            start = item[1] + 1
        for i in range(start, len(arr)):
            pre[i] = cur_length

        start = result[-1][0]
        cur_length = result[-1][1] - result[-1][0] + 1
        for item in result[::-2]:
            for i in range(item[0] + 1, start + 1):
                post[i] = cur_length
            start = item[0]
            cur_length = min(cur_length, item[1] - item[0] + 1)

        for i in range(0, start + 1):
            post[i] = cur_length

        min_length = float(inf)

        for item in result:
            if item[0] == 0 and item[1] == len(arr) - 1:
                return -1
            elif item[0] - 1 < 0:
                side = post[item[1] + 1]
            elif item[1] + 1 == len(arr):
                side = pre[item[0] - 1]
            else:
                side = min(pre[item[0] - 1], post[item[1] + 1])
            min_length = min((item[1] - item[0] + 1) + side, min_length)
            if min_length == 6:
                print(item)

        if min_length == float(inf):
            return -1
        else:
            return min_length

'''
comments:
1. how to get sum of a continuous subarray and move left and right point correspondingly
2. the index to assign values to the pre and post
'''