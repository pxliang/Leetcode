from collections import defaultdict
import string
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return None

        alpha = list(string.ascii_lowercase)

        look = []
        for i in digits:
            temp = []
            if int(i) < 7:
                index = (int(i) - 2) * 3
                for t in range(3):
                    temp.append(alpha[index + t])
            elif int(i) == 7:
                index = (int(i) - 2) * 3
                for t in range(4):
                    temp.append(alpha[index + t])
            elif int(i) == 8:
                index = (int(i) - 2) * 3 + 1
                for t in range(3):
                    temp.append(alpha[index + t])
            else:
                index = (int(i) - 2) * 3 + 1
                for t in range(4):
                    temp.append(alpha[index + t])
            look.append(temp)

        result = product(*look)
        output = []

        for item in list(result):
            word = ''
            for s in item:
                word += s
            output.append(word)

        return output