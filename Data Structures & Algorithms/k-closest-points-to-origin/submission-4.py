class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p in points:
            d = math.sqrt(((0 - p[0]) ** 2) + ((0 - p[1]) ** 2))
            res.append((d, p))

        def lomuto_partition(arr, low, high):
            pivot = arr[high][0]
            i = low - 1
            for j in range(low, high):
                if arr[j][0] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quickselect(arr, low, high, k):
            """
            Rearranges the array so that the k smallest elements 
            occupy the first k positions (indices 0 to k-1).
            """
            if low <= high:
                # Partition the array around a pivot
                pivot_idx = lomuto_partition(arr, low, high)
                
                # If pivot is exactly at index k, the first k elements are found
                if pivot_idx == k:
                    return
                # If pivot index is greater than k, look left
                elif pivot_idx > k:
                    quickselect(arr, low, pivot_idx - 1, k)
                # If pivot index is less than k, look right
                else:
                    quickselect(arr, pivot_idx + 1, high, k)

        def get_top_k_smallest(arr, k):
            if k <= 0 or k > len(arr):
                return []
            # k elements means we want indices 0 to k-1, so target index is k
            quickselect(arr, 0, len(arr) - 1, k)
            return arr[:k]
        
        return [r[1] for r in get_top_k_smallest(res, k)]
        

