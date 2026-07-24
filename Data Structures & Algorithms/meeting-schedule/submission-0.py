"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        ### Sort by start times ###
        intervals.sort(key=lambda i: i.start )
        print([(i.start,i.end) for i in intervals])

        for i in range(1,len(intervals)):

            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True