class Solution:
    # find angle between hour and 0degree - hourbetween 0 amd minute hand
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = 6
        hour_angle = 30

        minute_angle = min_angle * minutes
        hour_angle = (hour % 12 + minutes/60.0) * hour_angle

        diff = abs(hour_angle - minute_angle)
        return min(diff, 360-diff)