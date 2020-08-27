class Solution:
    def calculate(self, s: str) -> int:

        cal = []

        pre = ''
        for i in s[::-1]:
            if i.isdigit():
                if pre:
                    pre = i + pre
                    cal[-1] = int(pre)
                else:
                    pre = i
                    cal.append(int(pre))

            elif i == '+' or i == '-' or i == '(' or i == ')':

                pre = ''

                if i == '(':
                    total = cal.pop()
                    while cal:
                        cur = cal.pop()
                        if cur == ')':
                            cal.append(total)
                            break
                        if cur == '+':
                            total += cal.pop()
                        elif cur == '-':
                            total -= cal.pop()
                else:
                    cal.append(i)

        total = cal.pop()
        while cal:
            cur = cal.pop()
            if cur == '+':
                total += cal.pop()
            elif cur == '-':
                total -= cal.pop()

        return total
