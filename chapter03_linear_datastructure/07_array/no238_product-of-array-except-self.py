from typing import *
def productExceptSelf(nums: List[int]) -> List[int]:
    results = []

    left_out = []
    right_out = []
    for idx, num in enumerate(nums):
        left_p = 1
        right_p = 1

        if idx > 0:
            for i in nums[:idx]:
                left_p *= i
        if idx < len(nums) - 1:
            for j in nums[idx + 1:]:
                right_p *= j
        left_out.append(left_p)
        right_out.append(right_p)

    print(left_out)
    print(right_out)

    for l, r in zip(left_out, right_out):
        results.append(l * r)

    return results

# print(productExceptSelf([1, 2, 3, 4]))

def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    left_p = 1

    for i in range(0, len(nums)):
        out.append(left_p)
        left_p *= nums[i]

    right_p = 1
    for j in range(len(nums) - 1, -1, -1):
        out[j] = out[j] * right_p
        right_p = right_p * nums[j]

    return out

productExceptSelf([1, 2, 3, 4])