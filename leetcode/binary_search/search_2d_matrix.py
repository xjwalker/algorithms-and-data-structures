from typing import List
class Solution:

    def binary_search(self, nums, target):
        size = len(nums)
        low = 0
        high = size
        mid = (low + high) // 2
        while low != high:
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            mid = (low + high) // 2
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = len(matrix) - 1
        # print('start', matrix[row_index], target)
        while row_index >= 0:
            if self.binary_search(matrix[row_index], target):
                return True
            row_index -= 1
        return False

if __name__ == "__main__":
    input_ar = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(Solution().searchMatrix(input_ar, 3)) # True
    print(Solution().searchMatrix(input_ar, 13)) # False
