class Solution:
    def decodeString(self, s: str) -> str:

        result = ''
        count = []
        letter = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                cur_c = s[i]
                while s[i + 1].isdigit():
                    i += 1
                    cur_c += s[i]
                count.append(int(cur_c))
            elif s[i] == '[':
                letter.append(s[i])
            elif s[i] == ']':
                current = ''
                while letter:
                    word = letter.pop()
                    if word == '[':
                        time = count.pop()
                        current = current * time
                        letter.append(current)
                        break
                    current = word + current
            else:
                letter.append(s[i])
            i += 1

        while letter:
            string = letter.pop(0)
            result += string
        return result

'''
comments:
1. perserve output sequence
'''