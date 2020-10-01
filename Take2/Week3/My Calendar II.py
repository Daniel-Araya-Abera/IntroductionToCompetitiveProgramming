# My Calendar II
# https://leetcode.com/problems/my-calendar-ii/
# Difficulty: Medium

class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.doubleBookings = []
        

    def book(self, start: int, end: int) -> bool:
        for currStart, currEnd in self.doubleBookings:
            # if currStart < end and currEnd > start:
            if not(end <= currStart or currEnd <= start):
                return False

        for currStart, currEnd in self.bookings:
            if not(end <= currStart or currEnd <= start):
                newStart = max(start,currStart)
                newEnd = min(end, currEnd)
                self.doubleBookings.append((newStart,newEnd))

        self.bookings.append((start,end))
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)