from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        count_A = 0
        dic_sec = defaultdict(int)
        dic_gue = defaultdict(int)

        for t, letter in enumerate(secret):
            if guess[t] == letter:
                count_A += 1
            else:
                dic_sec[letter] += 1
                dic_gue[guess[t]] += 1

        count_B = 0

        for item in dic_gue:
            if dic_sec[item] > 0:
                count_B += min(dic_sec[item], dic_gue[item])
                dic_sec[item] -= min(dic_sec[item], dic_gue[item])

        return '%dA%dB' % (count_A, count_B)

### one round

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        dic = defaultdict(int)
        bull, cow = 0, 0

        for t, letter in enumerate(secret):
            if letter == guess[t]:
                bull += 1
            else:
                cow += int(dic[guess[t]] > 0) + int(dic[letter] < 0)
                dic[letter] += 1
                dic[guess[t]] -= 1

        return '%dA%dB' % (bull, cow)

'''
comments:
1. use one dictionary for two strings
2. letter in secrest is the supply, and letter in guess is customer
'''