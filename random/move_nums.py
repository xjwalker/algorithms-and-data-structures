nums = [1,2,3,5,9]

print(nums)
first = nums[0] # 2,3,5,9,1
for i in range(1, len(nums)): # 2, 3, 5, 9, 1
    last_value = nums[i] # 9
    nums[i-1] = last_value

nums[len(nums) -1] = first
print(nums)


nums = [1,2,3,5,9] # 9,1,2,3,5
last_value = nums[0] # 1
aux = 0
aux_last = nums[len(nums) -1] # 9
for i in range(1,len(nums)): # 1,2,3,5,5
    aux = nums[i] # 3
    nums[i]= last_value # 2
    last_value = aux # 3

nums[0] = aux_last
print(nums)