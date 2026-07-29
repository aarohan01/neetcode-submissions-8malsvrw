"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        ##### Line Sweep ######
        # O(n)
        # O(n)
        time = []
        for i in intervals:
            time.append((i.start,+1))
            time.append((i.end,-1))

        time.sort()

        maxrooms = 0
        currooms = 0
        for x,y in time:

            currooms += y
            maxrooms = max(maxrooms,currooms)
        return maxrooms
