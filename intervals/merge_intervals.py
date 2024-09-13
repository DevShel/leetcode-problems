from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        output_list = []
        i = 0
        while (i < len(intervals) - 1):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            next_start, next_end = intervals[i+1][0], intervals[i+1][1]
            
            if (curr_end > next_end):
                intervals[i] = [curr_start, curr_end]
                intervals.pop(i + 1)
            elif(curr_end <= next_end and curr_end >= next_start):
                intervals[i] = [curr_start, next_end]
                intervals.pop(i + 1)
            else:
                output_list.append(intervals[i])
                i+=1
        if (i == len(intervals) - 1): output_list.append(intervals[i])

        return output_list