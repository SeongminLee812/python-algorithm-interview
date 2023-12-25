from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] + nums[j] == target:
                    return [i, j]

print(twoSum([2,7,11,15], 9))

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        other_num = target - nums[i]
        if (other_num in nums) and (i != nums.index(other_num)):
            return [i, nums.index(other_num)]

print(twoSum([2, 7, 11, 5], 9))

def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + (i + 1)] # i+1번째 요소가 0인덱스로 변경되므로 i+1을 붙여서 반환
print(twoSum([2, 7, 11, 5], 9))


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

print(twoSum([2, 7, 11, 5], 9))

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
        nums_map[num] = i

print(twoSum([2, 7, 11, 5], 9))

