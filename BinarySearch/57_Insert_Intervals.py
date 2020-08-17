class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def find(inter, num, left, right):

            while left <= right:
                mid = (left + right) // 2
                if inter[mid] == num:
                    return mid
                elif inter[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1

            return right

        left_idx = find([a[0] for a in intervals], newInterval[0], 0, len(intervals) - 1)
        right_idx = find([a[1] for a in intervals], newInterval[1], max(left_idx, 0), len(intervals) - 1)

        if left_idx > right_idx:
            return intervals
        else:
            new_interval = intervals[:max(left_idx, 0)]
            sub = []
            if left_idx == -1:
                sub.append(newInterval[0])
            else:
                if intervals[left_idx][1] < newInterval[0]:
                    new_interval.append(intervals[left_idx])
                    sub.append(newInterval[0])
                else:
                    sub.append(intervals[left_idx][0])

            if (right_idx + 1) >= len(intervals) or intervals[right_idx + 1][0] > newInterval[1]:
                sub.append(newInterval[1])
            else:
                sub.append(intervals[right_idx + 1][1])

            new_interval.append(sub)

            if right_idx + 1 < len(intervals):
                if intervals[right_idx + 1][0] > sub[1]:
                    new_interval.extend(intervals[right_idx + 1:])
                else:
                    if right_idx + 2 < len(intervals):
                        new_interval.extend(intervals[right_idx + 2:])

        return new_interval
