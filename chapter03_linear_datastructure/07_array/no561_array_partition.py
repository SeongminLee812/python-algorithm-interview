from typing import *
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    results_list = []
    for i in range(0, len(nums), 2):
        results_list.append(min(nums[i], nums[i+1]))

    result = sum(results_list)

    return result

print(arrayPairSum([6,2,6,5,1,2]))

def arrayPairSum(nums: List[int]) -> int:
    sums = 0
    pair = []
    nums.sort()
    for n in nums:
        pair.append(n)
        if len(pair)==2:
            sums += min(pair)
            pair = []

    return sums

def arrayPairSum(nums: List[int]) -> int:
    sums = 0
    nums.sort()
    for i, n in enumerate(nums):
        if i % 2 == 0:
            sums += n

    return sums

print(arrayPairSum([6,2,6,5,1,2]))

def arrayPairSum(nums: List[int]) -> int:
    # pythonic way
    return sum(sorted(nums)[::2])

print(arrayPairSum([6,2,6,5,1,2]))
