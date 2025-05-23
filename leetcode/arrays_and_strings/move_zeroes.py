
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pointer] = nums[i]
            pointer += 1
        
    for i in range(pointer, len(nums)):
        nums[i] = 0
    print(nums)

if __name__ == "__main__":
    # expected [1,3,12,0,0]
    moveZeroes([0,1,0,3,12])
