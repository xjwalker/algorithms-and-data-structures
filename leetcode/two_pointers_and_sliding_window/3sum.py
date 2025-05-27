from typing import List

class Solution:
    def two_sum(self,seen_nums,  nums, target, index):
        for i in range(len(nums)):
            if i == index:
                continue
            if target - nums[i] in seen_nums:
                return [i, seen_nums[target - nums[i]]]
        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        seen_nums = {num: index for index, num in enumerate(nums)}
        seen_indexes = {}
        for i in range(len(nums)-1):
            vals = self.two_sum(seen_nums, nums, nums[i] * -1, index)
            if not vals:
                continue
            vals.extend([i])
            vals.sort()
            new_vals = [str(i) for i in vals]
            key = "".join(new_vals)
            if key in seen_indexes:
                continue
            seen_indexes[key] = [nums[value] for value in vals]
        print(seen_indexes)
        return [values for _, values in seen_indexes.items()]

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(Solution().threeSum([0,1,1])) # []
    print(Solution().threeSum([0,0,0]))   # [[0,0,0]]
