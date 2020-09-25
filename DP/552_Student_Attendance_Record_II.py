class Solution:
    def checkRecord(self, n: int) -> int:

        if n == 1:
            return 3
        elif n == 2:
            return 8
        elif n == 0:
            return 1
        else:
            a, b, c, d, e, f = [1, 0, 3, 1, 1, 2]
            M = 10 ** 9 + 7
            for i in range(2, n):
                a, b, c, d, e, f = c, a, (a + b + c + d + e + f) % M, f, d, (f + e + d) % M

            return (a + b + c + d + e + f) % M