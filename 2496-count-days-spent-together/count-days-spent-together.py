class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # prefix[m] = number of days in all months before month m (1-indexed)
        prefix = [0]
        for d in days:
            prefix.append(prefix[-1] + d)

        def to_day(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return prefix[month - 1] + day

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))

        return max(0, end - start + 1)