class Solution:
    def minWindow(self, S: str, T: str) -> str:

        record = [[-1 for _ in range(len(S))] for _ in range(len(T))]

        if S[0] == T[0]:
            record[0][0] = 0

        for i in range(1, len(S)):
            if S[i] == T[0]:
                record[0][i] = i

            for j in range(len(T) - 1):
                if record[j][i - 1] == -1:
                    break
                if S[i] == T[j + 1]:
                    record[j + 1][i] = record[j][i - 1]
                if record[j][i] == -1:
                    record[j][i] = record[j][i - 1]

        min_value = 20001
        result = [0, 20000]
        for i in range(len(S)):
            if record[len(T) - 1][i] > -1:
                if i - record[len(T) - 1][i] < min_value:
                    min_value = i - record[len(T) - 1][i]
                    result[0], result[1] = record[len(T) - 1][i], i

        if min_value < 20001:
            return S[result[0]:result[1] + 1]
        else:
            return ""