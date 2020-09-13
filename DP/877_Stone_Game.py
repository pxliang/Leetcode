class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        record = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        total = [0 for _ in range(len(piles))]
        total[0] = piles[0]

        for i in range(len(piles)):
            record[i][i] = piles[i]

        for i in range(1, len(piles)):
            total[i] = total[i - 1] + piles[i]

        for i in range(1, len(piles)):
            for j in range(len(piles) - i):
                if j > 0:
                    left = total[i + j - 1] - total[j - 1]
                else:
                    left = total[i + j - 1]
                record[j][j + i] = max(total[i + j] - total[j] + piles[j] - record[j + 1][i + j], \
                                       left + piles[j + i] - record[j][i + j - 1])

        if total[-1] - 2 * record[0][-1] < 0:
            return True
        else:
            return False
