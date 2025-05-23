def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    # expecte value True
    print(containsDuplicate([7,1,5,3,6,5]))