class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0

        stack = [target]

        length = 1
        visit = set()
        visit.add(target)

        while stack:
            cur_stack = []
            while stack:
                cur = stack.pop(0)
                temp = []
                for i in range(4):
                    string = [(ord(cur[i]) - ord('0') + 1) % 10, (ord(cur[i]) - ord('0') - 1) % 10]
                    for sub_str in string:
                        temp.append(cur[0:i] + str(sub_str) + cur[i + 1:])

                for string in temp:
                    if not string in deadends and not string in visit:
                        cur_stack.append(string)
                        visit.add(string)
                    if string == '0000':
                        return length

            stack = cur_stack
            length += 1

        return -1