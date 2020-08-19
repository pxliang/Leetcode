import queue


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:

        if self.q.qsize() == self.size:
            self.sum -= self.q.get()
            self.q.put(val)
            self.sum += val
            return self.sum / self.size
        else:
            self.q.put(val)
            self.sum += val
            return self.sum / self.q.qsize()
        