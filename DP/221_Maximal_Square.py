class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        record = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        max_num = 0

        for i in range(len(matrix)):
            record[i][0] = int(matrix[i][0])
            if record[i][0] > max_num:
                max_num = record[i][0]

        for j in range(len(matrix[0])):
            record[0][j] = int(matrix[0][j])
            if record[0][j] > max_num:
                max_num = record[0][j]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]):
                    if record[i - 1][j] == record[i - 1][j - 1] and record[i - 1][j - 1] == record[i][j - 1]:
                        record[i][j] = record[i - 1][j] + 1
                    else:
                        record[i][j] = min(record[i - 1][j], record[i - 1][j - 1], record[i][j - 1]) + 1
                    if record[i][j] > max_num:
                        max_num = record[i][j]

        return max_num * max_num