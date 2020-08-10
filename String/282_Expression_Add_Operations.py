class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        if not num:
            return []

        def Operation(result, s):

            new_result = []
            for sub in result:
                if sub[-1] != '0' or (len(sub) > 1 and sub[-2] != '+' and sub[-2] != '-' and sub[-2] != '*'):
                    new_result.append(sub + s)
                new_result.append(sub + '+' + s)
                new_result.append(sub + '-' + s)
                new_result.append(sub + '*' + s)

            return new_result

        output = []
        result = [num[0]]
        for i in num[1:]:
            result = Operation(result, i)

        for sub in result:
            op = '+'
            last = 0
            stack = []
            for t, letter in enumerate(sub):

                if letter == '+' or letter == '-' or t == (len(sub) - 1):
                    if t == (len(sub) - 1):
                        stack.append(letter)

                    string = ''
                    while stack:
                        string = stack.pop() + string
                    sub_mul = string.split('*')
                    multiple = 1
                    for sm in sub_mul:
                        multiple *= int(sm)
                    if op == '+':
                        last = last + multiple
                    else:
                        last = last - multiple
                    op = letter
                else:
                    stack.append(letter)

            if last == target:
                output.append(sub)

        return output

'''
comments:
1. List all possible strings first
'''