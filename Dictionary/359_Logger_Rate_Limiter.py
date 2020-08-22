from collections import defaultdict


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if not message:
            return Null
        if message in self.dic:
            if abs(timestamp - self.dic[message]) > 9:
                self.dic[message] = timestamp
                return True
            else:
                return False
        self.dic[message] = timestamp
        return True

'''
comments:
1. update the record every time you print a string
'''