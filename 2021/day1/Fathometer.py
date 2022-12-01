"""A Fathometer is used to measure the depth of the ocean floor"""


from typing import List


class Fathometer:
    def __init__(self, measurements: List[int]):
        self.measurements = measurements

    def countIncreases(self) -> int:
        """Counts the number of times a depth measurement increases from the previous measurement.

        Return: 
            An int representing the number of increases between depth measurements.
        """
        prevDepth = None
        increases = 0
        for measurement in self.measurements:
            currentDepth = measurement
            if prevDepth and currentDepth > prevDepth:
                increases += 1
            prevDepth = currentDepth
        return increases

    def countSlidingWindowIncreases(self, windowSize: int) -> int:
        """Count the number of times the sum of measurements in this sliding window increases from the previous sum.

        Args:
            windowSize: An int representing the size of the sliding window.
        Returns: 
            An int representing the number of increases between the sliding depth windows.
        """
        increases = 0
        if len(self.measurements) < windowSize:
            # Not long enough for any sliding windows
            return increases

        prevWindow = None
        for i in range(len(self.measurements)):
            if i + windowSize <= len(self.measurements):
                currentWindow = sum(self.measurements[i:i+windowSize])
            if prevWindow and currentWindow > prevWindow:
                increases += 1

            prevWindow = currentWindow
        return increases
