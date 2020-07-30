#### initial version

from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        dic = defaultdict()
        word_dic = defaultdict()

        if len(pattern) != len(str.split(' ')):
            return False

        for i, word in enumerate(str.split(' ')):
            if pattern[i] not in dic:
                if word not in word_dic:
                    dic[pattern[i]] = word
                    word_dic[word] = pattern[i]
                else:
                    return False
            else:
                if word in word_dic:
                    if word_dic[word] != pattern[i]:
                        return False
                else:
                    return False

        return True

