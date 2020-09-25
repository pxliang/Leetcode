from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        find = defaultdict(list)

        for w in words:
            find[w[0]].append(w)

        for a in S:
            temp = []
            while find[a]:
                new = find[a].pop()
                if len(new) > 1:
                    if new[1] == a:
                        temp.append(new[1:])
                    else:
                        find[new[1]].append(new[1:])
            find[a].extend(temp)

        left = []
        for item in find:
            left.extend(find[item])

        return len(words) - len(left)