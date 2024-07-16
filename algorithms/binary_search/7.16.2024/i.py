# 07/16/2024
# Blind Practice writing iterative binary search

def bsearch(nums, target): 

    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if(nums[mid] == target):
            return mid
        elif nums[mid] > target: # search left
            right = mid - 1
        else:
            left = mid + 1

    return -1


nums = [1,2,3,4,5,6,7,8,9,12,34,65]

target = 12
target2 = 66

print(bsearch(nums, target))
print(bsearch(nums, target2))

