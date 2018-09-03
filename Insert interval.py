# Definition for an interval.
"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]

示例 2:
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not newInterval: return []
        if len(intervals) == 0: return [newInterval]
        out = []
        for i in range(len(intervals)):
            if newInterval.start < intervals[i].start:
                if newInterval.end < intervals[i].start:
                    out.append(newInterval)
                    out += intervals[i:]
                    return out
                elif intervals[i].start <= newInterval.end <= intervals[i].end:
                    newInterval.end = intervals[i].end
                else:
                    continue
            elif intervals[i].end >= newInterval.start >= intervals[i].start:
                if newInterval.end <= intervals[i].end:
                    newInterval.start = intervals[i].start
                    newInterval.end = intervals[i].end
                else:
                    newInterval.start = intervals[i].start
            else:
                out.append(intervals[i])
        out.append(newInterval)
        return out


s = Solution()
out = s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 8))
for i in out:
    print([i.start, i.end])