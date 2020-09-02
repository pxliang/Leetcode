from collections import Counter


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not S or not words:
            return 0

        def FindString(string):
            str_Stack = []
            count_Stack = []

            cur = string[0]
            count = 1
            for t, i in enumerate(string[1:]):
                if i == cur:
                    count += 1
                else:
                    str_Stack.append(cur)
                    count_Stack.append(count)
                    cur = i
                    count = 1

            str_Stack.append(cur)
            count_Stack.append(count)

            return str_Stack, count_Stack

        S_Stack, S_count = FindString(S)
        result = 0

        for string in words:
            cur_Stack, cur_count = FindString(string)
            find = 1
            if len(S_Stack) != len(cur_Stack):
                break
            for i in range(len(S_Stack)):
                if cur_Stack[i] != S_Stack[i]:
                    find = 0
                    break
                if cur_count[i] > S_count[i]:
                    find = 0
                    break
                if cur_count[i] < S_count[i] and S_count[i] < 3:
                    find = 0
                    break

            result += find

        return result

'''
comments:
1. when you write a string to #s, pay attention to the last word. For example: 'helllo', should be 1h1e2l10
'''