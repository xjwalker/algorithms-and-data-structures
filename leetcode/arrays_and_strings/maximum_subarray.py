def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_num = float('-inf')
    agg = 0
    
    for i in range(len(nums)):
        agg += nums[i]
        if agg > max_num:
            max_num = agg
        if agg < 0:
            agg = 0
            
    return max_num

if __name__ == "__main__":
    # expected value 6
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))