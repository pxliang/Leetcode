from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        num = Counter(deck)
        length = [num[i] for i in num]

        def gcd(num1, num2):

            while num2:
                num1, num2 = num2, num1 % num2

            return num1

        value = length[0]
        for i in range(1, len(length)):
            value = gcd(value, length[i])

        return value > 1