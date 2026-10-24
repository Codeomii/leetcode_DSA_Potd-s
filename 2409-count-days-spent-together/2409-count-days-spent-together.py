class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def day(s):
            m, d = map(int, s.split('-'))
            return sum(days[:m-1]) + d
        return max(0, min(day(leaveAlice), day(leaveBob)) - max(day(arriveAlice), day(arriveBob)) + 1)