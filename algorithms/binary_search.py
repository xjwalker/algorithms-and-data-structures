def binary_search(nums: list[int], target: int) -> bool: 
    low = 0
    high = len(nums) - 1
    while low <= len(nums) -1 and high >= 0:
        m = (low + high) // 2
        if nums[m] == target:
            return True
        if nums[m] > target:
            high = m - 1
        elif nums[m] < target:
            low = m + 1

    return False

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5], 1))
    print(binary_search([1,2,3,4,5], 5))
    print(binary_search([1,2,3,4,5], 8))
    print(binary_search([1,2,3,4,5], 0))
            