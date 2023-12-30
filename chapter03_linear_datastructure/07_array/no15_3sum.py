from typing import *
def threeSum(nums: List[int]) -> List[List[int]]:
    # 브루트 포스(쓰리 포인터)
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result

def threeSum(nums: List[int]) -> List[List[int]]:
    # 투 포인터를 이용한 문제풀이
    nums.sort()
    results = []
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i-1] == nums[i]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < 0:
                left += 1
            elif sums > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results

print(threeSum([-1,0,1,2,-1,-4]))