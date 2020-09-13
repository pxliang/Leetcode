class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        i = 0
        while i < len(s):

            if s[i] == ' ':
                i += 1
            elif s[i] == '*' or s[i] == '/':
                op = 1 if s[i] == '*' else 0
                num1 = stack.pop()
                i += 1
                num2 = ''
                while i < len(s) and (s[i] == ' ' or s[i].isdigit()):
                    if s[i] != ' ':
                        num2 += s[i]
                    i += 1
                if op:
                    stack.append(str(int(num1) * int(num2)))
                else:
                    stack.append(str(int(num1) // int(num2)))

            elif s[i].isdigit():
                num = s[i]
                i += 1
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(num)
            else:
                stack.append(s[i])
                i += 1

        result = int(stack.pop(0))
        while stack:
            cur = stack.pop(0)
            if cur == '+':
                result += int(stack.pop(0))
            else:
                result -= int(stack.pop(0))

        return result

'''
comments:
1. deal with ' ' using replace(' ', '')
2. strip(), split(), replace(), isdigit(), ord(), chr()
'''