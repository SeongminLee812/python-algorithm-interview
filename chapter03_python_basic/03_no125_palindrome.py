import collections
import re

def solve_my(S: str):
    s = S.lower().strip()
    s = [char for char in s if char in 'abcdefghijklmnopqrstuvwxyz']

    s_original = ''.join(s)
    s.reverse()
    s_reverse = ''.join(s)

    if s_original == s_reverse:
        print('true')
    else:
        print('false')

def solve_list(S: str):
    strs = []
    for char in S:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

def isPalindrome_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum(): # Return True if the string is an alpha-numeric string, False otherwise.
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

def isPalindrome_slicing(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s[:] == s[::-1]


solve_my('A man, a plan, a canal: Panama')
print(solve_list('A man, a plan, a canal: Panama'))
print(isPalindrome_deque('A man, a plan, a canal: Panama'))
print(isPalindrome_slicing('A man, a plan, a canal: Panama'))


a = '안녕하세요'

print(a[::-1])
print(a[:2][::-1])
print(a[::2])