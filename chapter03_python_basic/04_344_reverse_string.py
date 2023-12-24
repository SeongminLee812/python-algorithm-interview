def reverse_string(S):
    left, right = 0, len(S) - 1
    while left < right:
        S[left], S[right] = S[right], S[left]
        left += 1
        right -= 1

    return S

def reverse_string(S):
    S[:] = S[::-1]

print(reverse_string(['h', 'e', 'l', 'l' ,'o']))

