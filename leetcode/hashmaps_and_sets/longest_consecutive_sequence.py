class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        max_seq = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                curr = 1
                while current + 1 in nums_set:
                    current += 1
                    curr += 1
                max_seq = max(curr, max_seq)

        return max_seq

if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2]))   # 4
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # 7 
    print(Solution().longestConsecutive([1,0,1,2]))   # 3
