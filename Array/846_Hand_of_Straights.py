from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if not hand:
            return False

        dic = Counter(hand)
        stack = sorted(dic.items())
        stack = list(map(list, stack))

        while len(stack) >= W:
            cur = stack[0][0]
            stack[0][1] -= 1
            if stack[0][1] == 0:
                dele = [0]
            else:
                dele = []
            # print('stack: ', stack)
            for i in range(1, W):
                if stack[i][0] - 1 == cur:
                    cur = stack[i][0]
                    stack[i][1] -= 1
                    if stack[i][1] == 0:
                        dele.append(i)
                else:
                    return False
            for i in dele[::-1]:
                stack.pop(i)
        if stack:
            return False
        else:
            return True

