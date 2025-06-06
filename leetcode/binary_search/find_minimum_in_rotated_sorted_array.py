from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while low < high:
            if nums[mid] > nums[high]: 
                low = mid + 1                
            else:
                high = mid
            mid = (high + low) // 2
            
        return nums[low]

if __name__ == "__main__":
    print(Solution().findMin([3,4,5,1,2])) # 1
    print(Solution().findMin([4,5,6,7,0,1,2])) # 0
    print(Solution().findMin([11,13,15,17])) # 11
    print(Solution().findMin([5,1,2,3,4])) #  1
