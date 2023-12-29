from typing import *

def trap(height: List[int]) -> int:
    if not height:
        return 0
    left_pointer, right_pointer = 0, len(height) - 1
    left_max, right_max = height[left_pointer], height[right_pointer]
    volume = 0

    while left_pointer < right_pointer:
        left_max, right_max = max(height[left_pointer], left_max), \
                            max(height[right_pointer], right_max)

        if left_max >= right_max:
            volume += left_max - height[left_pointer]
            left_pointer += 1
        else:
            volume += right_max - height[right_pointer]
            right_pointer -= 1

    return volume

def trap_stack(height: List[int]) -> int:
    stack= []
    volume = 0
    for i in range(len(height)):
        # 변곡점을 맞나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]] - height[top])

            volume += distance * waters

        stack.append(i)
    return volume