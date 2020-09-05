class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        result = []

        cur = 0
        for num in popped:
            find = 0
            if len(result) > 0:
                if result[-1] == num:
                    result.pop()
                    find = 1
                    continue

            while cur < len(pushed):
                if pushed[cur] == num:
                    cur += 1
                    find = 1
                    break
                else:
                    result.append(pushed[cur])
                cur += 1

            if not find:
                return False

        return True

