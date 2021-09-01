from typing import List

# case1
# nums = [2,7,11,15]
# target = 9

# case2
# nums = [3,2,4]
# target = 6

# case 3
nums = [3,3]
target = 6

# submission
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i+1:], start=i+1):
            if target==(n+m):
                break
        if target==(n+m):
            break

    return [i, j]

twoSum(nums, target)