from typing import List

class Solution:
    def two_sum(self, nums, target, target_index):
        # print('**')
        seen_nums = {}
        results = []
        seen = set()
        for i in range(target_index, len(nums)):
            complement = -target - nums[i]
            if complement in seen_nums and f"{target}{complement}{nums[i]}" not in seen:
                seen.add(f"{target}{complement}{nums[i]}")
                results.append([target, complement, nums[i]])
            seen_nums[nums[i]] = i
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            results += self.two_sum(nums, nums[i], i + 1)
        return results


if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(Solution().threeSum([0,1,1])) # []
    print(Solution().threeSum([0,0,0]))   # [[0,0,0]]
    print(Solution().threeSum([0,0,0,0]))   # [[0,0,0]]
