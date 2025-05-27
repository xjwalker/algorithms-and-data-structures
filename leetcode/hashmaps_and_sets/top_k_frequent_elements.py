
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == len(nums):
        return nums
        
    repeat = {}
    for num in nums:
        repeat[num] = repeat.get(num, 0) + 1
        
    bucket = [[] for _ in range(len(nums) + 1)]        
    for num, freq in repeat.items():
        bucket[freq].append(num)

    result = []
    for freq in range(len(bucket) - 1, 0, -1):
        for num in bucket[freq]:
            result.append(num)
            if len(result) == k:
                return result
            
if __name__ == "__main__":
    # expecte value [1,2]
    print(topKFrequent([1,1,1,2,2,3], 2))

