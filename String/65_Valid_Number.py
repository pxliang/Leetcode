class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        if not s:
            return False

        sub = s.split('e')
        if len(sub) > 2:
            return False

        def check(s):
            if not s:
                return False

            if s[0] == '+' or s[0] == '-':
                s = s[1:]

            if not s:
                return False

            count = 0

            for i, letter in enumerate(s):

                if letter == '.':
                    if count:
                        return False
                    count += 1

                elif not letter.isdigit():
                    return False

            new_s = s.split('.')
            if len(new_s) == 2:
                if not new_s[0] and not new_s[1]:
                    return False

            return True

        for letter in sub:
            if not check(letter):
                return False

        if len(sub) == 2:
            if '.' in sub[-1]:
                return False
        return True

'''
commnets:
1. think problem in high-level: divide and conquer
2. Deal with special cases first to simplify problem
'''