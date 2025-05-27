class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nums = {}
        for index, number in enumerate(numbers):
            value = target - number #  2
            if value in nums: # true
                return [nums[value] + 1, index + 1]
            nums[number] = index # 2:0, 

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9)) # [1,2]
    print(Solution().twoSum([2,3,4], 6)) # [1,3]
    print(Solution().twoSum([-1,0], -1))   # [1,2]
    
    print(len([0,321,4354325432,7,4,5])//2)