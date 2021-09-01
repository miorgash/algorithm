from itertools import chain
nums = [8,1,2,2,3]
# [4,0,1,1,3]
def smallerNumbersThanCurrent(nums):
    return [sum(map(lambda x: x<i, nums)) for i in nums]

smallerNumbersThanCurrent(nums)