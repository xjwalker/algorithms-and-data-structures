from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

if __name__ == "__main__":
    print(Solution().search([3,4,5,1,2], 5)) # 2
    print(Solution().search([4,5,6,7,0,1,2], 8)) # -1
    print(Solution().search([18,11,13,15,17], 18)) # 0
    print(Solution().search([5,1,2,3,4], 4)) #  4
