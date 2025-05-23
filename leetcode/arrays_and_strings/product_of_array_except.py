def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        response = []
        prefix = 1
        for i in range(len(nums)):
            response.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) -1 , -1, -1):
            response[i] *= suffix
            suffix *= nums[i]

        return response

if __name__ == "__main__":
    # expecte value [24,12,8,6]
    print(productExceptSelf([1,2,3,4]))