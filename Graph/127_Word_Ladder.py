from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        start_queue = [beginWord]
        end_queue = [endWord]

        name_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                name_dict[word[:i] + '*' + word[i + 1:]].append(word)

        visit = set([endWord, beginWord])
        n = 0
        while start_queue and end_queue:
            if len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue

            next_queue = []
            while start_queue:
                current = start_queue.pop(0)

                # print('current: ', current)
                for i in range(len(current)):
                    if current[:i] + '*' + current[i + 1:] in name_dict:
                        for next_s in name_dict[current[:i] + '*' + current[i + 1:]]:
                            if next_s in end_queue:
                                return n + 2
                            if next_s not in visit:
                                next_queue.append(next_s)
                                visit.add(next_s)
            n += 1
            start_queue = next_queue
            # print(start_queue)

        return 0

'''
comments:
1. How to judge if there is only one/two/... letters different between two given strings? Generate a dictionary with strings 
have blank letter
2. Bi-directional BFS. 
3. Traverse a graph layer by layer
'''
