from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # print(len(str1))
        record = defaultdict(str)

        for i, word in enumerate(str1):
            if word != str2[i]:
                if word in record:
                    if record[word] != str2[i]:
                        return False
                else:
                    record[word] = str2[i]

        unvisit = 26 - len(Counter(str2))
        print(unvisit)
        if unvisit == 0:
            visit = set()
            # print(record)
            for item in record:
                if not item in visit:
                    cur = [item]
                    visit.add(item)
                    while cur:
                        # print(cur)
                        if cur[-1] not in record:
                            break
                        else:
                            if record[cur[-1]] in cur:
                                print('same: ', record[cur[-1]])
                                return False
                            else:
                                cur.append(record[cur[-1]])
                                visit.add(record[cur[-1]])

        return True