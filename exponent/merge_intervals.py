from typing import List

def starter(interval):
    return interval[0]

def find_max(intervals):
    max = float("-inf")
    for x in intervals:
        if x[1] > max:
            max = x[1]
    return max

# nlogn soln

def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=starter)
    max_val = find_max(intervals)
    if len(intervals) == 0:
        return []
    new_intervals = []
    start = intervals[0][0]
    finish = intervals[0][1]
    index = 0
    not_done = True
    while not_done:
        while index <= len(intervals) - 2 and intervals[index + 1][0] <= finish:
            # merge
            finish = max(intervals[index + 1][1], intervals[index][1])
            index += 1
        new_intervals.append([start, finish])
        if finish == max_val:
            not_done = False
        if index < len(intervals) - 1:
            index += 1
            start = intervals[index][0]
            finish = intervals[index][1]

    return new_intervals
    
# debug your code below
print(mergeIntervals([[1,3], [2,6], [8,10], [15,18]]))
print(mergeIntervals([[1,4], [4, 5]]))
print(mergeIntervals([[1,4], [2,3]]))
print(mergeIntervals([[1,2], [3,4], [5,6], [7,8]]))
