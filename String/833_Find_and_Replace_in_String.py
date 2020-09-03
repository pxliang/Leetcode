class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:

        if not S:
            return ""
        if not indexes:
            return S

        stack = []

        for t, num in enumerate(indexes):
            if S[num] == sources[t][0]:
                off = 0
                find = 1
                for cur in sources[t]:
                    if cur == S[num + off]:
                        off += 1
                    else:
                        find = 0
                        break
                if find:
                    if not stack:
                        stack.append((num, num + len(sources[t]), targets[t]))
                    else:
                        left, right = 0, len(stack) - 1
                        while left <= right:
                            middle = (left + right) // 2
                            if stack[middle][0] < num:
                                left = middle + 1
                            else:
                                right = middle - 1
                        stack[left:left] = [(num, num + len(sources[t]), targets[t])]

        result = ''
        pre = 0
        for pattern in stack:
            start, end, string = pattern
            result += S[pre:start] + string
            pre = end
        if pre < len(S):
            result += S[pre:]
        return result

'''
comments:
1. the order of idex is not in order, so you need to consider it
2. ranth than using binary search, you can use one forward pass by put the corresponding target string to the 
corresponding postion
'''