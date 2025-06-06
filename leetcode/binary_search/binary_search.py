from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low = 0
        high = size
        mid = (low + high) // 2
        while low != high:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            mid = (low + high) // 2
        return -1

if __name__ == "__main__":
    input_ar = [-1,0,3,5,9,12]
    print(Solution().search(input_ar, 9)) # 
    print(Solution().search(input_ar, 2)) # 