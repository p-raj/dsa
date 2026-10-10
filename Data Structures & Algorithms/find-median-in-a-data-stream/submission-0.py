class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr = MedianFinder.radix_sort_with_negatives(self.arr)
        if len(self.arr) % 2:
            return self.arr[len(self.arr)//2]
        r = len(self.arr)//2
        l = r-1
        return (self.arr[l] + self.arr[r])/2
        
    def counting_sort_for_radix(arr, exp):
        """A standard counting sort subroutine tailored for Radix Sort."""
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Store occurrences of digits (0-9)
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Change count[i] so it contains the actual position in output
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array stably
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy the sorted elements back to the original array
        for i in range(n):
            arr[i] = output[i]


    def standard_radix_sort(arr):
        """Standard Radix Sort for non-negative integers."""
        if not arr:
            return arr

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            MedianFinder.counting_sort_for_radix(arr, exp)
            exp *= 10
        return arr


    def radix_sort_with_negatives(arr):
        """Extended Radix Sort to handle mixed positive and negative integers."""
        if not arr:
            return arr

        # 1. Partition into negative and positive arrays
        negatives = [x for x in arr if x < 0]
        positives = [x for x in arr if x >= 0]

        # 2. Convert negatives to positive absolute values
        negatives = [abs(x) for x in negatives]

        # 3. Sort both arrays using standard Radix Sort
        MedianFinder.standard_radix_sort(positives)
        MedianFinder.standard_radix_sort(negatives)

        # 4. Reverse and re-negate the negative array to restore correct order
        # (e.g., [2, 10] becomes [-10, -2])
        negatives = [-x for x in reversed(negatives)]

        # 5. Merge the results
        return negatives + positives


