def twoSum(nums, target):
        """
        :type nums: List[int]g 
        :type target: int
        :rtype: List[int]
        """
        seen_n = {}
        for index, number in enumerate(nums): # 3 :1
            complement = target - number # 6 - 3: 3
            if complement in seen_n: # 3 in {3:0}?
                return index, seen_n[complement] # 1,0 
            seen_n[number] = index # 3:0
            
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))