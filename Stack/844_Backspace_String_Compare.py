class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        result1 = []
        for s in S:
            if s == '#':
                if result1:
                    result1.pop()
            else:
                result1.append(s)

        result2 = []
        for t in T:
            if t == '#':
                if result2:
                    result2.pop()
            else:
                result2.append(t)

        if result1 == result2:
            return True
        else:
            return False