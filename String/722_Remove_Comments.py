class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        if not source:
            return []
        stack = []
        block = 0
        for j, string in enumerate(source):
            if not block:
                temp = []
            i = 0
            while i < len(string):
                s = string[i]

                if s == '/':
                    if i < len(string) - 1 and string[i + 1] == '/' and not block:
                        if temp:
                            stack.append(''.join(temp))
                        i += 1
                        break
                    elif i < len(string) - 1 and string[i + 1] == '*' and not block:
                        i += 1
                        block = 1
                    else:
                        if not block:
                            temp.append(s)

                elif s == '*':
                    if i < len(string) - 1 and string[i + 1] == '/' and block:
                        i += 1
                        block = 0
                    else:
                        if not block:
                            temp.append(s)
                else:
                    if not block:
                        temp.append(s)

                if not block and temp and i == len(string) - 1:
                    stack.append(''.join(temp))
                i += 1

        return stack

'''
comments:
1. use while to skip element in python
2. judge special characteries, from i-1 to i, not from i to i-1 (overlap)
'''