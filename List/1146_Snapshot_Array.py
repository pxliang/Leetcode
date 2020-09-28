class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.id = -1

    def set(self, index: int, val: int) -> None:
        cur = self.array[index]
        if cur[-1][0] == self.id + 1:
            cur[-1][1] = val
        else:
            cur.append([self.id + 1, val])

    def snap(self) -> int:
        self.id += 1
        return self.id

    def get(self, index: int, snap_id: int) -> int:
        # print(self.array[index])
        cur = self.array[index]
        if cur[-1][0] <= snap_id:
            return cur[-1][1]
        else:
            left, right = 0, len(cur) - 1

            while left <= right:
                middle = (left + right) // 2
                if cur[middle][0] == snap_id:
                    return cur[middle][1]
                elif cur[middle][0] < snap_id:
                    left = middle + 1
                else:
                    right = middle - 1

            return cur[right][1]

