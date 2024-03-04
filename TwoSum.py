class Solution:
    def mergeSort(self, arr):
        if len(arr) > 1:
 
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # Into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            self.mergeSort(L)
    
            # Sorting the second half
            self.mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = nums.copy()
        self.mergeSort(sorted)
        arr = [0, (len(sorted) - 1)]

        sum = sorted[arr[0]] + sorted[arr[1]]

        while (sum != target):
            sum = sorted[arr[0]] + sorted[arr[1]]
            if (sum > target):
                arr[1] -= 1
            elif (sum < target):
                arr[0] += 1

        for i in range(0, len(nums)):
            if (nums[i] == sorted[arr[0]]):
                arr[0] = i
                break
        
        for i in reversed(range(len(nums))):
            if (nums[i] == sorted[arr[1]]):
                arr[1] = i
                break
        return arr
    
###################
# runtime is O(n log n + n + n + n) --> O(n log n)
###################