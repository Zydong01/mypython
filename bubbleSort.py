
def sort(nums):
    for j in range(len(nums), 2, -1):
        for i in range(0, j-1):
            if nums[i] > nums[i+1]:
                t = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = t
nums = [5, 2, 6, 8, 4, 3]
nums.sort()
print(nums)
