class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)

        record = [[0 for _ in range(len(word2))] for _ in range(len(word1))]

        if word1[0] == word2[0]:
            record[0][0] = 0
            flag1 = 0
            flag2 = 0
        else:
            record[0][0] = 1
            flag1 = 1
            flag2 = 1

        for i in range(1, len(word1)):
            if flag1 and word1[i] == word2[0]:
                record[i][0] = record[i - 1][0]
                flag1 = 0
            else:
                record[i][0] = record[i - 1][0] + 1

        for i in range(1, len(word2)):
            if flag2 and word2[i] == word1[0]:
                record[0][i] = record[0][i - 1]
                flag2 = 0
            else:
                record[0][i] = record[0][i - 1] + 1
        # print(record)
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                add = 0 if word1[i] == word2[j] else 1
                record[i][j] = min(record[i - 1][j] + 1, record[i][j - 1] + 1, record[i - 1][j - 1] + add)

        return record[-1][-1]