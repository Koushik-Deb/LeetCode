class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse=True,key=lambda x:(x[1],-x[0]))
        # print(intervals)
        slen = len(intervals)
        count = slen
        for i in range(slen-1):
            # print(intervals[i],intervals[i+1])
            if intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                # print("wh")
                intervals[i+1] = intervals[i]
                count-=1
        return count
    