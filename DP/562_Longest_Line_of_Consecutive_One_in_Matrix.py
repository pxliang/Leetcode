class Solution:
    def longestLine(self, M: List[List[int]]) -> int:

        if not M:
            return 0

        record = [[[0 for _ in range(4)] for _ in range(len(M[0]))] for _ in range(len(M))]

        result = 0
        if M[0][0]:
            result = 1
            for i in range(4):
                record[0][0][i] = 1

        for i in range(1, len(M)):
            if M[i][0]:
                record[i][0][0] = 1
                record[i][0][1] = 1
                record[i][0][2] = record[i - 1][0][2] + 1
                record[i][0][3] = 1
                result = max(result, record[i][0][2])

        for j in range(1, len(M[0])):
            for i in range(len(M)):
                if M[i][j]:
                    record[i][j][0] = record[i][j - 1][0] + 1
                    if i == 0:
                        record[i][j][1] = 1
                        record[i][j][2] = 1
                    else:
                        record[i][j][1] = record[i - 1][j - 1][1] + 1
                        record[i][j][2] = record[i - 1][j][2] + 1
                    if i == len(M) - 1:
                        record[i][j][3] = 1
                    else:
                        record[i][j][3] = record[i + 1][j - 1][3] + 1
                    result = max(result, record[i][j][0], record[i][j][1], record[i][j][2], record[i][j][3])

        return result

