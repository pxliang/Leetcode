from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        dic = defaultdict(int)
        result = []

        for sub_str in strings:
            code = ''
            for i in range(len(sub_str) - 1):
                code += str((ord(sub_str[i + 1]) - ord(sub_str[i])) % 26)

            if code not in dic:
                dic[code] = len(result)
                result.append([sub_str])
            else:
                result[dic[code]].append(sub_str)

        return result


'''
comments:
1. understand the question correctly
2. ord()
3. %26, index difference within a ring
'''