# 07/16/2024
# Blind Practice writing iterative binary search

def bsearch(nums, left, right, target):
    
    if left <= right:
    
        mid = (left + right) // 2
        if nums[mid] > target:
            return bsearch(nums,left, mid-1, target)
        elif nums[mid] < target:
            return bsearch(nums, mid+1, right, target)
        else:
            return mid
    else:
        return -1

nums = [1,2,3,4,5,6,7,8,9,12,34,65]

target = 12
target2 = 66

n = len(nums)-1

print(bsearch(nums, 0, n, target))
print(bsearch(nums, 0, n, target2))