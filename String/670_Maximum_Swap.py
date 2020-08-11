class Solution:
    def maximumSwap(self, num: int) -> int:

        string = str(num)
        current = 0
        pre = current
        for t, sub in enumerate(string[:-1]):
            if int(string[t + 1]) > int(sub):
                current = t
                break

        max_num = int(string[current])
        max_point = current
        for j in range(current + 1, len(string)):
            if int(string[j]) >= max_num:
                max_num = int(string[j])
                max_point = j

        start = 0
        for j in range(current + 1):
            if int(string[j]) < max_num:
                start = j
                break

        result = ''

        for t in range(len(string)):
            if t == start:
                result += string[max_point]

            elif t == max_point:
                result += string[start]
            else:
                result += string[t]

        return int(result)

'''
comments:
1. Find the first increasing number
2. swap the largest number in the latter part with the first smaller number in the previous part
'''